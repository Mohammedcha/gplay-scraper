Examples
========

This section provides practical examples for common use cases.

Basic App Information
---------------------

Get essential app details:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   app_id = "com.whatsapp"

   # Get basic info using app_get_fields
   basic_info = scraper.app_get_fields(app_id, [
       "title", "developer", "genre", "score", "free"
   ], lang="en", country="us")
   
   # Get high-quality media assets
   media_info = scraper.app_get_fields(app_id, [
       "icon", "screenshots", "headerImage"
   ], assets="LARGE")  # 2048px images

   for field, value in basic_info.items():
       print(f"{field}: {value}")

**Output:**

.. code-block:: text

   title: WhatsApp Messenger
   developer: WhatsApp LLC
   genre: Communication
   score: 4.3
   free: True

Competitive Analysis
--------------------

Compare multiple apps across key metrics:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()

   # Messaging apps
   apps = {
       "WhatsApp": "com.whatsapp",
       "Telegram": "org.telegram.messenger", 
       "Signal": "org.thoughtcrime.securesms"
   }

   results = []
   for name, app_id in apps.items():
       try:
           # Use app_get_fields with parameters
           data = scraper.app_get_fields(app_id, [
               "title", "score", "ratings", "installs", "icon"
           ], lang="en", country="us", assets="SMALL")  # Small icons for faster loading
           data["name"] = name
           results.append(data)
       except Exception as e:
           print(f"Error analyzing {name}: {e}")

   # Sort by rating
   results.sort(key=lambda x: x.get("score", 0), reverse=True)

   print("Ranking by Rating:")
   for i, app in enumerate(results, 1):
       print(f"{i}. {app['name']}: {app.get('score', 'N/A')} stars")

Search and Filter Apps
----------------------

Search for apps and filter results:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()

   # Search for fitness apps
   results = scraper.search_analyze("fitness tracker", count=50, lang="en", country="us")
   
   # Filter free apps with high ratings
   top_free = [app for app in results if app.get('free') and app.get('score', 0) >= 4.5]
   
   print("Top Free Fitness Apps:")
   for app in top_free[:10]:
       print(f"{app['title']}: {app['score']} stars - {app['installs']}")

Get Developer Portfolio
-----------------------

Analyze all apps from a developer:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   
   # WhatsApp Inc. developer ID
   dev_id = "5700313618786177705"

   # Get all developer apps
   apps = scraper.developer_analyze(dev_id, count=50, lang="en", country="us")

   print(f"Developer has {len(apps)} apps:")
   for app in apps:
       print(f"  {app['title']}: {app['score']} stars - {app['installs']}")

Get Reviews with Sentiment Analysis
------------------------------------

Extract and analyze user reviews:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   app_id = "com.whatsapp"

   # Get recent reviews
   reviews = scraper.reviews_analyze(app_id, count=100, sort="NEWEST", lang="en", country="us")

   # Analyze ratings distribution
   ratings = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
   for review in reviews:
       ratings[review['score']] += 1

   print("Ratings Distribution:")
   for stars, count in ratings.items():
       print(f"  {stars} stars: {count} reviews")
   
   # Get positive reviews (4-5 stars)
   positive = [r for r in reviews if r['score'] >= 4]
   print(f"\nPositive reviews: {len(positive)}/{len(reviews)}")

Get Top Charts by Category
---------------------------

Analyze top performing apps:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()

   # Get top free games
   top_games = scraper.list_analyze("TOP_FREE", "GAME", count=50, lang="en", country="us")
   
   print("Top 10 Free Games:")
   for i, app in enumerate(top_games[:10], 1):
       print(f"{i}. {app['title']} - {app['developer']}")
       print(f"   Rating: {app['score']} | Installs: {app['installs']}")
   
   # Get top paid apps
   top_paid = scraper.list_analyze("TOP_PAID", "APPLICATION", count=20, lang="en", country="us")
   
   print("\nTop 5 Paid Apps:")
   for i, app in enumerate(top_paid[:5], 1):
       print(f"{i}. {app['title']} - ${app['price']}")

