# Changelog

All notable changes to this project will be documented in this file.

## [1.0.3] - 2025-10-11

### Added
- Optional proxy configuration for both single-proxy and per-scheme setups via `GPlayScraper` and `Config`

## [1.0.2] - 2025-10-11

### Changed
- Swapped the HTTP layer to `curl-cffi` with Play Store browser impersonation enabled by default
- Centralized networking defaults (headers, timeout, impersonation) through `Config.get_request_config`
- Updated documentation and tests to reflect the new HTTP client

## [1.0.1] - 2025-10-07

### Added
- **Paid App Support**: Fixed JSON parsing issues for paid apps with malformed data structures
- **Reviews Extraction**: Successfully extracts user reviews for both free and paid apps
- **Organized Output**: Restructured JSON output with logical field grouping:
  - Basic Information
  - Category & Genre
  - Release & Updates
  - Media Content
  - Install Statistics
  - Ratings & Reviews
  - Advertising
  - Technical Details
  - Content Rating
  - Privacy & Security
  - Pricing & Monetization
  - Developer Information
  - ASO Analysis
- **Enhanced JSON Parser**: Bracket-matching algorithm for complex nested structures
- **Original Price Field**: Added `originalPrice` field for sale price tracking

### Fixed
- **JSON Parsing Errors**: Resolved "Expecting ',' delimiter" errors for paid apps
- **Reviews Data**: Fixed empty reviews arrays by implementing alternative parsing methods
- **Malformed Data Handling**: Improved handling of unquoted keys and malformed JSON from Play Store

### Improved
- **Error Handling**: Better fallback mechanisms for JSON parsing failures
- **Data Extraction**: More robust extraction for apps with complex pricing structures
- **Code Organization**: Cleaner separation of parsing logic and error recovery

## [1.0.0] - 2025-10-06

### Added
- Initial release of GPlay Scraper
- Complete Google Play Store app data extraction
- ASO (App Store Optimization) analysis
- Modular architecture with separate core modules
- Support for 60+ data fields including:
  - Basic app information
  - Install statistics and metrics
  - Ratings and reviews data
  - Technical specifications
  - Developer information
  - Media content (screenshots, videos, icons)
  - Pricing and monetization details
  - ASO keyword analysis
- Multiple access methods:
  - `analyze()` - Complete app analysis
  - `get_field()` - Single field retrieval
  - `get_fields()` - Multiple field retrieval
  - `print_field()` - Direct field printing
  - `print_fields()` - Multiple field printing
  - `print_all()` - Complete data printing
- Comprehensive documentation and examples
- Error handling and logging
- Rate limiting considerations
- Cross-platform compatibility

### Features
- Web scraping of Google Play Store pages
- JSON data extraction and parsing
- Automatic install metrics calculation
- Keyword frequency analysis
- Readability scoring
- Review data extraction
- Image URL processing
- Date parsing and age calculation
