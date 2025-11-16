Suggest Methods
===============

Get search suggestions and autocomplete.

Overview
--------

The Suggest methods provide search suggestions, returning lists of strings.

suggest_analyze()
-----------------

Get search suggestions for a term.

**Signature:**

.. code-block:: python

   suggest_analyze(term, count=5, lang='en', country='')

**Example:**

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   suggestions = scraper.suggest_analyze('mine', count=10)
   
   print(suggestions)
   # ['minecraft', 'minesweeper', 'mineplex', ...]

suggest_nested()
----------------

Get nested suggestions (suggestions for suggestions).

**Signature:**

.. code-block:: python

   suggest_nested(term, count=5, lang='en', country='')

**Returns:**

Dictionary mapping terms to their suggestion lists

**Example:**

.. code-block:: python

   nested = scraper.suggest_nested('game', count=5)
   
   for term, suggestions in nested.items():
       print(f"\n{term}:")
       for suggestion in suggestions:
           print(f"  - {suggestion}")

Common Use Cases
----------------

Keyword Research
^^^^^^^^^^^^^^^^

.. code-block:: python

   # Find popular search terms
   keywords = ['fitness', 'photo', 'music']
   
   for keyword in keywords:
       suggestions = scraper.suggest_analyze(keyword, count=10)
       print(f"\n{keyword} suggestions:")
       for s in suggestions:
           print(f"  {s}")

Trend Discovery
^^^^^^^^^^^^^^^

.. code-block:: python

   # Discover trending topics
   term = "ai"
   suggestions = scraper.suggest_analyze(term, count=20)
   
   print(f"Popular '{term}' searches:")
   for suggestion in suggestions:
       print(f"  {suggestion}")
