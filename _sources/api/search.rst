Search Methods
==============

Search for apps on Google Play Store by keyword and get results with 11 fields per app.

Overview
--------

The Search methods allow you to find apps by keyword, similar to using the Play Store search bar. Results include basic app information with 11 fields.

Available Methods
-----------------

* ``search_analyze()`` - Search and get all results
* ``search_get_field()`` - Get single field from all results
* ``search_get_fields()`` - Get multiple fields from all results
* ``search_print_field()`` - Print single field
* ``search_print_fields()`` - Print multiple fields
* ``search_print_all()`` - Print all results as JSON

search_analyze()
----------------

Search for apps and get complete results.

**Signature:**

.. code-block:: python

   search_analyze(query, count=100, lang='en', country='')

**Parameters:**

* ``query`` (str, required) - Search query string
* ``count`` (int, optional) - Number of results to return (default: 100, max: ~250)
* ``lang`` (str, optional) - Language code (default: 'en')
* ``country`` (str, optional) - Country code (default: '')

**Returns:**

List of dictionaries, each with 11 fields

**Example:**

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   results = scraper.search_analyze('messaging', count=10)
   
   for app in results:
       print(f"{app['title']} by {app['developer']}")
       print(f"  Rating: {app['score']}/5")
       print(f"  Free: {app['free']}")
       print(f"  URL: {app['url']}")

**Pagination Example:**

.. code-block:: python

   # Get top 100 results
   results = scraper.search_analyze('games', count=100)
   print(f"Found {len(results)} games")

search_get_field()
------------------

Get a single field from all search results.

**Signature:**

.. code-block:: python

   search_get_field(query, field, count=100, lang='en', country='')

**Parameters:**

* ``query`` (str, required) - Search query
* ``field`` (str, required) - Field name to retrieve
* ``count`` (int, optional) - Number of results
* ``lang`` (str, optional) - Language code
* ``country`` (str, optional) - Country code

**Returns:**

List of field values from all results

**Example:**

.. code-block:: python

   scraper = GPlayScraper()
   
   # Get all titles
   titles = scraper.search_get_field('messaging', 'title', count=10)
   print(titles)
   # ['WhatsApp Messenger', 'Telegram', 'Signal', ...]
   
   # Get all ratings
   scores = scraper.search_get_field('messaging', 'score', count=10)
   print(scores)
   # [4.2, 4.3, 4.5, ...]

search_get_fields()
-------------------

Get multiple fields from all search results.

**Signature:**

.. code-block:: python

   search_get_fields(query, fields, count=100, lang='en', country='')

**Parameters:**

* ``query`` (str, required) - Search query
* ``fields`` (list, required) - List of field names
* ``count`` (int, optional) - Number of results
* ``lang`` (str, optional) - Language code
* ``country`` (str, optional) - Country code

**Returns:**

List of dictionaries with requested fields

**Example:**

.. code-block:: python

   scraper = GPlayScraper()
   
   fields = ['title', 'developer', 'score', 'free']
   results = scraper.search_get_fields('games', fields, count=5)
   
   for app in results:
       print(f"{app['title']} - {app['score']}/5 - Free: {app['free']}")

search_print_field()
--------------------

Print single field from all search results.

**Signature:**

.. code-block:: python

   search_print_field(query, field, count=100, lang='en', country='')

**Returns:**

None (prints to console)

search_print_fields()
---------------------

Print multiple fields from all search results.

**Signature:**

.. code-block:: python

   search_print_fields(query, fields, count=100, lang='en', country='')

**Returns:**

None (prints to console)

search_print_all()
------------------

Print all search results as JSON.

**Signature:**

.. code-block:: python

   search_print_all(query, count=100, lang='en', country='')

**Returns:**

None (prints to console)

Available Fields
----------------

Each search result contains 11 fields:

* ``title`` - App name
* ``appId`` - Package identifier
* ``url`` - Play Store URL
* ``icon`` - App icon URL
* ``developer`` - Developer name
* ``summary`` - Short description
* ``score`` - Average rating (0-5)
* ``scoreText`` - Rating as text (e.g., "4.2★")
* ``price`` - App price
* ``free`` - Is free (boolean)
* ``currency`` - Currency code

Common Use Cases
----------------

Find Apps by Category
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   scraper = GPlayScraper()
   
   # Find fitness apps
   fitness_apps = scraper.search_analyze('fitness tracker', count=20)
   
   # Filter by rating
   high_rated = [app for app in fitness_apps if app['score'] >= 4.5]
   
   for app in high_rated:
       print(f"{app['title']}: {app['score']}/5")

Market Research
^^^^^^^^^^^^^^^

.. code-block:: python

   # Research competitors
   results = scraper.search_analyze('photo editor', count=50)
   
   # Analyze free vs paid
   free_apps = [app for app in results if app['free']]
   paid_apps = [app for app in results if not app['free']]
   
   print(f"Free apps: {len(free_apps)}")
   print(f"Paid apps: {len(paid_apps)}")
   
   # Average ratings
   avg_free = sum(app['score'] for app in free_apps) / len(free_apps)
   avg_paid = sum(app['score'] for app in paid_apps) / len(paid_apps)
   
   print(f"Average free app rating: {avg_free:.2f}")
   print(f"Average paid app rating: {avg_paid:.2f}")

Discovery
^^^^^^^^^

.. code-block:: python

   # Discover trending apps
   keywords = ['ai', 'chatbot', 'productivity']
   
   for keyword in keywords:
       results = scraper.search_analyze(keyword, count=5)
       print(f"\nTop {keyword} apps:")
       for app in results:
           print(f"  {app['title']} - {app['score']}/5")

Multi-Language Search
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Search in Spanish
   results_es = scraper.search_analyze('juegos', lang='es', count=10)
   
   # Search in French
   results_fr = scraper.search_analyze('jeux', lang='fr', count=10)
   
   # Regional search (UK)
   results_uk = scraper.search_analyze('games', country='gb', count=10)

See Also
--------

* :doc:`app` - Get detailed app information
* :doc:`../examples` - More practical examples
* :doc:`../configuration` - Configuration options
