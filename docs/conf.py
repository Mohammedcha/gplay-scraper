project = 'GPlay Scraper'
copyright = '2025, GPlay Scraper'
author = 'GPlay Scraper'
release = '1.0.5'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

try:
    import sphinx_copybutton
    extensions.append('sphinx_copybutton')
except ImportError:
    pass

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'en'

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "repository_url": "https://github.com/mohammedcha/gplay-scraper",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": False,
    "use_download_button": True,
    "home_page_in_toc": True,
    "show_navbar_depth": 2,
    "show_toc_level": 2,
    "navigation_with_keys": True,
    "collapse_navbar": False,
    "logo": {
        "text": "GPlay Scraper",
    },
    "extra_footer": "<p>Built with ❤️ using Sphinx Book Theme</p>",
    "search_bar_text": "Search documentation...",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/mohammedcha/gplay-scraper",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/gplay-scraper/",
            "icon": "fa-brands fa-python",
            "type": "fontawesome",
        },
    ],
}

pygments_style = 'monokai'
pygments_dark_style = 'monokai'

html_title = "GPlay Scraper"
html_static_path = ['_static']

html_logo = "_static/logo.png"
html_favicon = "_static/favicon.png"

if 'sphinx_copybutton' in extensions:
    copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
    copybutton_prompt_is_regexp = True
