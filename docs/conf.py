# Configuration file for Sphinx documentation builder

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'GPlay Scraper'
copyright = '2025, Mohammed Cha'
author = 'Mohammed Cha'
release = '1.0.2'

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

# Templates path
templates_path = ['_templates']

# Exclude patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# HTML theme options
html_theme_options = {
    'canonical_url': 'https://mohammedcha.github.io/gplay-scraper/',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# GitHub Pages configuration
html_baseurl = 'https://mohammedcha.github.io/gplay-scraper/'
html_context = {
    'display_github': True,
    'github_user': 'mohammedcha',
    'github_repo': 'gplay-scraper',
    'github_version': 'main',
    'conf_py_path': '/docs/',
}

# Napoleon settings (for Google/NumPy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'curl_cffi': ('https://curl-cffi.readthedocs.io/en/latest/', None),
}
