HTTP Clients
============

GPlay Scraper supports 7 HTTP clients with automatic fallback. If one client fails, it automatically tries the next available client.

Supported Clients
-----------------

1. **requests** (default)
   - Standard Python HTTP library
   - Most widely used and stable
   - Recommended for most use cases

2. **curl_cffi**
   - cURL with browser impersonation
   - Better for bypassing detection
   - Mimics real browser behavior

3. **tls_client**
   - Advanced TLS fingerprinting
   - Excellent for anti-bot protection
   - Custom TLS configurations

4. **httpx**
   - Modern async-capable HTTP client
   - HTTP/2 support
   - Clean API design

5. **urllib3**
   - Low-level HTTP client
   - Connection pooling
   - Retry mechanisms

6. **cloudscraper**
   - Cloudflare bypass capabilities
   - Automatic challenge solving
   - Good for protected sites

7. **aiohttp**
   - Async HTTP client
   - High performance
   - Concurrent requests

Usage
-----

Default Client
~~~~~~~~~~~~~~

.. code-block:: python

   from gplay_scraper import GPlayScraper
   
   # Uses requests by default with automatic fallback
   scraper = GPlayScraper()

Specify Client
~~~~~~~~~~~~~~

.. code-block:: python

   # Use curl_cffi
   scraper = GPlayScraper(http_client="curl_cffi")
   
   # Use tls_client
   scraper = GPlayScraper(http_client="tls_client")
   
   # Use httpx
   scraper = GPlayScraper(http_client="httpx")

Installation
------------

Default Installation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install gplay-scraper

This installs with requests (default client).

Optional Clients
~~~~~~~~~~~~~~~~

Install additional clients as needed:

.. code-block:: bash

   # curl_cffi
   pip install curl-cffi
   
   # tls_client
   pip install tls-client
   
   # httpx
   pip install httpx
   
   # urllib3
   pip install urllib3
   
   # cloudscraper
   pip install cloudscraper
   
   # aiohttp
   pip install aiohttp

Automatic Fallback
------------------

The library automatically tries clients in this order:

1. Your specified client (or requests if none specified)
2. curl_cffi
3. tls_client
4. urllib3
5. cloudscraper
6. aiohttp
7. httpx

Example:

.. code-block:: python

   # If curl_cffi fails, automatically tries tls_client, then others
   scraper = GPlayScraper(http_client="curl_cffi")
   data = scraper.app_analyze("com.whatsapp")

When to Use Each Client
-----------------------

**requests**
  - Default choice for most use cases
  - Stable and well-tested
  - Good documentation

**curl_cffi**
  - When you need browser impersonation
  - Bypassing basic detection
  - More realistic requests

**tls_client**
  - Advanced anti-bot protection
  - Custom TLS fingerprints
  - Maximum stealth

**httpx**
  - Modern Python projects
  - HTTP/2 support needed
  - Clean async/await code

**urllib3**
  - Low-level control needed
  - Custom connection pooling
  - Advanced retry logic

**cloudscraper**
  - Cloudflare-protected sites
  - Automatic challenge solving
  - DDoS protection bypass

**aiohttp**
  - High-performance async
  - Concurrent requests
  - WebSocket support

Error Handling
--------------

.. code-block:: python

   from gplay_scraper import GPlayScraper, NetworkError
   
   scraper = GPlayScraper(http_client="curl_cffi")
   
   try:
       data = scraper.app_analyze("com.whatsapp")
   except NetworkError as e:
       print(f"All HTTP clients failed: {e}")

Best Practices
--------------

1. **Start with default** - Use requests unless you have specific needs
2. **Install backups** - Install 2-3 clients for better reliability
3. **Test your client** - Verify your chosen client works for your use case
4. **Monitor failures** - Log which clients fail to optimize your setup
5. **Update regularly** - Keep HTTP clients updated for best compatibility
