"""GPlay Scraper - Google Play Store scraping library.

This package provides comprehensive tools for scraping Google Play Store data including:
- App details (65+ fields)
- Search results
- User reviews
- Developer portfolios
- Similar apps
- Top charts
- Search suggestions
"""

import logging

# Import main scraper class
from .app import GPlayScraper

# Import all method classes
from .core.gplay_methods import AppMethods, SearchMethods, ReviewsMethods, DeveloperMethods, SimilarMethods, ListMethods, SuggestMethods

# Import configuration
from .config import Config

# Import custom exceptions
from .exceptions import (
    GPlayScraperError,
    InvalidAppIdError,
    AppNotFoundError,
    RateLimitError,
    NetworkError,
    DataParsingError,
)

# Configure logging to use NullHandler by default
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Package metadata
__version__ = "1.0.6"

# Public API exports
__all__ = [
    "GPlayScraper",
    "AppMethods",
    "SearchMethods",
    "ReviewsMethods",
    "DeveloperMethods",
    "SimilarMethods",
    "ListMethods",
    "SuggestMethods",
    "Config",
    "GPlayScraperError",
    "InvalidAppIdError",
    "AppNotFoundError",
    "RateLimitError",
    "NetworkError",
    "DataParsingError",
]