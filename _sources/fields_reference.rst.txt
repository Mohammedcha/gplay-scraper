Fields Reference
================

This document lists all available fields for each method type.

App Methods Fields (65+)
-------------------------

Basic Information
~~~~~~~~~~~~~~~~~

- ``appId`` - Package name (e.g., "com.whatsapp")
- ``title`` - App name
- ``summary`` - Short description
- ``description`` - Full description
- ``url`` - Play Store URL

Ratings & Reviews
~~~~~~~~~~~~~~~~~

- ``score`` - Average rating (1-5)
- ``ratings`` - Total number of ratings
- ``reviews`` - Total number of reviews
- ``histogram`` - Rating distribution [1★, 2★, 3★, 4★, 5★]

Install Metrics
~~~~~~~~~~~~~~~

- ``installs`` - Install range (e.g., "10,000,000+")
- ``minInstalls`` - Minimum installs
- ``realInstalls`` - Estimated real installs

Pricing
~~~~~~~

- ``price`` - Price in currency (0 if free)
- ``currency`` - Currency code (e.g., "USD")
- ``free`` - Boolean, true if free
- ``offersIAP`` - Has in-app purchases
- ``inAppProductPrice`` - IAP price range
- ``sale`` - Currently on sale
- ``originalPrice`` - Original price if on sale

Media
~~~~~

- ``icon`` - App icon URL
- ``headerImage`` - Header image URL
- ``screenshots`` - List of screenshot URLs
- ``video`` - Promo video URL
- ``videoImage`` - Video thumbnail URL

Developer
~~~~~~~~~

- ``developer`` - Developer name
- ``developerId`` - Developer ID
- ``developerEmail`` - Contact email
- ``developerWebsite`` - Website URL
- ``developerAddress`` - Physical address
- ``developerPhone`` - Contact phone
- ``privacyPolicy`` - Privacy policy URL

Category
~~~~~~~~

- ``genre`` - Primary category (e.g., "Communication")
- ``genreId`` - Category ID (e.g., "COMMUNICATION")
- ``categories`` - List of categories

Technical
~~~~~~~~~

- ``version`` - Current version
- ``androidVersion`` - Required Android version
- ``minAndroidApi`` - Minimum API level
- ``maxAndroidApi`` - Maximum API level

Dates
~~~~~

- ``released`` - Release date
- ``lastUpdated`` - Last update date
- ``updatedTimestamp`` - Update timestamp

Content
~~~~~~~

- ``contentRating`` - Age rating (e.g., "Everyone")
- ``contentRatingDescription`` - Rating description
- ``whatsNew`` - Recent changes list
- ``permissions`` - Required permissions dict
- ``dataSafety`` - Data safety info list

Advertising
~~~~~~~~~~~

- ``adSupported`` - Contains ads
- ``containsAds`` - Shows advertisements

Availability
~~~~~~~~~~~~

- ``available`` - App is available

Search Methods Fields
---------------------

- ``appId`` - App package name
- ``title`` - App name
- ``icon`` - App icon URL
- ``url`` - Play Store URL
- ``developer`` - Developer name
- ``score`` - Average rating (1-5)
- ``scoreText`` - Rating as text
- ``currency`` - Price currency
- ``price`` - App price (0 if free)
- ``free`` - Boolean, true if free
- ``summary`` - App description

Reviews Methods Fields
----------------------

- ``reviewId`` - Unique review ID
- ``userName`` - Reviewer name
- ``userImage`` - Reviewer avatar URL
- ``score`` - Review rating (1-5 stars)
- ``content`` - Review text/comment
- ``thumbsUpCount`` - Number of helpful votes
- ``appVersion`` - App version reviewed
- ``at`` - Review timestamp (ISO 8601 format)

Developer Methods Fields
------------------------

- ``appId`` - App package name
- ``title`` - App name
- ``icon`` - App icon URL
- ``url`` - Play Store URL
- ``developer`` - Developer name
- ``description`` - App description
- ``score`` - Average rating (1-5)
- ``scoreText`` - Rating as text
- ``currency`` - Price currency
- ``price`` - App price (0 if free)
- ``free`` - Boolean, true if free

List Methods Fields
-------------------

- ``appId`` - App package name
- ``title`` - App name
- ``icon`` - App icon URL
- ``screenshots`` - List of screenshot URLs
- ``url`` - Play Store URL
- ``developer`` - Developer name
- ``genre`` - App category
- ``installs`` - Install count
- ``score`` - Average rating (1-5)
- ``scoreText`` - Rating as text
- ``currency`` - Price currency
- ``price`` - App price (0 if free)
- ``free`` - Boolean, true if free
- ``description`` - App description

