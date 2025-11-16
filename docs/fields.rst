Field Reference
===============

Complete reference of all 112 fields returned by GPlay Scraper.

App Fields (57 Fields)
-----------------------

Basic Information (5 fields)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``appId`` (string) - Package identifier (e.g., "com.whatsapp")
* ``title`` (string) - App name
* ``summary`` (string) - Short description
* ``description`` (string) - Full description
* ``appUrl`` (string) - Play Store URL

Category (4 fields)
^^^^^^^^^^^^^^^^^^^

* ``genre`` (string) - Primary category
* ``genreId`` (string) - Category ID
* ``categories`` (array) - All categories
* ``available`` (boolean) - Availability status

Release & Updates (3 fields)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``released`` (string) - Release date (e.g., "Oct 18, 2010")
* ``appAgeDays`` (integer) - Days since release (computed)
* ``lastUpdated`` (string) - Last update date

Media (5 fields)
^^^^^^^^^^^^^^^^

* ``icon`` (string) - App icon URL
* ``headerImage`` (string) - Header image URL
* ``screenshots`` (array) - Screenshot URLs
* ``video`` (string or null) - Promotional video URL
* ``videoImage`` (string or null) - Video thumbnail URL

Install Statistics (10 fields)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``installs`` (string) - Install range (e.g., "10,000,000,000+")
* ``minInstalls`` (integer) - Minimum installs
* ``realInstalls`` (integer) - Exact install count
* ``dailyInstalls`` (integer) - Average daily installs (computed)
* ``minDailyInstalls`` (integer) - Min daily installs (computed)
* ``realDailyInstalls`` (integer) - Real daily installs (computed)
* ``monthlyInstalls`` (integer) - Average monthly installs (computed)
* ``minMonthlyInstalls`` (integer) - Min monthly installs (computed)
* ``realMonthlyInstalls`` (integer) - Real monthly installs (computed)

Ratings (4 fields)
^^^^^^^^^^^^^^^^^^

* ``score`` (float) - Average rating (0-5)
* ``ratings`` (integer) - Total ratings count
* ``reviews`` (integer) - Total reviews count
* ``histogram`` (array) - Rating distribution [1★, 2★, 3★, 4★, 5★]

Ads (2 fields)
^^^^^^^^^^^^^^

* ``adSupported`` (boolean) - Supports ads
* ``containsAds`` (boolean) - Contains ads

Technical (7 fields)
^^^^^^^^^^^^^^^^^^^^

* ``version`` (string) - Current version
* ``androidVersion`` (string) - Minimum Android version
* ``maxAndroidApi`` (integer) - Maximum Android API
* ``minAndroidApi`` (string or integer) - Minimum Android API
* ``appBundle`` (string) - Bundle identifier
* ``contentRating`` (string) - Age rating
* ``contentRatingDescription`` (string) - Rating description

Updates (1 field)
^^^^^^^^^^^^^^^^^

* ``whatsNew`` (array) - Changelog entries

Privacy (2 fields)
^^^^^^^^^^^^^^^^^^

* ``permissions`` (object) - Required permissions
* ``dataSafety`` (array) - Data safety information

Pricing (7 fields)
^^^^^^^^^^^^^^^^^^

* ``price`` (number) - App price
* ``currency`` (string) - Currency code
* ``free`` (boolean) - Is free
* ``offersIAP`` (boolean) - Has in-app purchases
* ``inAppProductPrice`` (string or null) - IAP price range
* ``sale`` (boolean) - On sale
* ``originalPrice`` (number or null) - Original price if on sale

Developer (8 fields)
^^^^^^^^^^^^^^^^^^^^

* ``developer`` (string) - Developer name
* ``developerId`` (string) - Developer ID
* ``developerEmail`` (string) - Contact email
* ``developerWebsite`` (string) - Website URL
* ``developerAddress`` (string) - Physical address
* ``developerPhone`` (string or null) - Contact phone
* ``publisherCountry`` (string) - Publisher country (computed)
* ``privacyPolicy`` (string) - Privacy policy URL

Search Fields (11 Fields)
--------------------------

* ``title`` - App name
* ``appId`` - Package identifier
* ``url`` - Play Store URL
* ``icon`` - App icon URL
* ``developer`` - Developer name
* ``summary`` - Short description
* ``score`` - Average rating (0-5)
* ``scoreText`` - Rating as text
* ``price`` - App price
* ``free`` - Is free (boolean)
* ``currency`` - Currency code

Review Fields (8 Fields)
-------------------------

* ``reviewId`` - Unique review ID
* ``userName`` - Reviewer name
* ``userImage`` - Reviewer image URL
* ``content`` - Review text
* ``score`` - Rating (1-5)
* ``thumbsUpCount`` - Helpful votes
* ``at`` - Review date (ISO format)
* ``appVersion`` - App version reviewed

Developer App Fields (11 Fields)
---------------------------------

Same as Search Fields.

Similar App Fields (11 Fields)
-------------------------------

Same as Search Fields.

List (Top Charts) Fields (14 Fields)
-------------------------------------

* ``title`` - App name
* ``appId`` - Package identifier
* ``url`` - Play Store URL
* ``icon`` - App icon URL
* ``screenshots`` - Screenshot URLs (array)
* ``developer`` - Developer name
* ``genre`` - Category/genre
* ``installs`` - Install count
* ``description`` - App description
* ``score`` - Average rating
* ``scoreText`` - Rating as text
* ``price`` - App price
* ``free`` - Is free (boolean)
* ``currency`` - Currency code

Computed Fields
---------------

The following 8 fields are computed at runtime:

**appAgeDays**
   Calculated as: ``(current_date - release_date).days``

**dailyInstalls**
   Calculated as: ``total_installs / days_since_release``

**minDailyInstalls**
   Calculated as: ``min_installs / days_since_release``

**realDailyInstalls**
   Calculated as: ``real_installs / days_since_release``

**monthlyInstalls**
   Calculated as: ``total_installs / (days_since_release / 30.44)``

**minMonthlyInstalls**
   Calculated as: ``min_installs / months_since_release``

**realMonthlyInstalls**
   Calculated as: ``real_installs / months_since_release``

**publisherCountry**
   Extracted from developer phone prefix or address

Field Count Summary
-------------------

* App: 57 fields
* Search: 11 fields
* Reviews: 8 fields
* Developer: 11 fields
* Similar: 11 fields
* List: 14 fields
* **Total: 112 unique fields**
