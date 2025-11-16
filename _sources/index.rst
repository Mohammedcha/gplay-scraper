GPlay Scraper Documentation
============================

A comprehensive Python library for scraping Google Play Store data with 40 methods across 7 categories.

Features
--------

* **57 app fields** including install analytics
* **40 methods** for different data types
* **7 HTTP clients** with automatic fallback
* **Multi-language** and **multi-region** support
* **Automatic retries** and error handling
* **Rate limiting** built-in

Quick Example
-------------

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   
   # Get complete app data (57 fields)
   app = scraper.app_analyze('com.whatsapp')
   print(app['title'])              # WhatsApp Messenger
   print(app['realInstalls'])       # 10931553905
   print(app['dailyInstalls'])      # 1815870
   print(app['publisherCountry'])   # United States

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation
   quickstart
   examples

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/app
   api/search
   api/reviews
   api/developer
   api/similar
   api/list
   api/suggest

.. toctree::
   :maxdepth: 2
   :caption: Advanced

   configuration
   error_handling
   fields

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
