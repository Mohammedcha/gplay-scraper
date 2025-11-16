"""Parser classes for extracting and formatting data from raw responses.

This module contains 7 parser classes that handle JSON/HTML parsing and
data formatting for all scraping methods.
"""

import json
import re
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, Tuple
from ..models.element_specs import ElementSpecs, nested_lookup, format_image_url
from ..utils.helpers import clean_json_string, alternative_json_clean, calculate_app_age, calculate_daily_installs, calculate_monthly_installs, tamp_to_date, get_publisher_country
from ..config import Config
from ..exceptions import DataParsingError
from ..utils.error_handling import handle_parsing_errors
from ..utils.helpers import pho_count, add_count

class AppParser:
    """Parser for extracting and formatting app data."""
    @handle_parsing_errors()
    def parse_app_data(self, dataset: Dict, app_id: str, scraper=None, assets: str = None) -> Dict[str, Any]:
        """Parse raw app data from dataset with fallback for missing release date.
        
        Args:
            dataset: Raw dataset from scraper
            app_id: Google Play app ID
            scraper: AppScraper instance for fallback requests
            
        Returns:
            Dictionary with parsed app details
            
        Raises:
            DataParsingError: If parsing fails
        """
        ds5_data = dataset.get("ds:5", "")
        if not ds5_data:
            raise DataParsingError(Config.ERROR_MESSAGES["NO_DS5_DATA"])
        
        json_str_cleaned = clean_json_string(ds5_data)
        try:
            data = json.loads(json_str_cleaned)
        except json.JSONDecodeError as e:
            try:
                alternative_cleaned = alternative_json_clean(ds5_data)
                data = json.loads(alternative_cleaned)
            except Exception:
                raise DataParsingError(Config.ERROR_MESSAGES["JSON_PARSE_FAILED"].format(error=str(e)))

        app_details = {}
        for key, spec in ElementSpecs.App.items():
            value = spec.extract_content(data.get("data", data))
            if key in ["icon", "headerImage", "videoImage"] and value:
                app_details[key] = format_image_url(value, assets)
            elif key == "screenshots" and value:
                app_details[key] = [format_image_url(url, assets) for url in value if url]
            else:
                app_details[key] = value

        app_details['appId'] = app_id
        app_details['url'] = f"{Config.PLAY_STORE_BASE_URL}{Config.APP_DETAILS_ENDPOINT}?id={app_id}"
        app_details['publisherCountry'] = get_publisher_country(app_details.get('developerPhone'), app_details.get('developerAddress'))
        


        rating_fields = ["released", "score", "ratings", "reviews", "histogram"]
        missing_rating_fields = []
        for key in rating_fields:
            value = app_details.get(key)
            if key == "histogram":
                if not value or (isinstance(value, list) and all(x == 0 for x in value)):
                    missing_rating_fields.append(key)
            elif not value:
                missing_rating_fields.append(key)
        
        if missing_rating_fields and scraper:
            try:
                country_code = None
                phone = app_details.get("developerPhone")
                if phone:
                    country_code = pho_count(phone)
                
                if not country_code:
                    address = app_details.get("developerAddress")
                    if address:
                        country_code = add_count(address)
                
                if country_code:
                    fallback_dataset = scraper.fetch_fallback_data(app_id, gl=country_code)
                    suffix = f"fallback_{country_code}"
                else:
                    fallback_dataset = scraper.fetch_fallback_data(app_id, no_locale=True)
                    suffix = "fallback_no_locale"
                
                if fallback_dataset and fallback_dataset.get("ds:5"):
                    fallback_cleaned = clean_json_string(fallback_dataset["ds:5"])
                    try:
                        fallback_data = json.loads(fallback_cleaned)
                        
                        for field in missing_rating_fields:
                            if field in ElementSpecs.App:
                                spec = ElementSpecs.App[field]
                                fallback_value = spec.extract_content(fallback_data.get("data", fallback_data))
                                if fallback_value:
                                    app_details[field] = fallback_value
                    except:
                        pass
            except:
                pass

        if not app_details.get("score"):
            app_details["score"] = 0
        if not app_details.get("ratings"):
            app_details["ratings"] = 0
        if not app_details.get("reviews"):
            app_details["reviews"] = 0
        if not app_details.get("installs"):
            app_details["installs"] = 0
        if not app_details.get("minInstalls"):
            app_details["minInstalls"] = 0

        current_date = datetime.now(timezone.utc)
        release_date_str = app_details.get("released")
        if release_date_str:
            app_details["appAge"] = calculate_app_age(release_date_str, current_date)
            app_details["dailyInstalls"] = calculate_daily_installs(app_details.get("installs"), release_date_str, current_date)
            app_details["minDailyInstalls"] = calculate_daily_installs(app_details.get("minInstalls"), release_date_str, current_date)
            app_details["realDailyInstalls"] = calculate_daily_installs(app_details.get("realInstalls"), release_date_str, current_date)
            app_details["monthlyInstalls"] = calculate_monthly_installs(app_details.get("installs"), release_date_str, current_date)
            app_details["minMonthlyInstalls"] = calculate_monthly_installs(app_details.get("minInstalls"), release_date_str, current_date)
            app_details["realMonthlyInstalls"] = calculate_monthly_installs(app_details.get("realInstalls"), release_date_str, current_date)
        else:
            metric_keys = [
                "appAge", "dailyInstalls", "minDailyInstalls", "realDailyInstalls",
                "monthlyInstalls", "minMonthlyInstalls", "realMonthlyInstalls"
            ]
            for key in metric_keys:
                app_details[key] = 0

        return app_details

    @handle_parsing_errors()
    def format_app_data(self, details: dict) -> dict:
        """Format parsed app data into final structure.
        
        Args:
            details: Parsed app details
            
        Returns:
            Formatted dictionary with all app fields
        """
        return {
            "appId": details.get("appId"),
            "title": details.get("title"),
            "summary": details.get("summary"),
            "description": details.get("description"),
            "genre": details.get("genre"),
            "genreId": details.get("genreId"),
            "categories": details.get("categories"),
            "available": details.get("available"),
            "released": details.get("released"),
            "appAgeDays": details.get("appAge"),
            "lastUpdated": tamp_to_date(details.get("updated")),
            "icon": details.get("icon"),
            "headerImage": details.get("headerImage"),
            "screenshots": details.get("screenshots"),
            "video": details.get("video"),
            "videoImage": details.get("videoImage"),
            "installs": details.get("installs"),
            "minInstalls": details.get("minInstalls"),
            "realInstalls": details.get("realInstalls"),
            "dailyInstalls": details.get("dailyInstalls"),
            "minDailyInstalls": details.get("minDailyInstalls"),
            "realDailyInstalls": details.get("realDailyInstalls"),
            "monthlyInstalls": details.get("monthlyInstalls"),
            "minMonthlyInstalls": details.get("minMonthlyInstalls"),
            "realMonthlyInstalls": details.get("realMonthlyInstalls"),
            "score": details.get("score"),
            "ratings": details.get("ratings"),
            "reviews": details.get("reviews"),
            "histogram": details.get("histogram"),
            "adSupported": details.get("adSupported"),
            "containsAds": details.get("containsAds"),
            "version": details.get("version"),
            "androidVersion": details.get("androidVersion"),
            "maxAndroidApi": details.get("maxandroidapi"),
            "minAndroidApi": details.get("minandroidapi"),
            "appBundle": details.get("appBundle"),
            "contentRating": details.get("contentRating"),
            "contentRatingDescription": details.get("contentRatingDescription"),
            "whatsNew": details.get("whatsNew"),
            "permissions": details.get("permissions"),
            "dataSafety": details.get("dataSafety"),
            "price": details.get("price"),
            "currency": details.get("currency"),
            "free": details.get("free"),
            "offersIAP": details.get("offersIAP"),
            "inAppProductPrice": details.get("inAppProductPrice"),
            "sale": details.get("sale"),
            "originalPrice": details.get("originalPrice"),
            "developer": details.get("developer"),
            "developerId": details.get("developerId"),
            "developerEmail": details.get("developerEmail"),
            "developerWebsite": details.get("developerWebsite"),
            "developerAddress": details.get("developerAddress"),
            "developerPhone": details.get("developerPhone"),
            "publisherCountry": details.get("publisherCountry"),
            "privacyPolicy": details.get("privacyPolicy"),
            "appUrl": details.get("url"),
        }


