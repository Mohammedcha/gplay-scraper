Quick Start Guide
=================

This guide will get you up and running with GPlay Scraper in minutes.

Basic Usage
-----------

Import and Initialize
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from gplay_scraper import GPlayScraper
   
   # Initialize with default HTTP client (requests)
   scraper = GPlayScraper()
   
   # Or specify HTTP client
   scraper = GPlayScraper(http_client="curl_cffi")
   # Options: requests, curl_cffi, tls_client, httpx, urllib3, cloudscraper, aiohttp

7 Method Types
--------------

GPlay Scraper provides 7 method types, each with 6 functions:

1. **App Methods** - Extract 65+ fields from any app
2. **Search Methods** - Search for apps by keyword
3. **Reviews Methods** - Get user reviews and ratings
4. **Developer Methods** - Get all apps from a developer
5. **List Methods** - Get top charts (free, paid, grossing)
6. **Similar Methods** - Find similar/competitor apps
7. **Suggest Methods** - Get search suggestions

Each method type has these functions:

- ``analyze()`` - Get all data as dictionary/list
- ``get_field()`` - Get single field value
- ``get_fields()`` - Get multiple fields
- ``print_field()`` - Print single field to console
- ``print_fields()`` - Print multiple fields to console
- ``print_all()`` - Print all data as JSON

Common Parameters
-----------------

All methods support these parameters:

- ``lang`` - Language code (default: "en")
- ``country`` - Country code (default: "us")
- ``count`` - Number of results to return

.. code-block:: python

   # English for United States (default)
   scraper.app_analyze("com.whatsapp", lang="en", country="us")
   
   # Spanish for Spain
   scraper.app_analyze("com.whatsapp", lang="es", country="es")
   
   # French for France
   scraper.app_analyze("com.whatsapp", lang="fr", country="fr")

1. App Methods
--------------

Extract 65+ fields from any app:

.. code-block:: python

   app_id = "com.whatsapp"
   
   # Get all app data
   data = scraper.app_analyze(app_id, lang="en", country="us")
   print(f"Title: {data['title']}")
   print(f"Rating: {data['score']}")
   
   # Get single field
   title = scraper.app_get_field(app_id, "title", lang="en", country="us")
   
   # Get multiple fields
   fields = scraper.app_get_fields(app_id, ["title", "score", "installs"])
   
   # Print methods
   scraper.app_print_all(app_id)

2. Search Methods
-----------------

Search for apps by keyword:

.. code-block:: python

   query = "social media"
   
   # Get all search results
   results = scraper.search_analyze(query, count=20, lang="en", country="us")
   for app in results:
       print(f"{app['title']} - {app['developer']}")
   
   # Get single field from all results
   titles = scraper.search_get_field(query, "title", count=10)
   
   # Get multiple fields
   data = scraper.search_get_fields(query, ["title", "score"], count=10)
   
   # Print methods
   scraper.search_print_all(query, count=10)

3. Reviews Methods
------------------

Get user reviews with ratings:

.. code-block:: python

   app_id = "com.whatsapp"
   
   # Get reviews (sort: NEWEST, RELEVANT, RATING)
   reviews = scraper.reviews_analyze(app_id, count=50, sort="NEWEST")
   for review in reviews:
       print(f"{review['userName']}: {review['score']} stars")
   
   # Get specific field from reviews
   scores = scraper.reviews_get_field(app_id, "score", count=100, sort="NEWEST")
   
   # Print methods
   scraper.reviews_print_all(app_id, count=50, sort="NEWEST")

4. Developer Methods
--------------------

Get all apps from a developer:

.. code-block:: python

   dev_id = "5700313618786177705"  # WhatsApp Inc.
   
   # Get all developer apps
   apps = scraper.developer_analyze(dev_id, count=20, lang="en", country="us")
   for app in apps:
       print(f"{app['title']} - {app['score']} stars")
   
   # Get specific fields
   titles = scraper.developer_get_field(dev_id, "title", count=20)
   
   # Print methods
   scraper.developer_print_all(dev_id, count=20)

5. List Methods
---------------

Get top charts:

