Similar Methods
===============

Find apps similar to a given app (competitors or alternatives).

Overview
--------

The Similar methods help you discover competitor apps or alternatives, returning 11 fields per app.

similar_analyze()
-----------------

**Signature:**

.. code-block:: python

   similar_analyze(app_id, count=100, lang='en', country='')

**Example:**

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   similar = scraper.similar_analyze('com.whatsapp', count=20)
   
   for app in similar:
       print(f"{app['title']} - {app['score']}/5")

Available Fields
----------------

Same 11 fields as Developer Methods.

Common Use Cases
----------------

Competitor Analysis
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Find competitors
   my_app = scraper.app_analyze('com.myapp')
   competitors = scraper.similar_analyze('com.myapp', count=10)
   
   print(f"My App: {my_app['score']}/5")
   print("\nCompetitors:")
   for comp in competitors:
       print(f"  {comp['title']}: {comp['score']}/5")
