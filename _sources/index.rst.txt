GPlay Scraper Documentation
===========================

**GPlay Scraper** is a powerful Python library for extracting comprehensive app data from the Google Play Store. Get ratings, install counts, reviews, developer information, and 65+ data fields with 7 method types and 42 functions.

.. image:: https://img.shields.io/pypi/v/gplay-scraper.svg
   :target: https://pypi.org/project/gplay-scraper/
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/gplay-scraper.svg
   :target: https://pypi.org/project/gplay-scraper/
   :alt: Python Versions

.. image:: https://img.shields.io/github/license/mohammedcha/gplay-scraper.svg
   :target: https://github.com/mohammedcha/gplay-scraper/blob/main/LICENSE
   :alt: License

Key Features
------------

✅ **7 Method Types** - App, Search, Reviews, Developer, List, Similar, Suggest

✅ **42 Functions** - analyze(), get_field(), get_fields(), print_field(), print_fields(), print_all()

✅ **65+ Data Fields** - Complete app information extraction

✅ **7 HTTP Clients** - requests, curl_cffi, tls_client, httpx, urllib3, cloudscraper, aiohttp

✅ **Multi-language Support** - Get localized data for different countries and languages

✅ **No API Keys Required** - Direct scraping from Google Play Store

Quick Start
-----------

.. code-block:: python

   from gplay_scraper import GPlayScraper

   # Initialize scraper (optional: specify HTTP client)
   scraper = GPlayScraper(http_client="requests")  # or curl_cffi, tls_client, etc.

   # App Methods - Extract 65+ fields from any app
   scraper.app_print_all("com.whatsapp", lang="en", country="us")
   
   # Search Methods - Search for apps by keyword
   scraper.search_print_all("social media", count=10, lang="en", country="us")
   
   # Reviews Methods - Get user reviews with ratings
   scraper.reviews_print_all("com.whatsapp", count=50, sort="NEWEST", lang="en", country="us")
   
   # Developer Methods - Get all apps from a developer
   scraper.developer_print_all("5700313618786177705", count=20, lang="en", country="us")
   
   # List Methods - Get top charts (TOP_FREE, TOP_PAID, TOP_GROSSING)
   scraper.list_print_all("TOP_FREE", "GAME", count=20, lang="en", country="us")
   
   # Similar Methods - Find similar/competitor apps
   scraper.similar_print_all("com.whatsapp", count=20, lang="en", country="us")
   
   # Suggest Methods - Get search suggestions/autocomplete
   scraper.suggest_print_all("fitness", count=5, lang="en", country="us")

Installation
------------

.. code-block:: bash

   pip install gplay-scraper

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart
   http_clients
   fields_reference
   examples
   configuration

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   gplay_scraper

.. toctree::
   :maxdepth: 1
   :caption: Additional Information

   changelog
   contributing
   license

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`