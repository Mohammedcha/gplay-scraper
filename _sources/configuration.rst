Configuration
=============

Advanced configuration options for GPlay Scraper.

HTTP Client Selection
---------------------

Choose from 7 HTTP clients with automatic fallback.

.. code-block:: python

   from gplay_scraper import GPlayScraper

   # Default (requests)
   scraper = GPlayScraper()
   
   # Use curl_cffi (best for bypassing blocks)
   scraper = GPlayScraper(http_client='curl_cffi')
   
   # Use tls_client (advanced TLS fingerprinting)
   scraper = GPlayScraper(http_client='tls_client')
   
   # Use httpx (modern HTTP/2)
   scraper = GPlayScraper(http_client='httpx')

Available HTTP Clients
^^^^^^^^^^^^^^^^^^^^^^

1. **requests** - Default, most compatible
2. **curl_cffi** - Best for anti-bot bypass (Chrome 110 impersonation)
3. **tls_client** - Advanced TLS fingerprinting (Chrome 112)
4. **urllib3** - Low-level HTTP with connection pooling
5. **cloudscraper** - Cloudflare bypass
6. **aiohttp** - Async HTTP support
7. **httpx** - Modern HTTP/2 client

The library automatically falls back to the next available client if one fails.

Rate Limiting
-------------

Configure delay between requests to avoid rate limits.

.. code-block:: python

   from gplay_scraper import Config
   
   # Set rate limit delay (seconds)
   Config.RATE_LIMIT_DELAY = 2.0  # 2 seconds between requests
   
   # Or use default (1.0 second)
   Config.RATE_LIMIT_DELAY = 1.0

Language & Region
-----------------

Set default language and country for all requests.

.. code-block:: python

   from gplay_scraper import Config
   
   # Set default language
   Config.DEFAULT_LANGUAGE = 'es'  # Spanish
   
   # Set default country
   Config.DEFAULT_COUNTRY = 'mx'  # Mexico

Common Language Codes
^^^^^^^^^^^^^^^^^^^^^^

* ``en`` - English
* ``es`` - Spanish  
* ``fr`` - French
* ``de`` - German
* ``it`` - Italian
* ``pt`` - Portuguese
* ``ja`` - Japanese
* ``ko`` - Korean
* ``zh`` - Chinese
* ``ru`` - Russian
* ``ar`` - Arabic
* ``hi`` - Hindi

Common Country Codes
^^^^^^^^^^^^^^^^^^^^^

* ``us`` - United States
* ``gb`` - United Kingdom
* ``ca`` - Canada
* ``de`` - Germany
* ``fr`` - France
* ``es`` - Spain
* ``mx`` - Mexico
* ``jp`` - Japan
* ``kr`` - South Korea
* ``cn`` - China
* ``in`` - India
* ``br`` - Brazil

Request Timeout
---------------

Configure HTTP request timeout.

.. code-block:: python

   from gplay_scraper import Config
   
   # Set timeout (seconds)
   Config.DEFAULT_TIMEOUT = 30  # 30 seconds
   
   # Or use default (10 seconds)
   Config.DEFAULT_TIMEOUT = 10

Retry Configuration
-------------------

Configure automatic retry behavior.

.. code-block:: python

   from gplay_scraper import Config
   
   # Set number of retries
   Config.DEFAULT_RETRY_COUNT = 5  # Try 5 times
   
   # Or use default (3 retries)
   Config.DEFAULT_RETRY_COUNT = 3

Image Asset Sizes
-----------------

Configure default image size for all requests.

.. code-block:: python

   scraper = GPlayScraper()
   
   # Small images (512px)
   app = scraper.app_analyze('com.whatsapp', assets='SMALL')
   
   # Medium images (1024px) - default
   app = scraper.app_analyze('com.whatsapp', assets='MEDIUM')
   
   # Large images (2048px)
   app = scraper.app_analyze('com.whatsapp', assets='LARGE')
   
   # Original size (maximum)
   app = scraper.app_analyze('com.whatsapp', assets='ORIGINAL')

Per-Request Configuration
--------------------------

Override defaults for specific requests.

.. code-block:: python

   scraper = GPlayScraper()
   
   # Per-request language
   app_es = scraper.app_analyze('com.whatsapp', lang='es')
   app_fr = scraper.app_analyze('com.whatsapp', lang='fr')
   
   # Per-request country
   app_uk = scraper.app_analyze('com.whatsapp', country='gb')
   app_de = scraper.app_analyze('com.whatsapp', country='de')
   
   # Per-request images
   app_large = scraper.app_analyze('com.whatsapp', assets='LARGE')

Logging
-------

Configure logging level for debugging.

.. code-block:: python

   import logging
   
   # Enable debug logging
   logging.basicConfig(level=logging.DEBUG)
   
   # Enable info logging
   logging.basicConfig(level=logging.INFO)
   
   # Disable logging
   logging.basicConfig(level=logging.ERROR)

Complete Configuration Example
-------------------------------

.. code-block:: python

   from gplay_scraper import GPlayScraper, Config
   import logging
   
   # Configure library
   Config.RATE_LIMIT_DELAY = 2.0
   Config.DEFAULT_LANGUAGE = 'en'
   Config.DEFAULT_COUNTRY = 'us'
   Config.DEFAULT_TIMEOUT = 30
   Config.DEFAULT_RETRY_COUNT = 5
   
   # Configure logging
   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(levelname)s - %(message)s'
   )
   
   # Initialize with preferred HTTP client
   scraper = GPlayScraper(http_client='curl_cffi')
   
   # Use the scraper
   app = scraper.app_analyze('com.whatsapp')

Environment Variables
---------------------

You can also use environment variables for configuration.

.. code-block:: bash

   # Set in your shell or .env file
   export GPLAY_HTTP_CLIENT=curl_cffi
   export GPLAY_RATE_LIMIT=2.0
   export GPLAY_LANGUAGE=en
   export GPLAY_COUNTRY=us

Best Practices
--------------

1. **Use curl_cffi or tls_client** for better success rates
2. **Set rate limiting** to 2+ seconds for large batch operations
3. **Use field filtering** to reduce data transfer and parsing time
4. **Enable logging** during development, disable in production
5. **Handle exceptions** gracefully for production use
6. **Reuse scraper instance** instead of creating new ones

See Also
--------

* :doc:`error_handling` - Error handling guide
* :doc:`examples` - Practical examples
