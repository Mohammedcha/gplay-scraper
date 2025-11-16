App Methods
===========

Extract comprehensive app data with 57 fields including install analytics, ratings, pricing, and developer information.

Overview
--------

The App methods provide access to detailed information about any Google Play Store app. All methods return data in JSON format with 57 fields.

Available Methods
-----------------

* ``app_analyze()`` - Get all 57 fields
* ``app_get_field()`` - Get single field value
* ``app_get_fields()`` - Get multiple field values
* ``app_print_field()`` - Print single field
* ``app_print_fields()`` - Print multiple fields
* ``app_print_all()`` - Print all data as JSON

app_analyze()
-------------

Get complete app data with all 57 fields.

**Signature:**

.. code-block:: python

   app_analyze(app_id, lang='en', country='', assets=None)

**Parameters:**

* ``app_id`` (str, required) - Google Play app ID (e.g., 'com.whatsapp')
* ``lang`` (str, optional) - Language code (default: 'en')
* ``country`` (str, optional) - Country code (default: '')
* ``assets`` (str, optional) - Image size: 'SMALL', 'MEDIUM', 'LARGE', 'ORIGINAL'

**Returns:**

Dictionary with 57 fields

**Example:**

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   app = scraper.app_analyze('com.whatsapp')
   
   print(app['title'])              # WhatsApp Messenger
   print(app['developer'])          # WhatsApp LLC
   print(app['score'])              # 4.2189474
   print(app['realInstalls'])       # 10931553905
   print(app['dailyInstalls'])      # 1815870
   print(app['publisherCountry'])   # United States

**Multi-language Example:**

.. code-block:: python

   # Get app data in Spanish
   app_es = scraper.app_analyze('com.whatsapp', lang='es')
   print(app_es['description'])  # Description in Spanish
   
   # Get app data for UK region
   app_uk = scraper.app_analyze('com.whatsapp', country='gb')

**Image Size Example:**

.. code-block:: python

   # Get large images
   app = scraper.app_analyze('com.whatsapp', assets='LARGE')
   print(app['icon'])  # URL with =w2048 parameter

app_get_field()
---------------

Get a single field value from app data.

**Signature:**

.. code-block:: python

   app_get_field(app_id, field, lang='en', country='', assets=None)

**Parameters:**

* ``app_id`` (str, required) - Google Play app ID
* ``field`` (str, required) - Field name to retrieve
* ``lang`` (str, optional) - Language code
* ``country`` (str, optional) - Country code
* ``assets`` (str, optional) - Image size

**Returns:**

Value of the requested field (type depends on field)

**Example:**

.. code-block:: python

   scraper = GPlayScraper()
   
   # Get title
   title = scraper.app_get_field('com.whatsapp', 'title')
   print(title)  # "WhatsApp Messenger"
   
   # Get score
   score = scraper.app_get_field('com.whatsapp', 'score')
   print(score)  # 4.2189474
   
   # Get daily installs
   daily = scraper.app_get_field('com.whatsapp', 'dailyInstalls')
   print(f"{daily:,}")  # 1,815,870

app_get_fields()
----------------

Get multiple field values from app data.

**Signature:**

.. code-block:: python

   app_get_fields(app_id, fields, lang='en', country='', assets=None)

**Parameters:**

* ``app_id`` (str, required) - Google Play app ID
* ``fields`` (list, required) - List of field names
* ``lang`` (str, optional) - Language code
* ``country`` (str, optional) - Country code
* ``assets`` (str, optional) - Image size

**Returns:**

Dictionary with requested fields and values

**Example:**

.. code-block:: python

   scraper = GPlayScraper()
   
   fields = ['title', 'developer', 'score', 'realInstalls', 'dailyInstalls']
   data = scraper.app_get_fields('com.whatsapp', fields)
   
   print(data)
   # {
   #     'title': 'WhatsApp Messenger',
   #     'developer': 'WhatsApp LLC',
   #     'score': 4.2189474,
   #     'realInstalls': 10931553905,
   #     'dailyInstalls': 1815870
   # }

app_print_field()
-----------------

Print a single field value to console.

**Signature:**

.. code-block:: python

   app_print_field(app_id, field, lang='en', country='', assets=None)

**Returns:**

None (prints to console)

**Example:**

.. code-block:: python

   scraper = GPlayScraper()
   scraper.app_print_field('com.whatsapp', 'title')
   # Output: title: WhatsApp Messenger

app_print_fields()
------------------

Print multiple field values to console.

**Signature:**

.. code-block:: python

   app_print_fields(app_id, fields, lang='en', country='', assets=None)

**Returns:**

None (prints to console)

**Example:**

.. code-block:: python

   scraper = GPlayScraper()
   fields = ['title', 'score', 'dailyInstalls']
   scraper.app_print_fields('com.whatsapp', fields)

app_print_all()
---------------

Print all 57 fields as formatted JSON to console.

**Signature:**