.. code-block:: python

   # Collections: TOP_FREE, TOP_PAID, TOP_GROSSING
   # Categories: GAME, SOCIAL, COMMUNICATION, etc.
   
   # Get top free games
   apps = scraper.list_analyze("TOP_FREE", "GAME", count=50)
   for app in apps:
       print(f"{app['title']} - {app['installs']}")
   
   # Get top paid apps
   apps = scraper.list_analyze("TOP_PAID", "APPLICATION", count=20)
   
   # Print methods
   scraper.list_print_all("TOP_FREE", "GAME", count=20)

6. Similar Methods
------------------

Find similar/competitor apps:

.. code-block:: python

   app_id = "com.whatsapp"
   
   # Get similar apps
   similar = scraper.similar_analyze(app_id, count=20)
   for app in similar:
       print(f"{app['title']} - {app['developer']}")
   
   # Get specific fields
   titles = scraper.similar_get_field(app_id, "title", count=20)
   
   # Print methods
   scraper.similar_print_all(app_id, count=20)

7. Suggest Methods
------------------

Get search suggestions:

.. code-block:: python

   term = "fitness"
   
   # Get suggestions
   suggestions = scraper.suggest_analyze(term, count=10)
   print(suggestions)  # ['fitness tracker', 'fitness app', ...]
   
   # Get nested suggestions (suggestions for suggestions)
   nested = scraper.suggest_nested(term, count=5)
   
   # Print methods
   scraper.suggest_print_all(term, count=10)
   scraper.suggest_print_nested(term, count=5)

Method Parameters Reference
---------------------------

App Methods
~~~~~~~~~~~

- ``app_id`` - Google Play app ID
- ``field`` / ``fields`` - Field name(s) to retrieve
- ``lang`` - Language code (default: "en")
- ``country`` - Country code (default: "us")

Search Methods
~~~~~~~~~~~~~~

- ``query`` - Search query string
- ``field`` / ``fields`` - Field name(s) to retrieve
- ``count`` - Number of results (default: 20)
- ``lang`` - Language code (default: "en")
- ``country`` - Country code (default: "us")

Reviews Methods
~~~~~~~~~~~~~~~

- ``app_id`` - Google Play app ID
- ``field`` / ``fields`` - Field name(s) to retrieve
- ``count`` - Number of reviews (default: 100)
- ``sort`` - Sort order: "NEWEST", "RELEVANT", "RATING"
- ``lang`` - Language code (default: "en")
- ``country`` - Country code (default: "us")

Developer Methods
~~~~~~~~~~~~~~~~~

- ``dev_id`` - Developer ID (numeric or string)
- ``field`` / ``fields`` - Field name(s) to retrieve
- ``count`` - Number of apps (default: 50)
- ``lang`` - Language code (default: "en")
- ``country`` - Country code (default: "us")

List Methods
~~~~~~~~~~~~

- ``collection`` - "TOP_FREE", "TOP_PAID", "TOP_GROSSING"
- ``category`` - "GAME", "SOCIAL", "COMMUNICATION", etc.
- ``field`` / ``fields`` - Field name(s) to retrieve
- ``count`` - Number of apps (default: 50)
- ``lang`` - Language code (default: "en")
- ``country`` - Country code (default: "us")

Similar Methods
~~~~~~~~~~~~~~~

- ``app_id`` - Google Play app ID
- ``field`` / ``fields`` - Field name(s) to retrieve
- ``count`` - Number of similar apps (default: 50)
- ``lang`` - Language code (default: "en")
- ``country`` - Country code (default: "us")

Suggest Methods
~~~~~~~~~~~~~~~

- ``term`` - Search term for suggestions
- ``count`` - Number of suggestions (default: 5)
- ``lang`` - Language code (default: "en")
- ``country`` - Country code (default: "us")

Finding IDs
-----------

App Package Names
~~~~~~~~~~~~~~~~~

From Play Store URL:

.. code-block:: text

   URL: https://play.google.com/store/apps/details?id=com.whatsapp
   App ID: com.whatsapp

Developer IDs
~~~~~~~~~~~~~

From developer page URL:

.. code-block:: text

   URL: https://play.google.com/store/apps/dev?id=5700313618786177705
   Developer ID: 5700313618786177705

Next Steps
----------

- Check out :doc:`examples` for real-world use cases
- Read the :doc:`api_reference` for detailed method documentation
- Learn about :doc:`configuration` options
