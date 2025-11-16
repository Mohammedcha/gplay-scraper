# Google Play Scraper - Python Library 📱

[![PyPI version](https://badge.fury.io/py/gplay-scraper.svg)](https://badge.fury.io/py/gplay-scraper)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-available-brightgreen.svg)](https://mohammedcha.github.io/gplay-scraper/)
[![Downloads](https://pepy.tech/badge/gplay-scraper)](https://pepy.tech/project/gplay-scraper)
[![GitHub stars](https://img.shields.io/github/stars/Mohammedcha/gplay-scraper.svg)](https://github.com/Mohammedcha/gplay-scraper/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/Mohammedcha/gplay-scraper.svg)](https://github.com/Mohammedcha/gplay-scraper/issues)

<div align="center">
  <img src="https://github.com/Mohammedcha/gplay-scraper/blob/main/assets/gplay-scraper.png" alt="GPlay Scraper">
</div>

**GPlay Scraper** is a powerful Python library for extracting comprehensive data from the Google Play Store. Built for developers, data analysts, and researchers, it provides easy access to app information, user reviews, search results, top charts, and market intelligence—all without requiring API keys.

## 🐛 Found a Bug? Help Us Improve!

**We value your feedback!** If you encounter any bugs, errors, or have suggestions for improvements, please [open an issue](https://github.com/Mohammedcha/gplay-scraper/issues). Contributors who report bugs or suggest features will be acknowledged in our [Contributors section](#-contributors) 🙏

## 🎯 What Can You Scrape?

**App Data (65+ Fields)**
- Basic info: title, developer, description, category, genre
- Ratings & reviews: score, ratings count, histogram, user reviews
- Install metrics: install count ranges, download statistics
- Pricing: free/paid status, price, in-app purchases, currency
- Media: icon, screenshots, video, header image URLs
- Technical: version, size, Android version, release date, last update
- Content: age rating, privacy policy, developer contact info
- Features: permissions, what's new, developer website

**Search & Discovery**
- Search apps by keyword with filtering and pagination
- Get search suggestions and autocomplete terms
- Find similar/competitor apps for any app
- Access top charts (free, paid, grossing) across 54 categories

**Developer Intelligence**
- Get complete app portfolio for any developer
- Track developer's app performance and ratings
- Analyze developer's market presence

**User Reviews**
- Extract reviews with ratings, text, and timestamps
- Get reviewer names and helpful vote counts
- Filter by newest, most relevant, or highest rated
- Track app versions mentioned in reviews

**Market Research**
- Multi-language support (100+ languages)
- Multi-region data (150+ countries)
- Localized pricing and availability
- Competitive analysis and benchmarking

## 🆕 **What's New in v1.0.6** 

**✅ Critical Bug Fixes:**
- **Reviews Pagination Fix** - Fixed critical issue when requesting more reviews than available
- **NoneType Error Resolution** - Resolved 'NoneType' object is not subscriptable error in reviews
- **Empty Response Handling** - Better handling of apps with limited reviews
- **Token Extraction Logic** - Improved pagination token handling for empty responses
- **Graceful Degradation** - Now returns available reviews instead of crashing

**✅ Enhanced Reliability:**
- **Safe Bounds Checking** - Added proper bounds checking for pagination tokens
- **Null Checking** - Enhanced null checking for empty data structures
- **Error Recovery** - Improved error handling in ReviewsScraper and ReviewsParser
- **Stability Improvements** - Better handling of edge cases in reviews extraction

**🙏 Acknowledgments:**
- Thanks to [@PhamDinhThienVu](https://github.com/PhamDinhThienVu) for reporting the reviews pagination bug

**✅ 7 Method Types:**
- **App Methods** - Extract 65+ data fields from any app (ratings, installs, pricing, permissions, etc.)
- **Search Methods** - Search Google Play Store apps with comprehensive filtering
- **Reviews Methods** - Extract user reviews with ratings, timestamps, and detailed feedback
- **Developer Methods** - Get all apps published by a specific developer
- **List Methods** - Access top charts (top free, top paid, top grossing) by category
- **Similar Methods** - Find similar/competitor apps for market research
- **Suggest Methods** - Get search suggestions and autocomplete for ASO

## ⚡ Key Features

**Powerful & Flexible**
- **7 HTTP clients with automatic fallback** - requests, curl_cffi, tls_client, httpx, urllib3, cloudscraper, aiohttp
- **42 functions across 7 method types** - analyze(), get_field(), get_fields(), print_field(), print_fields(), print_all()
- **No API keys required** - Direct scraping from Google Play Store
- **Multi-language & multi-region** - 100+ languages, 150+ countries

**Reliable & Safe**
- **Built-in rate limiting** - Prevents blocking with automatic delays
- **Automatic HTTP client fallback** - Ensures maximum reliability
- **Error handling** - Graceful failures with informative messages
- **Retry logic** - Automatic retries for failed requests

**Developer Friendly**
- **Simple API** - Intuitive method names and parameters
- **Comprehensive documentation** - Examples for every use case
- **Type hints** - Full IDE autocomplete support
- **Flexible output** - Get data as dict/list or print as JSON

## 📋 Requirements

- Python 3.7+
- requests (default HTTP client)
- Optional: curl-cffi, tls-client, httpx, urllib3, cloudscraper, aiohttp (for advanced HTTP clients)

## 🚀 Installation

```bash
# Install from PyPI
pip install gplay-scraper

# Or install in development mode
pip install -e .
```

## 📖 Quick Start

```python
from gplay_scraper import GPlayScraper

# Initialize with HTTP client (curl_cffi recommended for best performance)
scraper = GPlayScraper(http_client="curl_cffi")

# Get app details with different image sizes
app_id = "com.whatsapp"
scraper.app_print_all(app_id, lang="en", country="us", assets="LARGE")

# Get high-quality app data
data = scraper.app_analyze(app_id, assets="ORIGINAL")  # Maximum image quality
icon_small = scraper.app_get_field(app_id, "icon", assets="SMALL")  # 512px icon

# Print specific fields with custom image sizes
scraper.app_print_field(app_id, "icon", assets="LARGE")  # Print large icon URL
scraper.app_print_fields(app_id, ["icon", "screenshots"], assets="ORIGINAL")  # Print multiple fields

# Search for apps
scraper.search_print_all("social media", count=10, lang="en", country="us")

# Get reviews
scraper.reviews_print_all(app_id, count=50, sort="NEWEST", lang="en", country="us")

# Get developer apps
scraper.developer_print_all("5700313618786177705", count=20, lang="en", country="us")

# Get top charts
scraper.list_print_all("TOP_FREE", "GAME", count=20, lang="en", country="us")

# Get similar apps
scraper.similar_print_all(app_id, count=30, lang="en", country="us")

# Get search suggestions
scraper.suggest_print_all("fitness", count=5, lang="en", country="us")
```

## 🎯 7 Method Types

GPlay Scraper provides 7 method types with 42 functions to interact with Google Play Store data:

### 1. [App Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/APP_METHODS.md) - Extract app details (65+ fields)
### 2. [Search Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/SEARCH_METHODS.md) - Search for apps by keyword
### 3. [Reviews Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/REVIEWS_METHODS.md) - Get user reviews and ratings
### 4. [Developer Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/DEVELOPER_METHODS.md) - Get all apps from a developer
### 5. [List Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/LIST_METHODS.md) - Get top charts (free, paid, grossing)
### 6. [Similar Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/SIMILAR_METHODS.md) - Find similar/related apps
### 7. [Suggest Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/SUGGEST_METHODS.md) - Get search suggestions/autocomplete

Each method type has 6 functions:
- `analyze()` - Get all data as dictionary/list
- `get_field()` - Get single field value
- `get_fields()` - Get multiple fields
- `print_field()` - Print single field to console
- `print_fields()` - Print multiple fields to console
- `print_all()` - Print all data as JSON

## 🎯 Method Examples

### 1. [App Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/APP_METHODS.md) - Get App Details
Extract comprehensive information about any app including ratings, installs, pricing, and 65+ data fields.

📖 **[View detailed documentation →](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/APP_METHODS.md)**

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper(http_client="curl_cffi")

# Print all app data as JSON
scraper.app_print_all("com.whatsapp", lang="en", country="us")
```

**What you get:** Complete app profile with title, developer, ratings, install counts, pricing, screenshots, permissions, and more.

📄 **[View JSON example →](https://github.com/Mohammedcha/gplay-scraper/blob/main/output/app_example.json)**

---

### 2. [Search Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/SEARCH_METHODS.md) - Find Apps by Keyword
Search the Play Store by keyword, app name, or category to discover apps.

📖 **[View detailed documentation →](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/SEARCH_METHODS.md)**

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper(http_client="curl_cffi")

# Print all search results as JSON
scraper.search_print_all("fitness tracker", count=20, lang="en", country="us")
```

**What you get:** List of apps matching your search with titles, developers, ratings, prices, and Play Store URLs.

📄 **[View JSON example →](https://github.com/Mohammedcha/gplay-scraper/blob/main/output/search_example.json)**

---

### 3. [Reviews Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/REVIEWS_METHODS.md) - Extract User Reviews
Get user reviews with ratings, comments, timestamps, and helpful votes for sentiment analysis.

📖 **[View detailed documentation →](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/REVIEWS_METHODS.md)**

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper(http_client="curl_cffi")

# Print all reviews as JSON
scraper.reviews_print_all("com.whatsapp", count=100, sort="NEWEST", lang="en", country="us")
```

**What you get:** User reviews with names, ratings (1-5 stars), review text, timestamps, app versions, and helpful vote counts.

📄 **[View JSON example →](https://github.com/Mohammedcha/gplay-scraper/blob/main/output/reviews_example.json)**

---

### 4. [Developer Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/DEVELOPER_METHODS.md) - Get Developer's Apps
Retrieve all apps published by a specific developer using their developer ID.

📖 **[View detailed documentation →](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/DEVELOPER_METHODS.md)**

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper(http_client="curl_cffi")

# Print all developer apps as JSON
scraper.developer_print_all("5700313618786177705", count=50, lang="en", country="us")
```

**What you get:** Complete portfolio of apps from a developer with titles, ratings, prices, and descriptions.

📄 **[View JSON example →](https://github.com/Mohammedcha/gplay-scraper/blob/main/output/developer_example.json)**

---

### 5. [List Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/LIST_METHODS.md) - Get Top Charts
Access Play Store top charts including top free, top paid, and top grossing apps by category.

📖 **[View detailed documentation →](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/LIST_METHODS.md)**

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper(http_client="curl_cffi")

# Print top free games as JSON
scraper.list_print_all("TOP_FREE", "GAME", count=50, lang="en", country="us")
```

**What you get:** Top-ranked apps with titles, developers, ratings, install counts, prices, and screenshots.

📄 **[View JSON example →](https://github.com/Mohammedcha/gplay-scraper/blob/main/output/list_example.json)**

---

### 6. [Similar Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/SIMILAR_METHODS.md) - Find Related Apps
Discover apps similar to a reference app for competitive analysis and market research.

📖 **[View detailed documentation →](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/SIMILAR_METHODS.md)**

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper(http_client="curl_cffi")

# Print similar apps as JSON
scraper.similar_print_all("com.whatsapp", count=30, lang="en", country="us")
```

**What you get:** List of similar/competitor apps with titles, developers, ratings, and pricing information.

📄 **[View JSON example →](https://github.com/Mohammedcha/gplay-scraper/blob/main/output/similar_example.json)**

---

### 7. [Suggest Methods](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/SUGGEST_METHODS.md) - Get Search Suggestions
Get autocomplete suggestions and keyword ideas for ASO and market research.

📖 **[View detailed documentation →](https://github.com/Mohammedcha/gplay-scraper/blob/main/README/SUGGEST_METHODS.md)**

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper(http_client="curl_cffi")

# Print search suggestions as JSON
scraper.suggest_print_all("photo editor", count=10, lang="en", country="us")
```

**What you get:** List of popular search terms related to your keyword for ASO and keyword research.

📄 **[View JSON example →](https://github.com/Mohammedcha/gplay-scraper/blob/main/output/suggest_example.json)**

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Contributors

Special thanks to developers who helped improve this library:

- [@PhamDinhThienVu](https://github.com/PhamDinhThienVu) - Reported reviews pagination bug (v1.0.6)
- [@elmissouri16](https://github.com/elmissouri16) - Suggested multiple HTTP clients support (v1.0.3)

---

**Happy Analyzing! 🚀**