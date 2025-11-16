Error Handling
==============

Guide to handling errors and exceptions in GPlay Scraper.

Exception Types
---------------

GPlay Scraper provides 6 custom exception types:

AppNotFoundError
^^^^^^^^^^^^^^^^

Raised when an app, developer, or resource is not found.

.. code-block:: python

   from gplay_scraper import GPlayScraper
   from gplay_scraper.exceptions import AppNotFoundError

   scraper = GPlayScraper()
   
   try:
       app = scraper.app_analyze('invalid.app.id')
   except AppNotFoundError as e:
       print(f"App not found: {e}")

NetworkError
^^^^^^^^^^^^

Raised when network or HTTP errors occur.

.. code-block:: python

   from gplay_scraper.exceptions import NetworkError

   try:
       app = scraper.app_analyze('com.whatsapp')
   except NetworkError as e:
       print(f"Network error: {e}")

DataParsingError
^^^^^^^^^^^^^^^^

Raised when JSON parsing or data extraction fails.

.. code-block:: python

   from gplay_scraper.exceptions import DataParsingError

   try:
       app = scraper.app_analyze('com.whatsapp')
   except DataParsingError as e:
       print(f"Parsing error: {e}")

RateLimitError
^^^^^^^^^^^^^^

Raised when rate limits are exceeded.

.. code-block:: python

   from gplay_scraper.exceptions import RateLimitError

   try:
       # Making too many requests too quickly
       for i in range(1000):
           app = scraper.app_analyze(f'com.app{i}')
   except RateLimitError as e:
       print(f"Rate limited: {e}")

InvalidAppIdError
^^^^^^^^^^^^^^^^^

Raised when input validation fails.

.. code-block:: python

   from gplay_scraper.exceptions import InvalidAppIdError

   try:
       app = scraper.app_analyze('')  # Empty app ID
   except InvalidAppIdError as e:
       print(f"Invalid input: {e}")

GPlayScraperError
^^^^^^^^^^^^^^^^^

Base exception for all library errors.

.. code-block:: python

   from gplay_scraper.exceptions import GPlayScraperError

   try:
       app = scraper.app_analyze('com.whatsapp')
   except GPlayScraperError as e:
       print(f"Library error: {e}")

Comprehensive Error Handling
-----------------------------

Handle all common exceptions.

.. code-block:: python

   from gplay_scraper import GPlayScraper
   from gplay_scraper.exceptions import (
       AppNotFoundError,
       NetworkError,
       DataParsingError,
       RateLimitError,
       InvalidAppIdError,
       GPlayScraperError
   )

   scraper = GPlayScraper()

   try:
       app = scraper.app_analyze('com.whatsapp')
   except InvalidAppIdError as e:
       print(f"Invalid app ID: {e}")
   except AppNotFoundError as e:
       print(f"App not found: {e}")
   except NetworkError as e:
       print(f"Network error: {e}")
   except DataParsingError as e:
       print(f"Parsing error: {e}")
   except RateLimitError as e:
       print(f"Rate limited: {e}")
   except GPlayScraperError as e:
       print(f"Unknown library error: {e}")

Automatic Retries
-----------------

The library automatically retries failed requests with HTTP client fallback.

.. code-block:: python

   from gplay_scraper import Config
   
   # Configure retries
   Config.DEFAULT_RETRY_COUNT = 5  # Try 5 times
   
   scraper = GPlayScraper()
   app = scraper.app_analyze('com.whatsapp')
   # Automatically retries up to 5 times if it fails
   # Switches HTTP clients between retries

Graceful Degradation
--------------------

Methods return None or empty lists on failure instead of crashing.

.. code-block:: python

   scraper = GPlayScraper()
   
   # Returns None if app not found (after retries)
   app = scraper.app_analyze('invalid.app')
   if app is None:
       print("App not found")
   
   # Returns empty list if search fails
   results = scraper.search_analyze('invalid query')
   if not results:
       print("No results found")

Production Error Handling
--------------------------

Example for production use.

.. code-block:: python

   import logging
   from gplay_scraper import GPlayScraper, Config
   from gplay_scraper.exceptions import GPlayScraperError

   # Configure logging
   logging.basicConfig(
       level=logging.ERROR,
       format='%(asctime)s - %(levelname)s - %(message)s',
       filename='gplay_scraper.log'
   )

   logger = logging.getLogger(__name__)

   # Configure retries
   Config.DEFAULT_RETRY_COUNT = 5

   scraper = GPlayScraper(http_client='curl_cffi')

   def safe_analyze_app(app_id):
       """Safely analyze an app with error handling."""
       try:
           return scraper.app_analyze(app_id)
       except GPlayScraperError as e:
           logger.error(f"Failed to analyze {app_id}: {e}")
           return None

   # Use in production
   app_ids = ['com.app1', 'com.app2', 'com.app3']
   results = []
   
   for app_id in app_ids:
       app = safe_analyze_app(app_id)
       if app:
           results.append(app)
   
   print(f"Successfully analyzed {len(results)}/{len(app_ids)} apps")

Batch Processing with Error Handling
-------------------------------------

.. code-block:: python

   from gplay_scraper import GPlayScraper
   from gplay_scraper.exceptions import GPlayScraperError

   scraper = GPlayScraper()
   
   app_ids = ['com.app1', 'com.app2', 'invalid.app', 'com.app3']
   
   successful = []
   failed = []
   
   for app_id in app_ids:
       try:
           app = scraper.app_analyze(app_id)
           if app:
               successful.append(app)
       except GPlayScraperError as e:
           failed.append((app_id, str(e)))
   
   print(f"Successful: {len(successful)}")
   print(f"Failed: {len(failed)}")
   
   if failed:
       print("\nFailed apps:")
       for app_id, error in failed:
           print(f"  {app_id}: {error}")

Best Practices
--------------

1. **Always handle exceptions** in production code
2. **Use specific exceptions** when possible instead of catching all
3. **Log errors** for debugging and monitoring
4. **Implement retries** for transient failures
5. **Use graceful degradation** - continue processing even if some items fail
6. **Monitor error rates** to detect issues early

See Also
--------

* :doc:`configuration` - Configuration options
* :doc:`examples` - More practical examples
