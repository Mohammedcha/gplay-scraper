from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="gplay-scraper",
    version="1.0.2",
    description="Powerful Python Google Play scraper library for extracting comprehensive app data from Google Play Store - ratings, installs, reviews, ASO metrics, and 65+ fields.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mohammed Cha",
    url="https://github.com/mohammedcha/gplay-scraper",
    project_urls={
        "Bug Reports": "https://github.com/mohammedcha/gplay-scraper/issues",
        "Source": "https://github.com/mohammedcha/gplay-scraper",
        "Documentation": "https://mohammedcha.github.io/gplay-scraper/",
    },
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
    keywords="google play scraper, playstore scraper, python google play, app store scraper, google play api, aso tools, app analytics, mobile app data, android scraper, play store data",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",

        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    include_package_data=True,
    zip_safe=False,
)
