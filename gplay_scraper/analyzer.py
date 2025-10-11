import json
from typing import Any, List, Dict, Optional
from datetime import datetime, timezone
import logging

from .core.scraper import PlayStoreScraper
from .core.aso_analyzer import AsoAnalyzer
from .models.element_specs import ElementSpecs
from .utils.helpers import (
    calculate_app_age, calculate_daily_installs, calculate_monthly_installs, clean_json_string
)

# Configure logging only if not already configured
if not logging.getLogger().handlers:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GPlayScraper:
    """Main Google Play Store scraper class.
    
    Provides methods to extract comprehensive app data from Google Play Store
    including ratings, installs, reviews, ASO metrics, and 65+ data fields.
    
    Example:
        >>> scraper = GPlayScraper()
        >>> data = scraper.analyze("com.hubolabs.hubo")
        >>> title = scraper.get_field("com.hubolabs.hubo", "title")
    """
    
    def __init__(
        self,
        proxy: Optional[str] = None,
        proxies: Optional[Dict[str, str]] = None,
    ):
        """Initialize the scraper with required components.

        Args:
            proxy (str, optional): Single proxy URL for all HTTP requests.
            proxies (Dict[str, str], optional): Mapping of scheme to proxy URL.
        """
        self.scraper = PlayStoreScraper(proxy=proxy, proxies=proxies)
        self.aso_analyzer = AsoAnalyzer()
        self._cache = {}  # Cache for analyzed app data

    def analyze(self, app_id: str) -> Dict:
        """Analyze a Google Play Store app and return all available data.
        
        Args:
            app_id (str): The app's package name (e.g., "com.hubolabs.hubo")
            
        Returns:
            Dict: Complete app data with 65+ fields including ratings, installs,
                 reviews, ASO metrics, developer info, and technical details
                 
        Raises:
            ValueError: If app_id is invalid or empty
            Exception: If scraping or parsing fails
            
        Example:
            >>> scraper = GPlayScraper()
            >>> data = scraper.analyze("com.hubolabs.hubo")
            >>> print(f"App: {data['title']}, Rating: {data['score']}")
        """
        # Validate input parameters
        if not app_id or not isinstance(app_id, str):
            raise ValueError("app_id must be a non-empty string")
            
        try:
            # Scrape raw data from Google Play Store
            ds5_data, ds11_data = self.scraper.scrape_play_store_data(app_id)
        except Exception as e:
            raise

        # Clean and parse JSON data
        json_str_cleaned = clean_json_string(ds5_data)
        try:
            data = json.loads(json_str_cleaned)
        except json.JSONDecodeError as e:
            # Try alternative cleaning for paid apps
            try:
                alternative_cleaned = self._alternative_json_clean(ds5_data)
                data = json.loads(alternative_cleaned)
            except Exception:
                raise ValueError(f"Failed to parse ds:5 JSON: {str(e)}")

        # Extract app details using element specifications
        app_details = {}
        for key, spec in ElementSpecs.Detail.items():
            app_details[key] = spec.extract_content(data)

        # Add computed fields
        app_details['appId'] = app_id
        app_details['url'] = f"https://play.google.com/store/apps/details?id={app_id}"

        # Calculate time-based metrics if release date is available
        current_date = datetime.now(timezone.utc)
        release_date_str = app_details.get("released")
        if release_date_str:
            # Calculate app age and install metrics
            app_details["appAge"] = calculate_app_age(release_date_str, current_date)
            app_details["dailyInstalls"] = calculate_daily_installs(app_details.get("installs"), release_date_str, current_date)
            app_details["minDailyInstalls"] = calculate_daily_installs(app_details.get("minInstalls"), release_date_str, current_date)
            app_details["realDailyInstalls"] = calculate_daily_installs(app_details.get("realInstalls"), release_date_str, current_date)
            app_details["monthlyInstalls"] = calculate_monthly_installs(app_details.get("installs"), release_date_str, current_date)
            app_details["minMonthlyInstalls"] = calculate_monthly_installs(app_details.get("minInstalls"), release_date_str, current_date)
            app_details["realMonthlyInstalls"] = calculate_monthly_installs(app_details.get("realInstalls"), release_date_str, current_date)
        else:
            # Set metrics to None if no release date available
            metric_keys = [
                "appAge", "dailyInstalls", "minDailyInstalls", "realDailyInstalls",
                "monthlyInstalls", "minMonthlyInstalls", "realMonthlyInstalls"
            ]
            for key in metric_keys:
                app_details[key] = None

        # Perform ASO analysis and extract reviews
        app_details['keywordAnalysis'] = self.aso_analyzer.analyze_app_text(app_details)
        app_details['reviewsData'] = self.scraper.extract_reviews(ds11_data)

        return self._format_app_details(app_details)
    
    def _alternative_json_clean(self, json_str: str) -> str:
        """Alternative JSON cleaning method for problematic paid app data."""
        import re
        import json
        
        # Try to extract the data array using bracket matching
        data_start = json_str.find('data:')
        if data_start != -1:
            bracket_start = json_str.find('[', data_start)
            if bracket_start != -1:
                # Find matching closing bracket
                bracket_count = 0
                pos = bracket_start
                
                while pos < len(json_str):
                    if json_str[pos] == '[':
                        bracket_count += 1
                    elif json_str[pos] == ']':
                        bracket_count -= 1
                        if bracket_count == 0:
                            data_end = pos + 1
                            break
                    pos += 1
                
                if bracket_count == 0:
                    # Extract the data array
                    data_array = json_str[bracket_start:data_end]
                    
                    try:
                        # Test if the array parses correctly
                        parsed_array = json.loads(data_array)
                        
                        # Create proper JSON structure
                        return json.dumps({
                            "key": "ds:5",
                            "hash": "13",
                            "data": parsed_array
                        })
                    except json.JSONDecodeError:
                        pass
        
        # Fallback: aggressive cleaning
        json_str = re.sub(r',\s*sideChannel:\s*\{\}', '', json_str)
        json_str = re.sub(r'\bfunction\s*\([^)]*\)\s*\{[^}]*\}', 'null', json_str)
        json_str = re.sub(r'\bundefined\b', 'null', json_str)
        json_str = re.sub(r'\bNaN\b', 'null', json_str)
        
        # Handle malformed objects with missing quotes
        json_str = re.sub(r'([{,]\s*)([a-zA-Z_$][a-zA-Z0-9_$]*)\s*:', r'\1"\2":', json_str)
        
        # Fix price formatting issues
        json_str = re.sub(r':\s*\$([0-9.,]+)', r': "$\1"', json_str)
        
        # Remove trailing commas
        json_str = re.sub(r',\s*([}\]])', r'\1', json_str)
        
        # Fix multiple commas
        json_str = re.sub(r',,+', ',', json_str)
        
        return json_str

    def _format_app_details(self, details: dict) -> dict:
        """Format and structure app details into final output format.
        
        Args:
            details (dict): Raw app details from scraping and analysis
            
        Returns:
            dict: Formatted app data with standardized field names
        """
        keyword_analysis = details.get("keywordAnalysis", {})
        
        # Build organized result dictionary
        result = {}
        
        # Basic Information
        result["appId"] = details.get("appId")
        result["title"] = details.get("title")
        result["summary"] = details.get("summary")
        result["description"] = details.get("description")
        result["appUrl"] = details.get("url")
        
        # Category & Genre
        result["genre"] = details.get("genre")
        result["genreId"] = details.get("genreId")
        result["categories"] = details.get("categories")
        result["available"] = details.get("available")
        
        # Release & Updates
        result["released"] = details.get("released")
        result["appAgeDays"] = details.get("appAge")
        result["lastUpdated"] = details.get("lastUpdatedOn")
        result["updatedTimestamp"] = details.get("updated")
        
        # Media Content
        result["icon"] = details.get("icon")
        result["headerImage"] = details.get("headerImage")
        result["screenshots"] = details.get("screenshots")
        result["video"] = details.get("video")
        result["videoImage"] = details.get("videoImage")
        
        # Install Statistics
        result["installs"] = details.get("installs")
        result["minInstalls"] = details.get("minInstalls")
        result["realInstalls"] = details.get("realInstalls")
        result["dailyInstalls"] = details.get("dailyInstalls")
        result["minDailyInstalls"] = details.get("minDailyInstalls")
        result["realDailyInstalls"] = details.get("realDailyInstalls")
        result["monthlyInstalls"] = details.get("monthlyInstalls")
        result["minMonthlyInstalls"] = details.get("minMonthlyInstalls")
        result["realMonthlyInstalls"] = details.get("realMonthlyInstalls")
        
        # Ratings & Reviews
        result["score"] = details.get("score")
        result["ratings"] = details.get("ratings")
        result["reviews"] = details.get("reviews")
        result["histogram"] = details.get("histogram")
        result["reviewsData"] = details.get("reviewsData")
        
        # Advertising
        result["adSupported"] = details.get("adSupported")
        result["containsAds"] = details.get("containsAds")
        
        # Technical Details
        result["version"] = details.get("version")
        result["androidVersion"] = details.get("androidVersion")
        result["maxAndroidApi"] = details.get("maxandroidapi")
        result["minAndroidApi"] = details.get("minandroidapi")
        result["appBundle"] = details.get("appBundle")
        
        # Content Rating
        result["contentRating"] = details.get("contentRating")
        result["contentRatingDescription"] = details.get("contentRatingDescription")
        result["whatsNew"] = details.get("whatsNew")
        
        # Privacy & Security
        result["permissions"] = details.get("permissions")
        result["dataSafety"] = details.get("dataSafety")
        
        # Pricing & Monetization
        result["price"] = details.get("price")
        result["currency"] = details.get("currency")
        result["free"] = details.get("free")
        result["offersIAP"] = details.get("offersIAP")
        result["inAppProductPrice"] = details.get("inAppProductPrice")
        result["sale"] = details.get("sale")
        result["originalPrice"] = details.get("originalPrice")
        
        # Developer Information
        result["developer"] = details.get("developer")
        result["developerId"] = details.get("developerId")
        result["developerEmail"] = details.get("developerEmail")
        result["developerWebsite"] = details.get("developerWebsite")
        result["developerAddress"] = details.get("developerAddress")
        result["developerPhone"] = details.get("developerPhone")
        result["privacyPolicy"] = details.get("privacyPolicy")
        
        # ASO (App Store Optimization) Analysis
        result["totalWords"] = keyword_analysis.get("total_words")
        result["uniqueKeywords"] = keyword_analysis.get("unique_keywords")
        result["topKeywords"] = keyword_analysis.get("top_keywords")
        result["topBigrams"] = keyword_analysis.get("top_bigrams")
        result["topTrigrams"] = keyword_analysis.get("top_trigrams")
        result["competitiveKeywords"] = keyword_analysis.get("competitive_analysis")
        result["readability"] = keyword_analysis.get("readability")
        
        return result

    def _get_cached_data(self, app_id: str) -> Dict:
        """Get cached app data or analyze if not cached.
        
        Args:
            app_id (str): App package name
            
        Returns:
            Dict: Complete app analysis data
        """
        if app_id not in self._cache:
            self._cache[app_id] = self.analyze(app_id)
        return self._cache[app_id]

    def get_field(self, app_id: str, field: str) -> Any:
        """Get a specific field value from app analysis.
        
        Args:
            app_id (str): App package name (e.g., "com.hubolabs.hubo")
            field (str): Field name to retrieve (e.g., "title", "score")
            
        Returns:
            Any: Field value or None if not found
            
        Example:
            >>> scraper = GPlayScraper()
            >>> title = scraper.get_field("com.hubolabs.hubo", "title")
        """
        return self._get_cached_data(app_id).get(field)

    def get_fields(self, app_id: str, fields: List[str]) -> Dict[str, Any]:
        """Get multiple specific fields from app analysis.
        
        Args:
            app_id (str): App package name
            fields (List[str]): List of field names to retrieve
            
        Returns:
            Dict[str, Any]: Dictionary with requested fields and values
            
        Example:
            >>> scraper = GPlayScraper()
            >>> data = scraper.get_fields("com.hubolabs.hubo", ["title", "score", "installs"])
        """
        data = self._get_cached_data(app_id)
        return {field: data.get(field) for field in fields}

    def print_field(self, app_id: str, field: str) -> None:
        """Print a specific field value to console.
        
        Args:
            app_id (str): App package name
            field (str): Field name to print
            
        Example:
            >>> scraper = GPlayScraper()
            >>> scraper.print_field("com.hubolabs.hubo", "title")
            title: purp - Make new friends
        """
        value = self.get_field(app_id, field)
        try:
            print(f"{field}: {value}")
        except UnicodeEncodeError:
            # Handle Unicode characters that can't be displayed
            print(f"{field}: {repr(value)}")

    def print_fields(self, app_id: str, fields: List[str]) -> None:
        """Print multiple field values to console.
        
        Args:
            app_id (str): App package name
            fields (List[str]): List of field names to print
            
        Example:
            >>> scraper = GPlayScraper()
            >>> scraper.print_fields("com.hubolabs.hubo", ["title", "score", "developer"])
        """
        data = self.get_fields(app_id, fields)
        for field, value in data.items():
            try:
                print(f"{field}: {value}")
            except UnicodeEncodeError:
                # Handle Unicode characters that can't be displayed
                print(f"{field}: {repr(value)}")

    def print_all(self, app_id: str) -> None:
        """Print all app data as formatted JSON.
        
        Args:
            app_id (str): App package name
            
        Example:
            >>> scraper = GPlayScraper()
            >>> scraper.print_all("com.hubolabs.hubo")
            # Outputs complete JSON with all 65+ fields
        """
        data = self._get_cached_data(app_id)
        try:
            # Print with Unicode support
            print(json.dumps(data, indent=2, ensure_ascii=False))
        except UnicodeEncodeError:
            # Fallback to ASCII-safe output
            print(json.dumps(data, indent=2, ensure_ascii=True))