Find Similar Apps
-----------------

Discover competitor apps:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   app_id = "com.whatsapp"

   # Get similar apps
   similar = scraper.similar_analyze(app_id, count=30, lang="en", country="us")
   
   print(f"Apps similar to WhatsApp:")
   for app in similar[:10]:
       print(f"  {app['title']} by {app['developer']}")
       print(f"    Rating: {app['score']} | {app['installs']}")

Get Search Suggestions
----------------------

Find popular search terms:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()

   # Get suggestions for a term
   suggestions = scraper.suggest_analyze("photo editor", count=10, lang="en", country="us")
   
   print("Popular searches:")
   for suggestion in suggestions:
       print(f"  - {suggestion}")
   
   # Get nested suggestions
   nested = scraper.suggest_nested("fitness", count=5, lang="en", country="us")
   for term, related in nested.items():
       print(f"{term}: {related}")

Assets Parameter - Image Sizes
-------------------------------

Control image quality for icons, screenshots, and media:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   app_id = "com.whatsapp"

   # Get different image sizes
   small_icon = scraper.app_get_field(app_id, "icon", assets="SMALL")
   # Returns: https://...=w512

   medium_icon = scraper.app_get_field(app_id, "icon", assets="MEDIUM")
   # Returns: https://...=w1024 (default)

   large_icon = scraper.app_get_field(app_id, "icon", assets="LARGE")
   # Returns: https://...=w2048

   original_icon = scraper.app_get_field(app_id, "icon", assets="ORIGINAL")
   # Returns: https://...=w9999 (maximum quality)

   # Get all media with custom sizes
   media = scraper.app_get_fields(app_id, [
       "icon", "screenshots", "headerImage", "videoImage"
   ], assets="ORIGINAL")

   print(f"Icon: {media['icon']}")
   print(f"Screenshots: {len(media['screenshots'])} images")
   print(f"Header: {media['headerImage']}")

   # Print methods also support assets parameter
   scraper.app_print_field(app_id, "icon", assets="LARGE")
   scraper.app_print_all(app_id, assets="ORIGINAL")

Multi-Language Support
----------------------

Get localized data:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   app_id = "com.whatsapp"

   # Get app data in different languages
   languages = [
       ("en", "us", "English"),
       ("es", "es", "Spanish"),
       ("fr", "fr", "French"),
       ("de", "de", "German")
   ]

   for lang, country, name in languages:
       data = scraper.app_get_fields(app_id, ["title", "description"], lang=lang, country=country)
       print(f"\n{name}:")
       print(f"  Title: {data['title']}")
       print(f"  Description: {data['description'][:100]}...")

HTTP Client Selection
---------------------

Choose different HTTP clients:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   # Try different HTTP clients
   clients = ["requests", "curl_cffi", "tls_client", "httpx"]

   for client in clients:
       try:
           scraper = GPlayScraper(http_client=client)
           data = scraper.app_get_field("com.whatsapp", "title")
           print(f"{client}: Success - {data}")
       except Exception as e:
           print(f"{client}: Failed - {e}")

Real-World Use Cases
--------------------

**Market Research**
  Analyze competitor apps to understand market positioning and user satisfaction.

**Keyword Research**
  Use search suggestions to discover popular keywords for app optimization.

**App Monitoring**
  Track your app's performance metrics over time.

**Data Analysis**
  Collect app data for research, reporting, or machine learning projects.

**Competitive Intelligence**
  Monitor competitor updates, ratings, and user feedback.

**Image Quality Control**
  Use assets parameter to get appropriate image sizes for different use cases:
  
  - **SMALL (512px)** - Thumbnails, lists, mobile displays
  - **MEDIUM (1024px)** - Standard web displays, default quality
  - **LARGE (2048px)** - High-resolution displays, detailed views
  - **ORIGINAL (max)** - Print quality, archival purposes