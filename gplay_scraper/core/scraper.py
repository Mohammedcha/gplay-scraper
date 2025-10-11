import re
import json
import time
import logging
from typing import List, Dict, Tuple

from curl_cffi import requests as curl_requests
from curl_cffi.requests import exceptions as curl_exceptions

from gplay_scraper.utils.helpers import clean_json_string
from gplay_scraper.config import Config

logger = logging.getLogger(__name__)


class PlayStoreScraper:
    """Core scraper for Google Play Store web pages.
    
    Handles HTTP requests, HTML parsing, and data extraction from
    Google Play Store app pages.
    """
    
    def __init__(self, rate_limit_delay: float = None):
        """Initialize scraper with browser-like headers and rate limiting.
        
        Args:
            rate_limit_delay (float): Minimum seconds between requests (uses Config default if None)
        """
        # Use configuration for headers and settings
        request_config = Config.get_request_config()
        self.headers = request_config["headers"]
        self.timeout = request_config["timeout"]
        self.impersonate = request_config.get("impersonate", Config.DEFAULT_IMPERSONATE)
        
        # Rate limiting configuration
        self.rate_limit_delay = rate_limit_delay or Config.RATE_LIMIT_DELAY
        self.last_request_time = 0

    def fetch_playstore_page(self, app_id: str) -> str:
        """Fetch HTML content from Google Play Store app page.
        
        Args:
            app_id (str): App package name (e.g., "com.whatsapp")
            
        Returns:
            str: Raw HTML content of the app page
            
        Raises:
            ValueError: If app_id is invalid or malformed
            curl_cffi.requests.exceptions.RequestException: If HTTP request fails
        """
        # Validate input parameters
        if not app_id or not isinstance(app_id, str):
            raise ValueError("app_id must be a non-empty string")
        
        # Sanitize app_id to prevent URL injection attacks
        if not re.match(r'^[a-zA-Z0-9._]+$', app_id):
            raise ValueError("Invalid app_id format")
            
        # Apply rate limiting
        self._rate_limit()
        
        url = f"https://play.google.com/store/apps/details?id={app_id}&hl=en&gl=US"
        try:
            resp = curl_requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout,
                impersonate=self.impersonate,
                default_headers=False,
            )
            resp.raise_for_status()
            return resp.text
        except curl_exceptions.Timeout:
            logger.error(f"Timeout while fetching Play Store page for {app_id}")
            raise
        except curl_exceptions.ConnectionError:
            logger.error(f"Connection error while fetching Play Store page for {app_id}")
            raise
        except curl_exceptions.RequestException as e:
            logger.error(f"Failed to fetch Play Store page for {app_id}: {e}")
            raise

    def scrape_play_store_data(self, app_id: str) -> Tuple[str, str]:
        """Extract structured data from Google Play Store app page.
        
        Args:
            app_id (str): App package name
            
        Returns:
            Tuple[str, str]: (ds:5 data, ds:11 data) containing app info and reviews
            
        Raises:
            ValueError: If required data sections are not found
        """
        html = self.fetch_playstore_page(app_id)
        
        # Extract ds:5 (app data) and ds:11 (reviews data) from JavaScript callbacks
        ds5_data = None
        ds11_data = None
        
        # Try direct regex patterns first
        ds5_match = re.search(r'AF_initDataCallback\s*\(\s*({\s*key:\s*["\']ds:5["\'][\s\S]*?})\s*\)\s*;', html, re.DOTALL)
        if ds5_match:
            ds5_data = ds5_match.group(1)
            
        ds11_match = re.search(r'AF_initDataCallback\s*\(\s*({\s*key:\s*["\']ds:11["\'][\s\S]*?})\s*\)\s*;', html, re.DOTALL)
        if ds11_match:
            ds11_data = ds11_match.group(1)
        
        # Fallback: search all callbacks only if needed
        if not ds5_data or not ds11_data:
            all_callbacks = re.findall(r'AF_initDataCallback\s*\(\s*({[\s\S]*?})\s*\)\s*;', html, re.DOTALL)
            for callback in all_callbacks:
                if not ds5_data and ("'ds:5'" in callback or '"ds:5"' in callback):
                    ds5_data = callback
                elif not ds11_data and ("'ds:11'" in callback or '"ds:11"' in callback):
                    ds11_data = callback
                if ds5_data and ds11_data:
                    break
        
        if not ds5_data:
            raise ValueError("Could not find ds:5 data")
        if not ds11_data:
            logger.warning("Could not find ds:11 (reviews) data")

        return ds5_data, ds11_data

    def extract_reviews(self, ds11_data: str) -> List[Dict]:
        """Extract and parse user reviews from ds:11 data.
        
        Args:
            ds11_data (str): Raw ds:11 JSON string containing reviews
            
        Returns:
            List[Dict]: List of review dictionaries with user, rating, text, etc.
        """
        if not ds11_data:
            return []

        try:
            data = json.loads(clean_json_string(ds11_data))
            data = data.get('data', data)
        except Exception:
            # Try alternative parsing with bracket matching
            try:
                data_start = ds11_data.find('data:')
                if data_start != -1:
                    bracket_start = ds11_data.find('[', data_start)
                    if bracket_start != -1:
                        bracket_count = 0
                        pos = bracket_start
                        while pos < len(ds11_data):
                            if ds11_data[pos] == '[':
                                bracket_count += 1
                            elif ds11_data[pos] == ']':
                                bracket_count -= 1
                                if bracket_count == 0:
                                    data_end = pos + 1
                                    break
                            pos += 1
                        if bracket_count == 0:
                            data_array = ds11_data[bracket_start:data_end]
                            parsed_array = json.loads(data_array)
                            data = parsed_array
                        else:
                            return []
                    else:
                        return []
                else:
                    return []
            except Exception:
                return []

        # Extract individual review entries
        reviews = []
        try:
            if data and len(data) > 0 and data[0]:
                for entry in data[0]:
                    review = self._parse_review_entry(entry)
                    if review:
                        reviews.append(review)
        except Exception:
            return []

        return reviews

    def _parse_review_entry(self, entry: List) -> Dict:
        """Parse a single review entry from the data structure.
        
        Args:
            entry (List): Raw review data array from Google Play Store
            
        Returns:
            Dict: Parsed review with id, user, rating, text, etc. or None if parsing fails
        """
        try:
            return {
                "id": entry[0],                                    # Review ID
                "user": entry[1][0],                               # Username
                "avatar": entry[1][1][3][2] if entry[1][1] else None,  # Avatar URL
                "rating": entry[2],                                # Star rating (1-5)
                "text": entry[4],                                  # Review text
                "version": entry[10] if len(entry) > 10 else None  # App version reviewed
            }
        except (IndexError, TypeError):
            # Return None if data structure is unexpected
            return None
    
    def _rate_limit(self):
        """Implement rate limiting to avoid overwhelming the server."""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.rate_limit_delay:
            sleep_time = self.rate_limit_delay - time_since_last
            logger.debug(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
