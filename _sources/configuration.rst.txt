Configuration
=============

GPlay Scraper provides flexible configuration options to customize behavior.

Default Settings
----------------

The library comes with sensible defaults:

.. code-block:: python

   from gplay_scraper import Config

   print(f"Timeout: {Config.DEFAULT_TIMEOUT}s")           # 30 seconds
   print(f"Rate limit: {Config.RATE_LIMIT_DELAY}s")       # 1.0 seconds
   print(f"ASO keywords: {Config.ASO_TOP_KEYWORDS}")      # 20
   print(f"Min word length: {Config.ASO_MIN_WORD_LENGTH}") # 3

Network Configuration
---------------------

Timeout Settings
~~~~~~~~~~~~~~~~

Control request timeout:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   
   # Access current timeout
   print(f"Current timeout: {scraper.scraper.timeout}s")
   
   # Modify timeout (affects all future requests)
   scraper.scraper.timeout = 45  # 45 seconds

Rate Limiting
~~~~~~~~~~~~~

Configure delays between requests:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   # Default rate limiting (1 second)
   scraper = GPlayScraper()
   
   # Custom rate limiting
   scraper = GPlayScraper()
   scraper.scraper.rate_limit_delay = 2.0  # 2 seconds between requests
   
   # Disable rate limiting (not recommended)
   scraper.scraper.rate_limit_delay = 0

User Agent
~~~~~~~~~~

Customize the user agent string:

.. code-block:: python

   from gplay_scraper import Config

   # Get default headers
   headers = Config.get_headers()
   print(headers['User-Agent'])
   
   # Custom user agent
   custom_headers = Config.get_headers("MyApp/1.0")
   print(custom_headers['User-Agent'])

ASO Configuration
-----------------

Keyword Analysis
~~~~~~~~~~~~~~~~

Configure ASO analysis parameters:

.. code-block:: python

   from gplay_scraper import GPlayScraper, Config

   scraper = GPlayScraper()
   
   # Use default settings (20 top keywords)
   data = scraper.analyze("com.hubolabs.hubo")
   
   # Custom keyword count
   # Note: This requires modifying the analyzer directly
   scraper.aso_analyzer.analyze_app_text(
       app_data, 
       top_n=50  # Get top 50 keywords instead of 20
   )

Stop Words
~~~~~~~~~~

Customize stop words for keyword analysis:

.. code-block:: python

   from gplay_scraper.core.aso_analyzer import AsoAnalyzer

   analyzer = AsoAnalyzer()
   
   # View default stop words
   print(f"Stop words count: {len(analyzer.default_stop_words)}")
   
   # Add custom stop words
   custom_stop_words = analyzer.default_stop_words.copy()
   custom_stop_words.update(['custom', 'words', 'to', 'exclude'])
   
   # Use custom stop words
   tokens = analyzer.tokenize_text("Your text here", stop_words=custom_stop_words)

Caching Configuration
---------------------

The library includes built-in caching for performance:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   
   # First call - fetches from Play Store
   data1 = scraper.analyze("com.hubolabs.hubo")
   
   # Second call - uses cached data (much faster)
   data2 = scraper.analyze("com.hubolabs.hubo")
   
   # Clear cache if needed
   scraper._cache.clear()

Environment Variables
---------------------

You can use environment variables for configuration:

.. code-block:: python

   import os
   from gplay_scraper import GPlayScraper

   # Set environment variables
   os.environ['GPLAY_TIMEOUT'] = '45'
   os.environ['GPLAY_RATE_LIMIT'] = '2.0'
   
   # Use in your application
   timeout = int(os.environ.get('GPLAY_TIMEOUT', 30))
   rate_limit = float(os.environ.get('GPLAY_RATE_LIMIT', 1.0))
   
   scraper = GPlayScraper()
   scraper.scraper.timeout = timeout
   scraper.scraper.rate_limit_delay = rate_limit

Advanced Configuration
----------------------

Custom Request Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For advanced users who need full control:

