Quick Start Guide
=================

This guide will get you started with GPlay Scraper in 5 minutes.

Basic Usage
-----------

Initialize the Scraper
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from gplay_scraper import GPlayScraper

   # Initialize once
   scraper = GPlayScraper()

Get App Data
^^^^^^^^^^^^

Extract complete app information with 57 fields:

.. code-block:: python

   # Get all app data
   app = scraper.app_analyze('com.whatsapp')
   
   # Access the data
   print(app['title'])              # App name
   print(app['developer'])          # Developer name
   print(app['score'])              # Rating (0-5)
   print(app['realInstalls'])       # Exact install count
   print(app['dailyInstalls'])      # Average daily installs
   print(app['publisherCountry'])   # Publisher country

Get Specific Fields
^^^^^^^^^^^^^^^^^^^

If you only need certain fields:

.. code-block:: python

   # Get single field
   title = scraper.app_get_field('com.whatsapp', 'title')
   
   # Get multiple fields
   fields = scraper.app_get_fields('com.whatsapp', 
       ['title', 'score', 'dailyInstalls'])

Search for Apps
^^^^^^^^^^^^^^^

Search the Play Store by keyword:

.. code-block:: python

   # Search for apps
   results = scraper.search_analyze('messaging', count=10)
   
   # Iterate through results
   for app in results:
       print(f"{app['title']} by {app['developer']}")
       print(f"  Rating: {app['score']}/5")
       print(f"  Free: {app['free']}")

Get Reviews
^^^^^^^^^^^

Extract user reviews with ratings:

.. code-block:: python

   # Get newest reviews
   reviews = scraper.reviews_analyze('com.whatsapp', 
       count=50, 
       sort='NEWEST')
   
   # Process reviews
   for review in reviews:
       print(f"{review['userName']}: {review['score']}/5")
       print(f"  {review['content'][:100]}...")

Get Developer Apps
^^^^^^^^^^^^^^^^^^

Find all apps from a developer:

.. code-block:: python

   # Get all apps from Google
   apps = scraper.developer_analyze('Google LLC')
   
   for app in apps:
       print(f"{app['title']} - {app['score']}/5")

Find Similar Apps
^^^^^^^^^^^^^^^^^

Discover competitor or similar apps:

.. code-block:: python

   # Find apps similar to WhatsApp
   similar = scraper.similar_analyze('com.whatsapp', count=20)
   
   for app in similar:
       print(f"{app['title']} - {app['score']}/5")

Get Top Charts
^^^^^^^^^^^^^^

Access top free, paid, or grossing apps:

.. code-block:: python

   # Top free games
   top_free = scraper.list_analyze('TOP_FREE', 
       category='GAME', 
       count=100)
   
   # Top paid apps
   top_paid = scraper.list_analyze('TOP_PAID', 
       category='APPLICATION', 
       count=50)
   
   # Top grossing
   top_grossing = scraper.list_analyze('TOP_GROSSING', count=100)

Get Search Suggestions
^^^^^^^^^^^^^^^^^^^^^^

Get autocomplete suggestions:

.. code-block:: python

   # Get suggestions
   suggestions = scraper.suggest_analyze('mine', count=10)
   print(suggestions)
   # ['minecraft', 'minesweeper', 'mineplex', ...]

Multi-Language Support
----------------------

Get data in different languages:

.. code-block:: python

   # Spanish
   app = scraper.app_analyze('com.whatsapp', lang='es')
   
   # French
   app = scraper.app_analyze('com.whatsapp', lang='fr')
   
   # Japanese
   app = scraper.app_analyze('com.whatsapp', lang='ja')

Regional Data
-------------

Get region-specific data:

.. code-block:: python

   # UK data
   app = scraper.app_analyze('com.whatsapp', country='gb')
   
   # Germany
   app = scraper.app_analyze('com.whatsapp', country='de')
   
   # Japan
   app = scraper.app_analyze('com.whatsapp', country='jp')

Image Sizes
-----------

Control image quality:

.. code-block:: python

   # Small images (512px)
   app = scraper.app_analyze('com.whatsapp', assets='SMALL')
   
   # Medium images (1024px) - default
   app = scraper.app_analyze('com.whatsapp', assets='MEDIUM')
   
   # Large images (2048px)
   app = scraper.app_analyze('com.whatsapp', assets='LARGE')
   
   # Original size
   app = scraper.app_analyze('com.whatsapp', assets='ORIGINAL')

Error Handling
--------------

Handle errors gracefully:

.. code-block:: python

   from gplay_scraper import GPlayScraper
   from gplay_scraper.exceptions import (
       AppNotFoundError,
       InvalidAppIdError,
       NetworkError
   )

   scraper = GPlayScraper()

   try:
       app = scraper.app_analyze('invalid.app.id')
   except InvalidAppIdError:
       print("Invalid app ID format")
   except AppNotFoundError:
       print("App not found on Play Store")
   except NetworkError:
       print("Network error occurred")

Common Patterns
---------------

Batch Processing
^^^^^^^^^^^^^^^^

.. code-block:: python

   app_ids = ['com.whatsapp', 'com.telegram', 'com.signal']
   
   for app_id in app_ids:
       app = scraper.app_analyze(app_id)
       print(f"{app['title']}: {app['realInstalls']:,} installs")

Market Research
^^^^^^^^^^^^^^^

.. code-block:: python

   # Find highly-rated messaging apps
   results = scraper.search_analyze('messaging', count=100)
   high_rated = [app for app in results if app['score'] >= 4.5]
   
   for app in high_rated:
       print(f"{app['title']}: {app['score']}/5")

Competitor Analysis
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Analyze your app vs competitors
   my_app = scraper.app_analyze('com.myapp')
   competitors = scraper.similar_analyze('com.myapp', count=10)
   
   print(f"My App: {my_app['score']}/5")
   print("\nCompetitors:")
   for comp in competitors:
       print(f"  {comp['title']}: {comp['score']}/5")

Review Monitoring
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Monitor negative reviews
   reviews = scraper.reviews_analyze('com.myapp', 
       count=100, 
       sort='NEWEST')
   
   negative = [r for r in reviews if r['score'] <= 2]
   
   for review in negative:
       print(f"{review['userName']}: {review['score']}/5")
       print(f"  {review['content']}")

Next Steps
----------

* :doc:`examples` - See more detailed examples
* :doc:`api/app` - Complete API reference
* :doc:`configuration` - Advanced configuration options
* :doc:`fields` - All available fields reference