Similar Methods Fields
----------------------

- ``appId`` - App package name
- ``title`` - App name
- ``icon`` - App icon URL
- ``url`` - Play Store URL
- ``developer`` - Developer name
- ``description`` - App description
- ``score`` - Average rating (1-5)
- ``scoreText`` - Rating as text
- ``currency`` - Price currency
- ``price`` - App price (0 if free)
- ``free`` - Boolean, true if free

Suggest Methods Fields
----------------------

Returns a list of suggestion strings (no field structure).

Example:

.. code-block:: python

   suggestions = scraper.suggest_analyze("fitness")
   # Returns: ['fitness tracker', 'fitness app', 'fitness watch', ...]

List Methods Categories
-----------------------

Collections
~~~~~~~~~~~

- ``TOP_FREE`` - Top free apps
- ``TOP_PAID`` - Top paid apps
- ``TOP_GROSSING`` - Top grossing apps

App Categories
~~~~~~~~~~~~~~

- ``APPLICATION`` - All apps
- ``COMMUNICATION`` - Communication
- ``SOCIAL`` - Social
- ``PRODUCTIVITY`` - Productivity
- ``ENTERTAINMENT`` - Entertainment
- ``TOOLS`` - Tools
- ``BUSINESS`` - Business
- ``FINANCE`` - Finance
- ``EDUCATION`` - Education
- ``HEALTH_AND_FITNESS`` - Health & fitness
- ``PHOTOGRAPHY`` - Photography
- ``MUSIC_AND_AUDIO`` - Music & audio
- ``NEWS_AND_MAGAZINES`` - News & magazines
- ``SHOPPING`` - Shopping
- ``TRAVEL_AND_LOCAL`` - Travel & local
- ``BOOKS_AND_REFERENCE`` - Books & reference
- ``LIFESTYLE`` - Lifestyle
- ``WEATHER`` - Weather
- ``MAPS_AND_NAVIGATION`` - Maps & navigation
- ``FOOD_AND_DRINK`` - Food & drink
- ``DATING`` - Dating
- ``BEAUTY`` - Beauty
- ``MEDICAL`` - Medical
- ``SPORTS`` - Sports
- ``PARENTING`` - Parenting
- ``PERSONALIZATION`` - Personalization
- ``AUTO_AND_VEHICLES`` - Auto & vehicles
- ``HOUSE_AND_HOME`` - House & home
- ``ART_AND_DESIGN`` - Art & design
- ``EVENTS`` - Events
- ``COMICS`` - Comics
- ``LIBRARIES_AND_DEMO`` - Libraries & demo
- ``VIDEO_PLAYERS`` - Video players
- ``WATCH_FACE`` - Watch faces
- ``ANDROID_WEAR`` - Android Wear
- ``FAMILY`` - Family

Game Categories
~~~~~~~~~~~~~~~

- ``GAME`` - All games
- ``GAME_ACTION`` - Action
- ``GAME_ADVENTURE`` - Adventure
- ``GAME_ARCADE`` - Arcade
- ``GAME_BOARD`` - Board
- ``GAME_CARD`` - Card
- ``GAME_CASINO`` - Casino
- ``GAME_CASUAL`` - Casual
- ``GAME_EDUCATIONAL`` - Educational
- ``GAME_MUSIC`` - Music
- ``GAME_PUZZLE`` - Puzzle
- ``GAME_RACING`` - Racing
- ``GAME_ROLE_PLAYING`` - Role playing
- ``GAME_SIMULATION`` - Simulation
- ``GAME_SPORTS`` - Sports
- ``GAME_STRATEGY`` - Strategy
- ``GAME_TRIVIA`` - Trivia
- ``GAME_WORD`` - Word

Reviews Methods Sort Options
-----------------------------

- ``NEWEST`` - Most recent reviews first (default)
- ``RELEVANT`` - Most relevant/helpful reviews
- ``RATING`` - Sorted by rating

Example:

.. code-block:: python

   # Get newest reviews
   reviews = scraper.reviews_analyze("com.whatsapp", sort="NEWEST")
   
   # Get most relevant reviews
   reviews = scraper.reviews_analyze("com.whatsapp", sort="RELEVANT")
   
   # Get reviews sorted by rating
   reviews = scraper.reviews_analyze("com.whatsapp", sort="RATING")