class SearchParser:
    """Parser for extracting and formatting search results."""
    
    @handle_parsing_errors(return_empty=True)
    def parse_search_results(self, dataset: Dict, count: int) -> List[Dict]:
        """Parse search results from dataset.
        
        Args:
            dataset: Raw dataset from scraper
            count: Maximum number of results to parse
            
        Returns:
            List of parsed search result dictionaries
        """
        if "ds:1" not in dataset:
            return []
        
        search_data = nested_lookup(dataset.get("ds:1", {}), [0, 1, 0, 0, 0])
        
        if not search_data:
            return []
        
        results = []
        n_apps = min(len(search_data), count)
        for i in range(n_apps):
            app = self.extract_search_result(search_data[i])
            if app:
                results.append(app)
        
        return results[:count]

    @handle_parsing_errors()
    def extract_search_result(self, data) -> Dict:
        """Extract single search result from raw data.
        
        Args:
            data: Raw search result data
            
        Returns:
            Dictionary with extracted search result or None if extraction fails
        """
        try:
            result = {}
            for key, spec in ElementSpecs.Search.items():
                result[key] = spec.extract_content(data)
            return result
        except Exception:
            return None

    @handle_parsing_errors()
    def format_search_result(self, result: dict) -> dict:
        """Format parsed search result into final structure.
        
        Args:
            result: Parsed search result
            
        Returns:
            Formatted dictionary with search result fields
        """
        return {
            "appId": result.get("appId"),
            "title": result.get("title"),
            "description": result.get("summary"),
            "icon": result.get("icon"),
            "developer": result.get("developer"),
            "score": result.get("score"),
            "scoreText": result.get("scoreText"),
            "currency": result.get("currency"),
            "price": result.get("price"),
            "free": result.get("free"),
            "url": result.get("url"),
        }
    
    @handle_parsing_errors()
    def extract_pagination_token(self, dataset: Dict) -> str:
        """Extract pagination token from search dataset.
        
        Args:
            dataset: Search dataset
            
        Returns:
            Pagination token or None
        """
        sections = nested_lookup(dataset.get("ds:1", {}), [0, 1, 0, 0])
        
        if not sections:
            return None
            
        for section in sections:
            if isinstance(section, list) and len(section) > 1:
                potential_token = nested_lookup(section, [1])
                if isinstance(potential_token, str):
                    return potential_token
        return None
    
    @handle_parsing_errors()
    def parse_html_content(self, html_content: str) -> Dict:
        """Extract datasets from search page HTML.
        
        Args:
            html_content: HTML content of search page
            
        Returns:
            Dictionary containing all datasets
            
        Raises:
            DataParsingError: If no datasets found
        """
        script_regex = re.compile(r"AF_initDataCallback[\s\S]*?</script")
        key_regex = re.compile(r"(ds:.*?)'")
        value_regex = re.compile(r"data:([\s\S]*?), sideChannel: \{\}\}\);</")
        
        matches = script_regex.findall(html_content)
        dataset = {}
        
        for match in matches:
            key_match = key_regex.findall(match)
            value_match = value_regex.findall(match)
            
            if key_match and value_match:
                key = key_match[0]
                try:
                    value = json.loads(value_match[0])
                    dataset[key] = value
                except json.JSONDecodeError:
                    continue
        
        if not dataset:
            raise DataParsingError("No search data found in HTML")
        
        return dataset


