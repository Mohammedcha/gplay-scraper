Reviews Methods
===============

Extract user reviews and ratings with sorting options.

Overview
--------

The Reviews methods allow you to get user reviews with 8 fields per review, including content, rating, and metadata.

Available Methods
-----------------

* ``reviews_analyze()`` - Get all reviews
* ``reviews_get_field()`` - Get single field from all reviews
* ``reviews_get_fields()`` - Get multiple fields from all reviews
* ``reviews_print_field()`` - Print single field
* ``reviews_print_fields()`` - Print multiple fields
* ``reviews_print_all()`` - Print all reviews as JSON

reviews_analyze()
-----------------

Get user reviews with all details.

**Signature:**

.. code-block:: python

   reviews_analyze(app_id, count=100, sort='NEWEST', lang='en', country='')

**Parameters:**

* ``app_id`` (str, required) - Google Play app ID
* ``count`` (int, optional) - Number of reviews (default: 100, max: ~1000+)
* ``sort`` (str, optional) - Sort order: 'NEWEST', 'RELEVANT', 'RATING' (default: 'NEWEST')
* ``lang`` (str, optional) - Language code
* ``country`` (str, optional) - Country code

**Returns:**

List of dictionaries, each with 8 fields

**Example:**

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   
   # Get newest reviews
   reviews = scraper.reviews_analyze('com.whatsapp', count=50, sort='NEWEST')
   
   for review in reviews:
       print(f"{review['userName']}: {review['score']}/5")
       print(f"Date: {review['at']}")
       print(f"Content: {review['content'][:100]}...")
       print(f"Helpful: {review['thumbsUpCount']} people")

Sort Options
^^^^^^^^^^^^

* **NEWEST** - Most recent reviews first (default)
* **RELEVANT** - Most helpful/relevant reviews
* **RATING** - Sorted by rating score

.. code-block:: python

   # Get most relevant reviews
   reviews = scraper.reviews_analyze('com.whatsapp', 
       count=100, 
       sort='RELEVANT')
   
   # Get reviews sorted by rating
   reviews = scraper.reviews_analyze('com.whatsapp', 
       count=100, 
       sort='RATING')

reviews_get_field()
-------------------

Get single field from all reviews.

**Example:**

.. code-block:: python

   scraper = GPlayScraper()
   
   # Get all usernames
   usernames = scraper.reviews_get_field('com.whatsapp', 'userName', count=10)
   
   # Get all scores
   scores = scraper.reviews_get_field('com.whatsapp', 'score', count=100)

reviews_get_fields()
--------------------

Get multiple fields from all reviews.

**Example:**

.. code-block:: python

   fields = ['userName', 'score', 'content', 'thumbsUpCount']
   reviews = scraper.reviews_get_fields('com.whatsapp', fields, count=50)

Available Fields
----------------

Each review contains 8 fields:

* ``reviewId`` - Unique review identifier
* ``userName`` - Reviewer's name
* ``userImage`` - Reviewer's profile image URL
* ``content`` - Review text
* ``score`` - Rating (1-5)
* ``thumbsUpCount`` - Number of helpful votes
* ``at`` - Review date (ISO format)
* ``appVersion`` - App version reviewed

Common Use Cases
----------------

Monitor Negative Reviews
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   scraper = GPlayScraper()
   
   reviews = scraper.reviews_analyze('com.myapp', count=100, sort='NEWEST')
   negative = [r for r in reviews if r['score'] <= 2]
   
   print(f"Found {len(negative)} negative reviews")
   for review in negative:
       print(f"{review['userName']}: {review['score']}/5")
       print(f"  {review['content']}")

Sentiment Analysis
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   reviews = scraper.reviews_analyze('com.whatsapp', count=500)
   
   # Count by rating
   rating_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
   for review in reviews:
       rating_counts[review['score']] += 1
   
   print("Rating distribution:")
   for rating, count in rating_counts.items():
       print(f"  {rating}★: {count} reviews")

Find Helpful Reviews
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   reviews = scraper.reviews_analyze('com.whatsapp', 
       count=100, 
       sort='RELEVANT')
   
   # Get most helpful
   most_helpful = sorted(reviews, 
       key=lambda x: x['thumbsUpCount'], 
       reverse=True)[:10]
   
   for review in most_helpful:
       print(f"{review['thumbsUpCount']} helpful votes")
       print(f"  {review['content'][:100]}...")

Track Version Feedback
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   reviews = scraper.reviews_analyze('com.myapp', count=200)
   
   # Group by app version
   by_version = {}
   for review in reviews:
       version = review['appVersion']
       if version not in by_version:
           by_version[version] = []
       by_version[version].append(review)
   
   # Analyze each version
   for version, version_reviews in by_version.items():
       avg_score = sum(r['score'] for r in version_reviews) / len(version_reviews)
       print(f"Version {version}: {avg_score:.2f}/5 ({len(version_reviews)} reviews)")

See Also
--------

* :doc:`app` - Get app information
* :doc:`../examples` - More examples
