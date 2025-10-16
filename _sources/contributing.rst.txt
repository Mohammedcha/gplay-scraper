Contributing
============

Thank you for your interest in contributing to GPlay Scraper!

Development Setup
-----------------

1. Fork the repository on GitHub
2. Clone your fork locally:

   .. code-block:: bash

      git clone https://github.com/yourusername/gplay-scraper.git
      cd gplay-scraper

3. Install in development mode:

   .. code-block:: bash

      pip install -e .

4. Install development dependencies:

   .. code-block:: bash

      pip install pytest sphinx sphinx-rtd-theme

Running Tests
-------------

Run the test suite:

.. code-block:: bash

   python -m pytest tests/ -v

Run tests with coverage:

.. code-block:: bash

   python -m pytest tests/ -v --cov=gplay_scraper

Code Style
----------

- Follow PEP 8 style guidelines
- Add docstrings to new functions and classes
- Include type hints where appropriate
- Write descriptive commit messages

Documentation
-------------

Build documentation locally:

.. code-block:: bash

   python build_docs.py

The documentation will be available at ``docs/_build/html/index.html``.

Submitting Changes
------------------

1. Create a feature branch:

   .. code-block:: bash

      git checkout -b feature-name

2. Make your changes
3. Add tests for new functionality
4. Run tests to ensure they pass
5. Update documentation if needed
6. Commit your changes:

   .. code-block:: bash

      git commit -m "Add feature: description"

7. Push to your fork:

   .. code-block:: bash

      git push origin feature-name

8. Submit a pull request on GitHub

Reporting Issues
----------------

Please use GitHub Issues to report bugs or request features. Include:

- Python version
- Operating system
- Steps to reproduce the issue
- Expected vs actual behavior
- Error messages (if any)

Code of Conduct
---------------

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the project's coding standards

Thank you for contributing! 🚀