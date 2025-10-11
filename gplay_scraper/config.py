"""Configuration settings for GPlay Scraper."""

from typing import Any, Dict, Optional


class Config:
    """Default configuration settings for the scraper."""

    # Network settings
    DEFAULT_TIMEOUT = 30
    DEFAULT_RETRIES = 3
    RATE_LIMIT_DELAY = 1.0
    DEFAULT_IMPERSONATE = "chrome"
    DEFAULT_PROXY: Optional[str] = None
    DEFAULT_PROXIES: Optional[Dict[str, str]] = None

    # User agent for HTTP client
    DEFAULT_USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    )

    # ASO analysis settings
    ASO_TOP_KEYWORDS = 20
    ASO_MIN_WORD_LENGTH = 3

    # Cache settings
    ENABLE_CACHING = True
    CACHE_MAX_SIZE = 100

    @classmethod
    def get_headers(cls, user_agent: str = None) -> Dict[str, str]:
        """Get HTTP headers for the scraper's HTTP client."""
        return {
            "User-Agent": user_agent or cls.DEFAULT_USER_AGENT
        }

    @classmethod
    def get_request_config(cls) -> Dict[str, Any]:
        """Get default HTTP client configuration."""
        return {
            "timeout": cls.DEFAULT_TIMEOUT,
            "headers": cls.get_headers(),
            "impersonate": cls.DEFAULT_IMPERSONATE,
            "proxy": cls.DEFAULT_PROXY,
            "proxies": cls.DEFAULT_PROXIES,
        }
