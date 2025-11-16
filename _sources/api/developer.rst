Developer Methods
=================

Get all apps from a specific developer or company.

Overview
--------

The Developer methods allow you to find all apps published by a developer, returning 11 fields per app.

Available Methods
-----------------

* ``developer_analyze()`` - Get all developer apps
* ``developer_get_field()`` - Get single field from all apps
* ``developer_get_fields()`` - Get multiple fields from all apps
* ``developer_print_field()`` - Print single field
* ``developer_print_fields()`` - Print multiple fields
* ``developer_print_all()`` - Print all apps as JSON

developer_analyze()
-------------------

Get all apps from a developer.

**Signature:**

.. code-block:: python

   developer_analyze(dev_id, count=100, lang='en', country='')

**Parameters:**

* ``dev_id`` (str, required) - Developer name or numeric ID
* ``count`` (int, optional) - Number of apps (default: 100)
* ``lang`` (str, optional) - Language code
* ``country`` (str, optional) - Country code

**Returns:**

List of dictionaries, each with 11 fields

**Example:**

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   
   # Using developer name
   apps = scraper.developer_analyze('Google LLC')
   
   for app in apps:
       print(f"{app['title']}")
       print(f"  Developer: {app['developer']}")
       print(f"  Rating: {app['score']}/5")
       print(f"  Free: {app['free']}")

**Using Numeric Developer ID:**

.. code-block:: python

   # Using numeric ID
   apps = scraper.developer_analyze('5700313618786177705')

Available Fields
----------------

Each app contains 11 fields:

* ``appId`` - Package identifier
* ``title`` - App name
* ``url`` - Play Store URL
* ``icon`` - App icon URL
* ``developer`` - Developer name
* ``description`` - App description
* ``score`` - Average rating (0-5)
* ``scoreText`` - Rating as text
* ``price`` - App price
* ``free`` - Is free (boolean)
* ``currency`` - Currency code

Common Use Cases
----------------

Portfolio Analysis
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   scraper = GPlayScraper()
   apps = scraper.developer_analyze('Google LLC')
   
   # Calculate average rating
   avg_rating = sum(app['score'] for app in apps) / len(apps)
   
   # Count free vs paid
   free_count = sum(1 for app in apps if app['free'])
   paid_count = len(apps) - free_count
   
   print(f"Total apps: {len(apps)}")
   print(f"Average rating: {avg_rating:.2f}/5")
   print(f"Free apps: {free_count}, Paid apps: {paid_count}")

Competitive Analysis
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   developers = ['Google LLC', 'Microsoft Corporation', 'Meta Platforms, Inc.']
   
   for dev in developers:
       apps = scraper.developer_analyze(dev)
       high_rated = [app for app in apps if app['score'] >= 4.5]
       
       print(f"\n{dev}:")
       print(f"  Total apps: {len(apps)}")
       print(f"  High-rated apps (4.5+): {len(high_rated)}")

See Also
--------

* :doc:`app` - Get detailed app information
* :doc:`similar` - Find similar apps
