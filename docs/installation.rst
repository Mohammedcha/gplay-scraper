Installation
============

Requirements
------------

* Python 3.7 or higher
* pip package manager

Basic Installation
------------------

Install using pip:

.. code-block:: bash

   pip install gplay-scraper

This installs the library with the default HTTP client (requests).

Optional Dependencies
---------------------

For better performance and anti-bot protection, install additional HTTP clients:

.. code-block:: bash

   # Install all optional HTTP clients
   pip install httpx curl-cffi tls-client aiohttp cloudscraper

   # Or install individually as needed
   pip install httpx        # Modern HTTP/2 client
   pip install curl-cffi    # Best for bypassing blocks
   pip install tls-client   # Advanced TLS fingerprinting
   pip install aiohttp      # Async support
   pip install cloudscraper # Cloudflare bypass

Verify Installation
-------------------

Test your installation:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   app = scraper.app_analyze('com.whatsapp')
   print(f"Successfully installed! Got: {app['title']}")

Development Installation
------------------------

To install from source:

.. code-block:: bash

   git clone https://github.com/yourusername/gplay-scraper.git
   cd gplay-scraper
   pip install -e .

Upgrading
---------

To upgrade to the latest version:

.. code-block:: bash

   pip install --upgrade gplay-scraper

Troubleshooting
---------------

ImportError
^^^^^^^^^^^

If you get an ImportError, ensure the package is installed:

.. code-block:: bash

   pip show gplay-scraper

HTTP Client Issues
^^^^^^^^^^^^^^^^^^

If you encounter HTTP errors, try installing alternative clients:

.. code-block:: bash

   pip install curl-cffi

Then specify the client:

.. code-block:: python

   from gplay_scraper import GPlayScraper
   
   scraper = GPlayScraper(http_client='curl_cffi')

Next Steps
----------

* :doc:`quickstart` - Get started with basic usage
* :doc:`examples` - See practical examples
* :doc:`api/app` - Explore the API reference
