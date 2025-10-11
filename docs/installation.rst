Installation
============

Requirements
------------

- Python 3.7+
- curl-cffi
- beautifulsoup4 (optional, for enhanced parsing)

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
   
   scraper = GPlayScraper()
   title = scraper.get_field("com.hubolabs.hubo", "title")
   print(f"Success! Retrieved: {title}")

Troubleshooting
---------------

**Unicode Encoding Errors (Windows)**

If you encounter encoding errors on Windows:

.. code-block:: python

   import sys
   if sys.platform == "win32":
       sys.stdout.reconfigure(encoding='utf-8')

**Rate Limiting**

If requests fail, the library includes automatic rate limiting. You can customize it:

.. code-block:: python

   from gplay_scraper import GPlayScraper
   
   # Custom rate limiting (2 seconds between requests)
   scraper = GPlayScraper()
   scraper.scraper.rate_limit_delay = 2.0