.. code-block:: python

   from gplay_scraper import Config
   import requests

   # Get request configuration
   config = Config.get_request_config()
   
   # Modify configuration
   config['timeout'] = 60
   config['headers']['Accept-Language'] = 'en-US,en;q=0.9'
   
   # Use with requests directly (advanced usage)
   response = requests.get('https://example.com', **config)

Logging Configuration
~~~~~~~~~~~~~~~~~~~~~

Configure logging for debugging:

.. code-block:: python

   import logging
   from gplay_scraper import GPlayScraper

   # Enable debug logging
   logging.basicConfig(level=logging.DEBUG)
   logger = logging.getLogger('gplay_scraper')
   
   # Now you'll see detailed logs
   scraper = GPlayScraper()
   data = scraper.analyze("com.hubolabs.hubo")

Error Handling
--------------

Handle errors gracefully:

.. code-block:: python

   from gplay_scraper import GPlayScraper, AppNotFoundError, NetworkError

   scraper = GPlayScraper()

   try:
       data = scraper.app_analyze("com.whatsapp")
   except AppNotFoundError:
       print("App not found")
   except NetworkError:
       print("Network error occurred")
   except Exception as e:
       print(f"Unexpected error: {e}")

When to Use Each Method
-----------------------

App Methods
~~~~~~~~~~~

- ``app_analyze()`` - Need all data for comprehensive analysis
- ``app_get_field()`` - Need just one specific value
- ``app_get_fields()`` - Need several specific fields (more efficient)
- ``app_print_field()`` - Quick debugging/console output
- ``app_print_fields()`` - Quick debugging of multiple values
- ``app_print_all()`` - Explore available data structure

Search Methods
~~~~~~~~~~~~~~

- ``search_analyze()`` - Need complete data for all search results
- ``search_get_field()`` - Need just one field from all results
- ``search_get_fields()`` - Need specific fields from all results
- ``search_print_all()`` - Explore available data structure

Reviews Methods
~~~~~~~~~~~~~~~

- ``reviews_analyze()`` - Need complete review data for analysis
- ``reviews_get_field()`` - Need just one field (e.g., all scores)
- ``reviews_get_fields()`` - Need specific fields (more efficient)
- ``reviews_print_all()`` - Explore available data structure

Developer Methods
~~~~~~~~~~~~~~~~~

- ``developer_analyze()`` - Need complete data for all apps
- ``developer_get_field()`` - Need just one field from all apps
- ``developer_get_fields()`` - Need specific fields from all apps
- ``developer_print_all()`` - Explore available data structure

List Methods
~~~~~~~~~~~~

- ``list_analyze()`` - Need complete data for all chart apps
- ``list_get_field()`` - Need just one field from all apps
- ``list_get_fields()`` - Need specific fields from all apps
- ``list_print_all()`` - Explore available data structure

Similar Methods
~~~~~~~~~~~~~~~

- ``similar_analyze()`` - Need complete data for similar apps
- ``similar_get_field()`` - Need just one field from all apps
- ``similar_get_fields()`` - Need specific fields from all apps
- ``similar_print_all()`` - Explore available data structure

Suggest Methods
~~~~~~~~~~~~~~~

- ``suggest_analyze()`` - Need list of suggestions
- ``suggest_nested()`` - Need suggestions for suggestions
- ``suggest_print_all()`` - Quick console output
- ``suggest_print_nested()`` - Quick nested output

Best Practices
--------------

**Rate Limiting**
  Always use appropriate rate limiting to avoid being blocked. The default 1-second delay is recommended.

**Error Handling**
  Always wrap scraper calls in try-catch blocks for production use.

**HTTP Client Selection**
  Start with default (requests), install 2-3 backup clients for reliability.

**Method Selection**
  Use get_fields() instead of multiple get_field() calls for better performance.

**Timeouts**
  Adjust timeouts based on your network conditions and requirements.

**Logging**
  Enable logging in development to understand what's happening under the hood.

**Multi-Region**
  Use lang and country parameters to get localized data for different markets.