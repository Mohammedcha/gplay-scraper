# GPlay Scraper Documentation

## Build Documentation

```bash
pip install -r requirements.txt
cd docs
sphinx-build -b html . _build/html
```

## Open Documentation

```bash
start _build/html/index.html  # Windows
open _build/html/index.html   # Mac
xdg-open _build/html/index.html  # Linux
```

## Live Reload

```bash
pip install sphinx-autobuild
sphinx-autobuild . _build/html
```
