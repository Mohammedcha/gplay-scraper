Installation
============

Requirements
------------

- Python 3.7+
- requests (default HTTP client)
- Optional: curl-cffi, tls-client, httpx, urllib3, cloudscraper, aiohttp

Install from PyPI
-----------------

The easiest way to install GPlay Scraper is from PyPI:

.. code-block:: bash

   pip install gplay-scraper

Development Installation
------------------------

For development or to get the latest features:

.. code-block:: bash

   git clone https://github.com/mohammedcha/gplay-scraper.git
   cd gplay-scraper
   pip install -e .

Verify Installation
-------------------

Test your installation:

.. code-block:: python

   from gplay_scraper import GPlayScraper
   
   # Initialize scraper
   scraper = GPlayScraper()
   
   # Test with a simple app query
   data = scraper.app_analyze("com.whatsapp")
   print(f"Success! Retrieved: {data['title']}")
   
   # Or use print method
   scraper.app_print_all("com.whatsapp")

Troubleshooting
---------------

**Unicode Encoding Errors (Windows)**

If you encounter encoding errors on Windows:

.. code-block:: python

   import sys
   if sys.platform == "win32":
       sys.stdout.reconfigure(encoding='utf-8')

**HTTP Client Selection**

The library supports 7 HTTP clients with automatic fallback:

.. code-block:: python

   from gplay_scraper import GPlayScraper
   
   # Default: uses requests with automatic fallback
   scraper = GPlayScraper()
   
   # Specify HTTP client (requests, curl_cffi, tls_client, httpx, urllib3, cloudscraper, aiohttp)
   scraper = GPlayScraper(http_client="curl_cffi")
   scraper = GPlayScraper(http_client="tls_client")
   scraper = GPlayScraper(http_client="httpx")

**Common Parameters**

All methods support these parameters:

- ``lang`` - Language code (default: "en")
- ``country`` - Country code (default: "us")
- ``count`` - Number of results to return

.. code-block:: python

   # Get app data in Spanish for Spain
   scraper.app_print_all("com.whatsapp", lang="es", country="es")
   
   # Search with custom count
   scraper.search_print_all("games", count=50, lang="en", country="us")