class ReviewsParser:
    """Parser for extracting and formatting user reviews."""
    
    @handle_parsing_errors(return_empty=True)
    def parse_reviews_response(self, content: str) -> Tuple[List[Dict], Optional[str]]:
        """Parse reviews from API response content.
        
        Args:
            content: Raw API response content
            
        Returns:
            Tuple of (list of review dictionaries, next page token)
        """
        if not content or not isinstance(content, str):
            return [], None
            
        regex = re.compile(r"\)]}'\n\n([\s\S]+)")
        matches = regex.findall(content)
        
        if not matches:
            return [], None
        
        try:
            data = json.loads(matches[0])
            if not data or len(data) == 0 or len(data[0]) < 3:
                return [], None
                
            reviews_data = json.loads(data[0][2])
            
            # Handle case where reviews_data is None or empty
            if not reviews_data:
                return [], None
                
            next_token = None
            try:
                if (isinstance(reviews_data, list) and len(reviews_data) >= 2 and 
                    reviews_data[-2] and isinstance(reviews_data[-2], list) and len(reviews_data[-2]) > 0):
                    potential_token = reviews_data[-2][-1]
                    if isinstance(potential_token, str):
                        next_token = potential_token
            except (IndexError, TypeError, AttributeError):
                pass
            
            # Check if we have actual reviews data
            if (not isinstance(reviews_data, list) or len(reviews_data) == 0 or 
                not isinstance(reviews_data[0], list) or len(reviews_data[0]) == 0):
                return [], None
            
            reviews = []
            for review_raw in reviews_data[0]:
                if review_raw:  # Make sure review_raw is not None
                    review = self.extract_review_data(review_raw)
                    if review:
                        reviews.append(review)
            
            return reviews, next_token
            
        except (json.JSONDecodeError, IndexError, KeyError, TypeError, AttributeError):
            return [], None

    @handle_parsing_errors()
    def extract_review_data(self, review_raw) -> Optional[Dict]:
        """Extract single review from raw data.
        
        Args:
            review_raw: Raw review data array
            
        Returns:
            Dictionary with extracted review data or None if extraction fails
        """
        try:
            review = {
                "reviewId": review_raw[0] if len(review_raw) > 0 else None,
                "userName": review_raw[1][0] if len(review_raw) > 1 and review_raw[1] else None,
                "userImage": None,
                "content": review_raw[4] if len(review_raw) > 4 else None,
                "score": review_raw[2] if len(review_raw) > 2 else None,
                "thumbsUpCount": review_raw[6] if len(review_raw) > 6 else None,
                "at": datetime.fromtimestamp(review_raw[5][0]).isoformat() if len(review_raw) > 5 and review_raw[5] else None,
                "appVersion": review_raw[10] if len(review_raw) > 10 else None,
            }
            try:
                if len(review_raw) > 1 and review_raw[1] and len(review_raw[1]) > 1 and review_raw[1][1]:
                    review["userImage"] = review_raw[1][1][3][2]
            except:
                pass
            return review
        except Exception:
            return None

    @handle_parsing_errors(return_empty=True)
    def parse_multiple_responses(self, dataset: Dict) -> List[Dict]:
        """Parse multiple review responses.
        
        Args:
            dataset: Dataset containing multiple review responses
            
        Returns:
            List of all parsed reviews
        """
        if not dataset or not isinstance(dataset, dict):
            return []
            
        responses = dataset.get("reviews", [])
        if not responses or not isinstance(responses, list):
            return []
            
        all_reviews = []
        
        for response in responses:
            if response and isinstance(response, str):
                try:
                    reviews, _ = self.parse_reviews_response(response)
                    if reviews:  # Only extend if we got actual reviews
                        all_reviews.extend(reviews)
                except Exception:
                    continue  # Skip this response if it fails
        
        return all_reviews

    @handle_parsing_errors(return_empty=True)
    def format_reviews_data(self, reviews_data: List[Dict]) -> List[Dict]:
        """Format parsed reviews into final structure.
        
        Args:
            reviews_data: List of parsed reviews
            
        Returns:
            List of formatted review dictionaries
        """
        formatted_reviews = []
        
        for review in reviews_data:
            formatted_review = {
                "reviewId": review.get("reviewId"),
                "userName": review.get("userName"),
                "userImage": review.get("userImage"),
                "score": review.get("score"),
                "content": review.get("content"),
                "thumbsUpCount": review.get("thumbsUpCount"),
                "appVersion": review.get("appVersion"),
                "at": review.get("at"),
            }
            formatted_reviews.append(formatted_review)
        
        return formatted_reviews


