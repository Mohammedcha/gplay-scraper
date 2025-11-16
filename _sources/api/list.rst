List Methods
============

Get top charts (top free, top paid, top grossing apps).

Overview
--------

The List methods access Play Store top charts, returning 14 fields per app.

list_analyze()
--------------

**Signature:**

.. code-block:: python

   list_analyze(collection='TOP_FREE', category='APPLICATION', 
                count=100, lang='en', country='')

**Parameters:**

* ``collection`` - 'TOP_FREE', 'TOP_PAID', 'TOP_GROSSING'
* ``category`` - App category (default: 'APPLICATION')
* ``count`` - Number of apps (default: 100, max: ~500)

**Example:**

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   
   # Top free games
   top_free = scraper.list_analyze('TOP_FREE', category='GAME', count=100)
   
   for i, app in enumerate(top_free, 1):
       print(f"{i}. {app['title']} - {app['score']}/5")

Available Fields
----------------

14 fields including: title, appId, url, icon, screenshots, developer, genre, installs, description, score, scoreText, price, free, currency

Collections
-----------

* **TOP_FREE** - Top free apps
* **TOP_PAID** - Top paid apps
* **TOP_GROSSING** - Highest earning apps

App Categories (36)
-------------------

* ``APPLICATION`` - All apps (default)
* ``ANDROID_WEAR`` - Android Wear apps
* ``ART_AND_DESIGN`` - Art & design
* ``AUTO_AND_VEHICLES`` - Auto & vehicles
* ``BEAUTY`` - Beauty
* ``BOOKS_AND_REFERENCE`` - Books & reference
* ``BUSINESS`` - Business
* ``COMICS`` - Comics
* ``COMMUNICATION`` - Communication
* ``DATING`` - Dating
* ``EDUCATION`` - Education
* ``ENTERTAINMENT`` - Entertainment
* ``EVENTS`` - Events
* ``FINANCE`` - Finance
* ``FOOD_AND_DRINK`` - Food & drink
* ``HEALTH_AND_FITNESS`` - Health & fitness
* ``HOUSE_AND_HOME`` - House & home
* ``LIBRARIES_AND_DEMO`` - Libraries & demo
* ``LIFESTYLE`` - Lifestyle
* ``MAPS_AND_NAVIGATION`` - Maps & navigation
* ``MEDICAL`` - Medical
* ``MUSIC_AND_AUDIO`` - Music & audio
* ``NEWS_AND_MAGAZINES`` - News & magazines
* ``PARENTING`` - Parenting
* ``PERSONALIZATION`` - Personalization
* ``PHOTOGRAPHY`` - Photography
* ``PRODUCTIVITY`` - Productivity
* ``SHOPPING`` - Shopping
* ``SOCIAL`` - Social
* ``SPORTS`` - Sports
* ``TOOLS`` - Tools
* ``TRAVEL_AND_LOCAL`` - Travel & local
* ``VIDEO_PLAYERS`` - Video players & editors
* ``WATCH_FACE`` - Watch faces
* ``WEATHER`` - Weather
* ``FAMILY`` - Family

Game Categories (18)
---------------------

* ``GAME`` - All games
* ``GAME_ACTION`` - Action games
* ``GAME_ADVENTURE`` - Adventure games
* ``GAME_ARCADE`` - Arcade games
* ``GAME_BOARD`` - Board games
* ``GAME_CARD`` - Card games
* ``GAME_CASINO`` - Casino games
* ``GAME_CASUAL`` - Casual games
* ``GAME_EDUCATIONAL`` - Educational games
* ``GAME_MUSIC`` - Music games
* ``GAME_PUZZLE`` - Puzzle games
* ``GAME_RACING`` - Racing games
* ``GAME_ROLE_PLAYING`` - Role playing games
* ``GAME_SIMULATION`` - Simulation games
* ``GAME_SPORTS`` - Sports games
* ``GAME_STRATEGY`` - Strategy games
* ``GAME_TRIVIA`` - Trivia games
* ``GAME_WORD`` - Word games

Example
-------

.. code-block:: python

   # Top paid communication apps
   top_paid = scraper.list_analyze('TOP_PAID', 
       category='COMMUNICATION', 
       count=50)