.. code-block:: python

   app_print_all(app_id, lang='en', country='', assets=None)

**Returns:**

None (prints to console)

**Example:**

.. code-block:: python

   scraper = GPlayScraper()
   scraper.app_print_all('com.whatsapp')
   # Outputs all 57 fields as formatted JSON

Available Fields
----------------

The App methods return 57 fields organized into categories:

**Basic Information (5 fields)**

* ``appId`` - Package identifier
* ``title`` - App name
* ``summary`` - Short description
* ``description`` - Full description
* ``appUrl`` - Play Store URL

**Category (4 fields)**

* ``genre`` - Primary category
* ``genreId`` - Category ID
* ``categories`` - All categories (array)
* ``available`` - Availability status (boolean)

**Release & Updates (3 fields)**

* ``released`` - Release date
* ``appAgeDays`` - Days since release (computed)
* ``lastUpdated`` - Last update date

**Media (5 fields)**

* ``icon`` - App icon URL
* ``headerImage`` - Header image URL
* ``screenshots`` - Screenshot URLs (array)
* ``video`` - Promotional video URL
* ``videoImage`` - Video thumbnail URL

**Install Statistics (10 fields)**

* ``installs`` - Install range string
* ``minInstalls`` - Minimum installs
* ``realInstalls`` - Exact install count
* ``dailyInstalls`` - Average daily installs (computed)
* ``minDailyInstalls`` - Min daily installs (computed)
* ``realDailyInstalls`` - Real daily installs (computed)
* ``monthlyInstalls`` - Average monthly installs (computed)
* ``minMonthlyInstalls`` - Min monthly installs (computed)
* ``realMonthlyInstalls`` - Real monthly installs (computed)

**Ratings (4 fields)**

* ``score`` - Average rating (0-5)
* ``ratings`` - Total number of ratings
* ``reviews`` - Total number of reviews
* ``histogram`` - Rating distribution [1★, 2★, 3★, 4★, 5★]

**Ads (2 fields)**

* ``adSupported`` - Supports ads (boolean)
* ``containsAds`` - Contains ads (boolean)

**Technical (7 fields)**

* ``version`` - Current version
* ``androidVersion`` - Minimum Android version
* ``maxAndroidApi`` - Maximum Android API level
* ``minAndroidApi`` - Minimum Android API level
* ``appBundle`` - Bundle identifier
* ``contentRating`` - Age rating
* ``contentRatingDescription`` - Rating description

**Updates (1 field)**

* ``whatsNew`` - Changelog (array)

**Privacy (2 fields)**

* ``permissions`` - Required permissions (object)
* ``dataSafety`` - Data safety info (array)

**Pricing (7 fields)**

* ``price`` - App price
* ``currency`` - Currency code
* ``free`` - Is free (boolean)
* ``offersIAP`` - Has in-app purchases (boolean)
* ``inAppProductPrice`` - IAP price range
* ``sale`` - On sale (boolean)
* ``originalPrice`` - Original price if on sale

**Developer (8 fields)**

* ``developer`` - Developer name
* ``developerId`` - Developer ID
* ``developerEmail`` - Contact email
* ``developerWebsite`` - Website URL
* ``developerAddress`` - Physical address
* ``developerPhone`` - Contact phone
* ``publisherCountry`` - Publisher country (computed)
* ``privacyPolicy`` - Privacy policy URL

Common Use Cases
----------------

App Analytics
^^^^^^^^^^^^^

.. code-block:: python

   scraper = GPlayScraper()
   app = scraper.app_analyze('com.whatsapp')
   
   print(f"App: {app['title']}")
   print(f"Total Installs: {app['realInstalls']:,}")
   print(f"Daily Installs: {app['dailyInstalls']:,}")
   print(f"Monthly Installs: {app['monthlyInstalls']:,}")
   print(f"Age: {app['appAgeDays']} days")
   print(f"Rating: {app['score']}/5 ({app['ratings']:,} ratings)")

Competitor Comparison
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   apps = ['com.whatsapp', 'org.telegram.messenger', 'org.thoughtcrime.securesms']
   
   for app_id in apps:
       app = scraper.app_analyze(app_id)
       print(f"{app['title']}")
       print(f"  Installs: {app['realInstalls']:,}")
       print(f"  Rating: {app['score']}/5")
       print(f"  Daily Growth: {app['dailyInstalls']:,}")

Market Research
^^^^^^^^^^^^^^^

.. code-block:: python

   # Get key metrics for analysis
   fields = [
       'title', 'developer', 'score', 'ratings',
       'realInstalls', 'dailyInstalls', 'free', 'price'
   ]
   
   apps = ['com.app1', 'com.app2', 'com.app3']
   
   for app_id in apps:
       data = scraper.app_get_fields(app_id, fields)
       print(data)

See Also
--------

* :doc:`../fields` - Complete field reference
* :doc:`../examples` - More practical examples
* :doc:`../configuration` - Configuration options