class DeveloperParser:
    """Parser for extracting and formatting developer apps."""
    
    @handle_parsing_errors(return_empty=True)
    def parse_developer_data(self, dataset: Dict, dev_id: str) -> List[Dict]:
        """Parse developer apps from dataset.
        
        Args:
            dataset: Raw dataset from scraper
            dev_id: Developer ID (numeric or string)
            
        Returns:
            List of parsed app dictionaries
            
        Raises:
            DataParsingError: If parsing fails
        """
        ds3_data = dataset.get("ds:3", "")
        if not ds3_data:
            raise DataParsingError(Config.ERROR_MESSAGES["NO_DS3_DATA"])
        
        json_str_cleaned = clean_json_string(ds3_data)
        try:
            data = json.loads(json_str_cleaned)
        except json.JSONDecodeError as e:
            try:
                alternative_cleaned = alternative_json_clean(ds3_data)
                data = json.loads(alternative_cleaned)
            except Exception:
                raise DataParsingError(Config.ERROR_MESSAGES["DS3_JSON_PARSE_FAILED"].format(error=str(e)))

        # Navigate to apps array based on dev_id type
        is_numeric = dev_id.isdigit()
        if is_numeric:
            apps_path = [0, 1, 0, 21, 0]
        else:
            apps_path = [0, 1, 0, 22, 0]
        
        apps_data = nested_lookup(data.get("data", data), apps_path)
        if not apps_data:
            return []
        
        apps = []
        for app_data in apps_data:
            app_details = {}
            for key, spec in ElementSpecs.Developer.items():
                app_details[key] = spec.extract_content(app_data)
            
            if app_details.get("title"):
                apps.append(app_details)
        
        return apps

    @handle_parsing_errors(return_empty=True)
    def format_developer_data(self, apps_data: List[Dict]) -> List[Dict]:
        """Format parsed developer apps into final structure.
        
        Args:
            apps_data: List of parsed apps
            
        Returns:
            List of formatted app dictionaries
        """
        formatted_apps = []
        
        for app in apps_data:
            formatted_app = {
                "appId": app.get("appId"),
                "title": app.get("title"),
                "description": app.get("description"),
                "icon": app.get("icon"),
                "developer": app.get("developer"),
                "score": app.get("score"),
                "scoreText": app.get("scoreText"),
                "currency": app.get("currency"),
                "price": app.get("price"),
                "free": app.get("free"),
                "url": app.get("url"),
            }
            formatted_apps.append(formatted_app)
        
        return formatted_apps


