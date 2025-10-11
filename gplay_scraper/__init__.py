import logging

from .analyzer import GPlayScraper
from .config import Config
from .exceptions import (
    GPlayScraperError,
    InvalidAppIdError,
    AppNotFoundError,
    RateLimitError,
    NetworkError,
    DataParsingError,
)

# Configure default logging - users can override
logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = "1.0.2"
__all__ = [
    "GPlayScraper",
    "Config",
    "GPlayScraperError",
    "InvalidAppIdError",
    "AppNotFoundError",
    "RateLimitError",
    "NetworkError",
    "DataParsingError",
]
