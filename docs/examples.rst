Examples
========

Practical examples of using GPlay Scraper for common tasks.

App Analytics Dashboard
-----------------------

Track key metrics for your app.

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   app = scraper.app_analyze('com.myapp')
   
   print("=== App Analytics Dashboard ===")
   print(f"App: {app['title']}")
   print(f"Developer: {app['developer']}")
   print(f"Rating: {app['score']}/5 ({app['ratings']:,} ratings)")
   print(f"\nInstall Metrics:")
   print(f"  Total Installs: {app['realInstalls']:,}")
   print(f"  Daily Installs: {app['dailyInstalls']:,}")
   print(f"  Monthly Installs: {app['monthlyInstalls']:,}")
   print(f"  App Age: {app['appAgeDays']} days")
   print(f"\nRating Distribution:")
   hist = app['histogram']
   for i, count in enumerate(hist, 1):
       print(f"  {i}★: {count:,}")

Market Research
---------------

Analyze a market segment.

.. code-block:: python

   scraper = GPlayScraper()
   
   # Search for fitness apps
   results = scraper.search_analyze('fitness tracker', count=100)
   
   # Filter by rating
   high_rated = [app for app in results if app['score'] >= 4.5]
   free_apps = [app for app in high_rated if app['free']]
   
   print(f"Total fitness tracker apps: {len(results)}")
   print(f"High-rated (4.5+): {len(high_rated)}")
   print(f"High-rated & Free: {len(free_apps)}")
   
   print("\nTop 5 Free High-Rated Apps:")
   for app in free_apps[:5]:
       print(f"  {app['title']}: {app['score']}/5")

Competitor Monitoring
---------------------

Track your competitors.

.. code-block:: python

   scraper = GPlayScraper()
   
   competitors = ['com.competitor1', 'com.competitor2', 'com.competitor3']
   
   print("Competitor Analysis")
   print("-" * 60)
   
   for app_id in competitors:
       app = scraper.app_analyze(app_id)
       reviews = scraper.reviews_analyze(app_id, count=100, sort='NEWEST')
       
       avg_recent_rating = sum(r['score'] for r in reviews) / len(reviews)
       
       print(f"\n{app['title']}")
       print(f"  Overall Rating: {app['score']}/5")
       print(f"  Recent Rating: {avg_recent_rating:.2f}/5")
       print(f"  Daily Installs: {app['dailyInstalls']:,}")
       print(f"  Total Installs: {app['realInstalls']:,}")

Review Sentiment Analysis
--------------------------

Analyze user feedback.

.. code-block:: python

   scraper = GPlayScraper()
   
   reviews = scraper.reviews_analyze('com.myapp', count=500)
   
   # Categorize by rating
   positive = [r for r in reviews if r['score'] >= 4]
   neutral = [r for r in reviews if r['score'] == 3]
   negative = [r for r in reviews if r['score'] <= 2]
   
   print("Review Sentiment Analysis")
   print(f"Total Reviews: {len(reviews)}")
   print(f"Positive (4-5★): {len(positive)} ({len(positive)/len(reviews)*100:.1f}%)")
   print(f"Neutral (3★): {len(neutral)} ({len(neutral)/len(reviews)*100:.1f}%)")
   print(f"Negative (1-2★): {len(negative)} ({len(negative)/len(reviews)*100:.1f}%)")
   
   # Show recent negative reviews
   print("\nRecent Negative Reviews:")
   for review in negative[:5]:
       print(f"  {review['userName']}: {review['score']}/5")
       print(f"    {review['content'][:100]}...")

Top Charts Tracking
-------------------

Monitor top charts positions.

.. code-block:: python

   scraper = GPlayScraper()
   
   # Track top free games
   top_games = scraper.list_analyze('TOP_FREE', category='GAME', count=50)
   
   # Find your app's position
   my_app_id = 'com.mygame'
   position = next((i for i, app in enumerate(top_games, 1) 
                    if app['appId'] == my_app_id), None)
   
   if position:
       print(f"Your game is ranked #{position} in top free games!")
   else:
       print("Your game is not in top 50")
   
   # Show top 10
   print("\nTop 10 Free Games:")
   for i, app in enumerate(top_games[:10], 1):
       print(f"{i}. {app['title']} - {app['score']}/5")

Developer Portfolio Overview
-----------------------------

Analyze a developer's entire portfolio.

.. code-block:: python

   scraper = GPlayScraper()
   
   apps = scraper.developer_analyze('Google LLC')
   
   # Calculate metrics
   avg_rating = sum(app['score'] for app in apps) / len(apps)
   free_count = sum(1 for app in apps if app['free'])
   high_rated = [app for app in apps if app['score'] >= 4.5]
   
   print(f"Developer: Google LLC")
   print(f"Total Apps: {len(apps)}")
   print(f"Average Rating: {avg_rating:.2f}/5")
   print(f"Free Apps: {free_count}/{len(apps)}")
   print(f"High-Rated Apps (4.5+): {len(high_rated)}")
   
   # Best rated apps
   sorted_apps = sorted(apps, key=lambda x: x['score'], reverse=True)
   print("\nTop 5 Highest Rated:")
   for app in sorted_apps[:5]:
       print(f"  {app['title']}: {app['score']}/5")

Batch Data Collection
----------------------

Collect data for multiple apps efficiently.

.. code-block:: python

   import json
   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   
   app_ids = [
       'com.whatsapp',
       'org.telegram.messenger',
       'org.thoughtcrime.securesms',
       'com.discord'
   ]
   
   results = []
   for app_id in app_ids:
       # Get only the fields you need
       fields = ['title', 'developer', 'score', 'realInstalls', 'dailyInstalls']
       data = scraper.app_get_fields(app_id, fields)
       results.append(data)
   
   # Save to JSON
   with open('messaging_apps.json', 'w') as f:
       json.dump(results, f, indent=2)
   
   print(f"Collected data for {len(results)} apps")

Multi-Language Content
----------------------

Get localized app information.

.. code-block:: python

   scraper = GPlayScraper()
   
   languages = {
       'en': 'English',
       'es': 'Spanish',
       'fr': 'French',
       'de': 'German',
       'ja': 'Japanese'
   }
   
   for lang_code, lang_name in languages.items():
       app = scraper.app_analyze('com.whatsapp', lang=lang_code)
       print(f"\n{lang_name} ({lang_code}):")
       print(f"  Title: {app['title']}")
       print(f"  Summary: {app['summary']}")

Trend Discovery
---------------

Discover trending apps in a category.

.. code-block:: python

   scraper = GPlayScraper()
   
   # Get top free apps
   top_free = scraper.list_analyze('TOP_FREE', category='PRODUCTIVITY', count=100)
   
   # Filter for new apps (less than 180 days old)
   new_apps = [app for app in top_free if 'New' in app.get('description', '')]
   
   # Get apps with high install velocity
   trending = []
   for app in top_free[:20]:
       full_data = scraper.app_analyze(app['appId'])
       if full_data['dailyInstalls'] > 10000:
           trending.append(full_data)
   
   print("Trending Productivity Apps:")
   for app in trending:
       print(f"  {app['title']}")
       print(f"    Daily Installs: {app['dailyInstalls']:,}")
       print(f"    Rating: {app['score']}/5")

See Also
--------

* :doc:`quickstart` - Basic usage guide
* :doc:`api/app` - Complete API reference
* :doc:`configuration` - Configuration options