class SimilarParser:
    """Parser for extracting and formatting similar apps."""
    
    @handle_parsing_errors(return_empty=True)
    def parse_similar_data(self, dataset: Dict) -> List[Dict]:
        """Parse similar apps from dataset.
        
        Args:
            dataset: Raw dataset from scraper
            
        Returns:
            List of parsed similar app dictionaries
        """
        ds3_data = dataset.get("ds:3", "")
        if not ds3_data:
            return []
        
        json_str_cleaned = clean_json_string(ds3_data)
        try:
            data = json.loads(json_str_cleaned)
        except json.JSONDecodeError as e:
            try:
                alternative_cleaned = alternative_json_clean(ds3_data)
                data = json.loads(alternative_cleaned)
            except Exception:
                return []

        apps_data = nested_lookup(data.get("data", data), [0, 1, 0, 21, 0])
        if not apps_data:
            return []
        
        apps = []
        for app_data in apps_data:
            app_details = {}
            for key, spec in ElementSpecs.Similar.items():
                app_details[key] = spec.extract_content(app_data)
            
            if app_details.get("title"):
                apps.append(app_details)
        
        return apps

    @handle_parsing_errors(return_empty=True)
    def format_similar_data(self, apps_data: List[Dict]) -> List[Dict]:
        """Format parsed similar apps into final structure.
        
        Args:
            apps_data: List of parsed apps
            
        Returns:
            List of formatted app dictionaries
        """
        formatted_apps = []
        
        for app in apps_data:
            formatted_app = {
                "appId": app.get("appId"),
                "title": app.get("title"),
                "description": app.get("description"),
                "icon": app.get("icon"),
                "developer": app.get("developer"),
                "score": app.get("score"),
                "scoreText": app.get("scoreText"),
                "currency": app.get("currency"),
                "price": app.get("price"),
                "free": app.get("free"),
                "url": app.get("url"),
            }
            formatted_apps.append(formatted_app)
        
        return formatted_apps


class ListParser:
    """Parser for extracting and formatting top chart apps."""
    
    @handle_parsing_errors(return_empty=True)
    def parse_list_data(self, dataset: Dict, count: int) -> List[Dict]:
        """Parse top chart apps from dataset.
        
        Args:
            dataset: Raw dataset from scraper
            count: Maximum number of apps to parse
            
        Returns:
            List of parsed app dictionaries
        """
        collection_data = dataset.get("collection_data")
        if not collection_data:
            return []
        
        apps_data = nested_lookup(collection_data, [0, 1, 0, 28, 0])
        if not apps_data:
            return []
        
        apps = []
        for app_data in apps_data[:count]:
            app_details = {}
            for key, spec in ElementSpecs.List.items():
                app_details[key] = spec.extract_content(app_data)
            
            if app_details.get("title"):
                apps.append(app_details)
        
        return apps

    @handle_parsing_errors(return_empty=True)
    def format_list_data(self, apps_data: List[Dict]) -> List[Dict]:
        """Format parsed list apps into final structure.
        
        Args:
            apps_data: List of parsed apps
            
        Returns:
            List of formatted app dictionaries
        """
        formatted_apps = []
        
        for app in apps_data:
            formatted_app = {
                "appId": app.get("appId"),
                "title": app.get("title"),
                "description": app.get("description"),
                "icon": app.get("icon"),
                "screenshots": app.get("screenshots"),
                "developer": app.get("developer"),
                "genre": app.get("genre"),
                "score": app.get("score"),
                "scoreText": app.get("scoreText"),
                "installs": app.get("installs"),
                "currency": app.get("currency"),
                "price": app.get("price"),
                "free": app.get("free"),
                "url": app.get("url"),
            }
            formatted_apps.append(formatted_app)
        
        return formatted_apps


class SuggestParser:
    """Parser for extracting and formatting search suggestions."""
    
    @handle_parsing_errors(return_empty=True)
    def parse_suggestions(self, dataset: Dict) -> List[str]:
        """Parse suggestions from dataset.
        
        Args:
            dataset: Raw dataset from scraper
            
        Returns:
            List of suggestion strings
        """
        return dataset.get("suggestions", [])

    @handle_parsing_errors(return_empty=True)
    def format_suggestions(self, suggestions: List[str]) -> List[str]:
        """Format suggestions (pass-through for strings).
        
        Args:
            suggestions: List of suggestion strings
            
        Returns:
            Same list of suggestion strings
        """
        return suggestions