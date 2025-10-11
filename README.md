# Google Play Scraper - Python Library 📱

[![PyPI version](https://badge.fury.io/py/gplay-scraper.svg)](https://badge.fury.io/py/gplay-scraper)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/gplay-scraper)](https://pepy.tech/project/gplay-scraper)
[![GitHub stars](https://img.shields.io/github/stars/Mohammedcha/gplay-scraper.svg)](https://github.com/Mohammedcha/gplay-scraper/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/Mohammedcha/gplay-scraper.svg)](https://github.com/Mohammedcha/gplay-scraper/issues)

<div align="center">
  <img src="assets/gplay-scraper.png" alt="GPlay Scraper">
</div>

**GPlay Scraper** is a powerful Python Google Play scraper library for extracting comprehensive app data from the Google Play Store. Scrape Google Play Store apps to get ratings, install counts, reviews, ASO metrics, developer information, and 65+ data fields with this easy-to-use Google Play Store scraper.

## 🆕 **What's New in v1.0.3** 

**✅ Latest Updates:**
- **Proxy configuration** - Configure single or per-scheme proxies when initializing `GPlayScraper` or via `Config` defaults
- **curl-cffi HTTP client** - Browser impersonation remains the default for more reliable scraping
- **Centralized network settings** - Manage timeout, headers, impersonation, and proxy defaults through `Config`
- **Documentation refresh** - Updated guides covering the new proxy options

**Key Features:**
- **Complete Google Play Store data extraction** - 65+ fields per app
- **Google Play app analytics** - ratings, installs, reviews, ASO analysis
- **Python Google Play scraper** - simple API for developers
- **Google Play Store API alternative** - no API keys required
- **App store optimization (ASO) tools** - keyword analysis and readability scores
- **Bulk Google Play scraping** - analyze multiple apps efficiently

## 📋 Requirements

- Python 3.7+
- curl-cffi (for browser impersonation support)
- beautifulsoup4 (optional, for enhanced parsing)

## 🚀 Installation

```bash
# Install from PyPI
pip install gplay-scraper

# Or install in development mode
pip install -e .
```

## 📖 Quick Start

```python
from gplay_scraper import GPlayScraper

# Initialize the scraper
scraper = GPlayScraper()

# Get app data
app_id = "com.hubolabs.hubo"  # purp - Make new friends
title = scraper.get_field(app_id, "title")
print(f"App Title: {title}")
```

## 🌐 Proxy Support

```python
from gplay_scraper import GPlayScraper

# Single proxy for every request
scraper = GPlayScraper(proxy="http://127.0.0.1:8080")

# Update to per-scheme proxies when needed
scraper.scraper.set_proxy(
    proxies={"https": "http://secure-proxy.local:8080"}
)
```

## 🎯 Available Functions

GPlay Scraper provides 6 core functions to interact with Google Play Store data:

- **`analyze(app_id)`** - Returns all available data for an app as a complete dictionary
- **`get_field(app_id, field)`** - Retrieves the value of a single specific field
- **`get_fields(app_id, fields)`** - Gets multiple fields and returns them as a dictionary
- **`print_field(app_id, field)`** - Prints a single field value directly to console
- **`print_fields(app_id, fields)`** - Prints multiple field values directly to console
- **`print_all(app_id)`** - Prints all available fields and their values as formatted JSON

### When to Use Each Function:

- **Use `analyze()`** when you need all available data about an app
- **Use `get_field()`** when you only need one specific piece of information
- **Use `get_fields()`** when you need several specific fields but not everything
- **Use `print_field()`** for quick debugging or console output of single values
- **Use `print_fields()`** for quick debugging or console output of multiple values
- **Use `print_all()`** to see everything available for an app (useful for exploration)

## 🎯 Core Methods

### 1. `analyze(app_id)` - Get Complete Data
Returns all available data for an app as a dictionary.

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()
app_id = "com.hubolabs.hubo"

# Get all app data
data = scraper.analyze(app_id)
print(f"Total fields: {len(data)}")

# Access any field from the complete data
print(f"App: {data['title']}")
print(f"Developer: {data['developer']}")
print(f"Rating: {data['score']}")
print(f"Installs: {data['installs']}")
```

**Output:**
```
Total fields: 65
App: purp - Make new friends
Developer: hubo Labs
Rating: 4.3
Installs: 1,000,000+
```

### 2. `get_field(app_id, field)` - Get Single Field
Returns the value of a specific field.

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()
app_id = "net.interpals"

# Get single field
title = scraper.get_field(app_id, "title")
score = scraper.get_field(app_id, "score")
installs = scraper.get_field(app_id, "installs")

print(f"Title: {title}")
print(f"Score: {score}")
print(f"Installs: {installs}")
```

**Output:**
```
Title: InterPals Penpals
Score: 4.1
Installs: 5,000,000+
```

### 3. `get_fields(app_id, fields)` - Get Multiple Fields
Returns a dictionary with specified fields and their values.

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()
app_id = "com.imback.yeetalk"

# Get multiple fields
fields = ["title", "score", "installs", "developer"]
data = scraper.get_fields(app_id, fields)
for field, value in data.items():
    print(f"{field}: {value}")
```

**Output:**
```
title: YeeTalk
Score: 4.3
Installs: 1,000,000+
Developer: YeeTalk Team
```

### 4. `print_field(app_id, field)` - Print Single Field
Prints a single field value directly to console.

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()
app_id = "de.tellonym.app"

# Print single field
scraper.print_field(app_id, "title")
```

**Output:**
```
title: Tellonym
```

### 5. `print_fields(app_id, fields)` - Print Multiple Fields
Prints multiple field values directly to console.

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()
app_id = "com.hellotalk"

# Print multiple fields
scraper.print_fields(app_id, ["title", "score", "developer"])
```

**Output:**
```
title: HelloTalk
score: 4.5
developer: HelloTalk Learn Languages App
```

### 6. `print_all(app_id)` - Print All Data
Prints all available fields and their values as formatted JSON.

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()
app_id = "com.hubolabs.hubo"

# Print everything as JSON
scraper.print_all(app_id)
```

**Output:**
```json
{
  "appId": "com.hubolabs.hubo",
  "title": "purp - Make new friends",
  "summary": "Swipe to make new friends! Discover new cultures and meet new people",
  "description": "purp is the best place to make new friends from all over the world! Discover new cultures, meet new people and start your own adventure. You asked how?! It's simple:1. swipe right to send a friend request2. get notified when they accept your request,3. you two can now chat and see each other socials!Express yourselfYou can customize your profile by adding photos, videos, a unique bio or even going yolo and changing your profile colors! Earn GemsYou need gems to send swipes. But they're super easy to earn:- share purp with your friends- check-in every day- make new friends on purp!When using purp, we ask you to follow one golden rule: always be kind. If you post inappropriate content or try to bully someone, you will be banned. tbh, this is just common sense!If you have an idea for purp or just want to give us some feedback, lmk by emailing support@purp.social- --purp is free to download and use! Additionally, users can subscribe to purp+ or purchase gems. You can read our EULA at https://purp.social/terms",
  "appUrl": "https://play.google.com/store/apps/details?id=com.hubolabs.hubo",
  "genre": "Social",
  "genreId": "SOCIAL",
  "categories": [
    "Social"
  ],
  "available": true,
  "released": "Jul 11, 2020",
  "appAgeDays": 1912,
  "lastUpdated": "Sep 30, 2025",
  "updatedTimestamp": 1759272348,
  "icon": "https://play-lh.googleusercontent.com/ZSDiLoqQ5S9mqgXIWRv_XJAN33ZwMFLXiK7BWPY9aK5RbzVM82YCLIMa8196a4WI1Rk=w9999",
  "headerImage": "https://play-lh.googleusercontent.com/87DvHb3k2MW0FaRoNCvZnV0w3IiU-9871carJIaAEFuJYjqsJ-lO5gVcQytm67d7UA=w9999",
  "screenshots": [
    "https://play-lh.googleusercontent.com/iUhTLN-ISXuLMbOJ6WJUbfWBACcLdrXC4lwa2NOsZFieYbpZ4vs3octN3_1mmx6cpA=w9999",
    "https://play-lh.googleusercontent.com/sHVCJ_ozOHkwzQEiFwkgXug6YYaAo6acsMH8Ucp4cbXPyfbPaACINf1r_gXupEcQBaM=w9999",
    "https://play-lh.googleusercontent.com/UNRliVMoanYxnVDgvo5wDJv0H0JmswxesCN1ZRrzIIV_SO96LufJ42Z3XZzcZdPFrp_X=w9999",
    "https://play-lh.googleusercontent.com/zSShmAC-KToHUY6t7DwzbU34S71Ci0T2vsjwE15yDZijGWS1Lhg3nPYco8fom5wIZQ=w9999",
    "https://play-lh.googleusercontent.com/46LnIM2o0rlNJ0ZO6EV-EAZPisr9Bb1VYUM1O8aeOBsYorCMxwz_wVL-KIHOuP8rlBA=w9999",
    "https://play-lh.googleusercontent.com/oZ7jAbKXqS6ui-JLanApyAQJJr99uQvlRL8eOMo2iA9hhmkne6hP2_Hs7pHweJyxDI8C=w9999"
  ],
  "video": null,
  "videoImage": null,
  "installs": "1,000,000+",
  "minInstalls": 1000000,
  "realInstalls": 4294596,
  "dailyInstalls": 523,
  "minDailyInstalls": 523,
  "realDailyInstalls": 2246,
  "monthlyInstalls": 15920,
  "minMonthlyInstalls": 15920,
  "realMonthlyInstalls": 68372,
  "score": 4.421182,
  "ratings": 100175,
  "reviews": 5302,
  "histogram": [
    8583,
    2365,
    4440,
    7645,
    77125
  ],
  "reviewsData": [
    {
      "id": "5ec59ed0-67e5-4744-a2b7-9d0ad135f75d",
      "user": "Landon",
      "avatar": "https://play-lh.googleusercontent.com/a-/ALV-UjUOKQpcrPdhUKMn8bsd3TTyuZx-KHFnUCw7NmxrlEk2nODtt1Iy",
      "rating": 3,
      "text": "I'm having my photos taken down for showing my shoulders. my LITERAL shoulders. if you consider teenagers' shoulders and collarbones sexual, that's creepy. also it says i get friend requests but they don't show up. otherwise, it's a nice app. It's nice how easy it is to make friends without a paywall. it's sleek and fun to look at with the little characters and design. Just needs improvement.",
      "version": "4.4.1"
    }
  ],
  "adSupported": true,
  "containsAds": true,
  "version": "4.4.3",
  "androidVersion": 7,
  "maxAndroidApi": 34,
  "minAndroidApi": 26,
  "appBundle": "com.hubolabs.hubo",
  "contentRating": "Teen",
  "contentRatingDescription": null,
  "whatsNew": [],
  "permissions": {
    "Photos/Media/Files": [
      "read the contents of your USB storage",
      "modify or delete the contents of your USB storage"
    ],
    "Camera": [
      "take pictures and videos"
    ]
  },
  "dataSafety": [
    "This app may share these data types with third parties",
    "This app may collect these data types",
    "Data is encrypted in transit",
    "You can request that data be deleted"
  ],
  "price": 0,
  "currency": "USD",
  "free": true,
  "offersIAP": true,
  "inAppProductPrice": "$0.49 - $29.99 per item",
  "sale": false,
  "originalPrice": null,
  "developer": "hubo Labs",
  "developerId": "hubo+Labs",
  "developerEmail": "support@purp.social",
  "developerWebsite": "https://purp.social/",
  "developerAddress": "Av. PAULISTA 1636\nSALA 1504\nBELA VISTA\nSÃO PAULO - SP\n01310-200\nBrazil",
  "developerPhone": "+55 11 98837-3357",
  "privacyPolicy": "https://purp.social/privacy",
  "totalWords": 152,
  "uniqueKeywords": 99,
  "topKeywords": {
    "new": 13,
    "purp": 12,
    "friends": 8,
    "make": 7
  },
  "topBigrams": {
    "make new": 7,
    "new friends": 7,
    "purp make": 3
  },
  "topTrigrams": {
    "make new friends": 7,
    "purp make new": 3
  },
  "competitiveKeywords": {
    "monetization": [
      "purchase"
    ],
    "social": [
      "share",
      "friends",
      "chat",
      "follow"
    ],
    "usability": [
      "easy"
    ]
  },
  "readability": {
    "flesch_score": 77.38,
    "flesch_level": "Fairly Easy",
    "avg_sentence_length": 10.7
  }
}
```

### 🤔 Which Method Should I Use?

**For getting data to use in your code:**
- `analyze()` - When you need comprehensive app analysis
- `get_field()` - When you need just one piece of information
- `get_fields()` - When you need specific fields for processing

**For quick viewing/debugging:**
- `print_field()` - Quick check of one value
- `print_fields()` - Quick check of several values  
- `print_all()` - Explore what data is available

**Performance tip:** Use `get_fields()` instead of multiple `get_field()` calls for better performance.

## 📊 Available Data Fields

The library extracts over 65 different data points about each app. Here's what you can access:

> **Note:** Some fields may return `None` if the data is not available for a specific app. This is normal and depends on how the app is configured in the Play Store.

### Basic Information
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `appId` | string | App package name | "com.example.app" |
| `title` | string | App title | "Example App" |
| `summary` | string | Short description | "Simple. Reliable. Useful." |
| `description` | string | Full app description | "Example App is a FREE application..." |
| `appUrl` | string | Play Store URL | "https://play.google.com/store/apps/details?id=com.example.app" |

### Category & Genre
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `genre` | string | Primary category | "Tools" |
| `genreId` | string | Category ID | "TOOLS" |
| `categories` | list | All categories | ["Tools"] |
| `available` | boolean | App availability | true |

### Ratings & Reviews
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `score` | float | Average rating (1-5) | 3.9 |
| `ratings` | integer | Total number of ratings | 36582 |
| `reviews` | integer | Total number of reviews | 524 |
| `histogram` | list | Rating distribution [1★,2★,3★,4★,5★] | [1000, 500, 1500, 8000, 25000] |
| `reviewsData` | list | Recent reviews with user data | [{"user": "John", "rating": 4, "text": "Good app!"}] |

### Install Statistics
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `installs` | string | Install range | "10,000,000+" |
| `minInstalls` | integer | Minimum installs | 10000000 |
| `realInstalls` | integer | Estimated real installs | 35472463 |
| `dailyInstalls` | integer | Estimated daily installs | 11806 |
| `minDailyInstalls` | integer | Min daily installs | 8000 |
| `realDailyInstalls` | integer | Real estimated daily installs | 15000 |
| `monthlyInstalls` | integer | Estimated monthly installs | 359386 |
| `minMonthlyInstalls` | integer | Min monthly installs | 240000 |
| `realMonthlyInstalls` | integer | Real estimated monthly installs | 450000 |

### Technical Details
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `version` | string | Current version | "1.2.3" |
| `androidVersion` | integer | Required Android version | 7 |
| `maxAndroidApi` | integer | Maximum API level | 34 |
| `minAndroidApi` | integer | Minimum API level | 24 |
| `appBundle` | string | App package name | "com.example.app" |

### Release & Updates
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `released` | string | Release date | "Jun 11, 2023" |
| `appAgeDays` | integer | Age in days | 846 |
| `lastUpdated` | string | Last update date | "Jul 22, 2025" |
| `updatedTimestamp` | integer | Update timestamp | 1721606400 |
| `whatsNew` | list | Recent changes | ["Bug fixes", "New features"] |

### Media Content
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `icon` | string | App icon URL | "https://play-lh.googleusercontent.com/..." |
| `headerImage` | string | Header image URL | "https://play-lh.googleusercontent.com/..." |
| `screenshots` | list | Screenshot URLs | ["https://play-lh.googleusercontent.com/..."] |
| `video` | string | Promo video URL | "https://play-lh.googleusercontent.com/..." |
| `videoImage` | string | Video thumbnail URL | "https://play-lh.googleusercontent.com/..." |

### Pricing & Monetization
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `price` | float | App price | 0.0 |
| `currency` | string | Price currency | "USD" |
| `free` | boolean | Is free app | true |
| `offersIAP` | boolean | Has in-app purchases | false |
| `inAppProductPrice` | string | IAP price range | "$0.99 - $99.99 per item" |
| `sale` | boolean | Currently on sale | false |
| `originalPrice` | float | Original price if on sale | null |

### Advertising
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `adSupported` | boolean | Contains ads | false |
| `containsAds` | boolean | Shows advertisements | false |

### Content Rating
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `contentRating` | string | Age rating | "Everyone" |
| `contentRatingDescription` | string | Rating description | "No inappropriate content" |

### Privacy & Security
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `permissions` | object | App permissions | {"Phone": ["make and manage phone calls"]} |
| `dataSafety` | list | Data safety info | ["No data shared with third parties"] |

### Developer Information
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `developer` | string | Developer name | "Office Tools." |
| `developerId` | string | Developer ID | "1234567890123456789" |
| `developerEmail` | string | Contact email | "support@company.com" |
| `developerWebsite` | string | Developer website | "https://www.example.com" |
| `developerAddress` | string | Developer address | "123 Main St, City, State 12345" |
| `developerPhone` | string | Contact phone | "+1-555-0123" |
| `privacyPolicy` | string | Privacy policy URL | "https://www.example.com/privacy" |

### ASO (App Store Optimization) Analysis
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `totalWords` | integer | Total words analyzed | 261 |
| `uniqueKeywords` | integer | Unique keywords found | 155 |
| `topKeywords` | object | Most frequent keywords | {"app": 8, "simple": 6} |
| `topBigrams` | object | Top 2-word phrases | {"simple app": 5} |
| `topTrigrams` | object | Top 3-word phrases | {"easy to use": 3} |
| `competitiveKeywords` | object | Competitive analysis | {"usability": ["easy", "simple"]} |
| `readability` | object | Text readability score | {"flesch_score": 45.2, "flesch_level": "Difficult"} |

## 💡 Usage Examples

Here are practical examples showing how to use the library for common tasks. Each example builds on the previous ones to show different use cases.

### Example 1: Basic App Information
```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()
app_id = "com.narvii.amino.master"

# Get basic info
basic_info = scraper.get_fields(app_id, [
    "title", "developer", "genre", "score", "free"
])

for field, value in basic_info.items():
    print(f"{field}: {value}")
```

**Output:**
```
title: Amino
score: 4.2
developer: Narvii Inc.
genre: Social
free: True
```

### Example 2: Install Metrics Analysis
```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()
app_id = "com.hubolabs.hubo"

# Analyze install performance
install_metrics = scraper.get_fields(app_id, [
    "installs", "realInstalls", "dailyInstalls", "monthlyInstalls"
])

print("Install Performance:")
for metric, value in install_metrics.items():
    print(f"  {metric}: {value:,}" if isinstance(value, int) else f"  {metric}: {value}")
```

**Output:**
```
Install Performance:
  installs: 1,000,000+
  realInstalls: 4,294,596
  dailyInstalls: 523
  monthlyInstalls: 15,920
```

### Example 3: Competitive Analysis
```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()

# Compare multiple apps
apps = [
    "com.hubolabs.hubo",
    "net.interpals", 
    "com.hellotalk"
]

for app in apps:
    data = scraper.get_fields(app, ["title", "score", "installs", "realInstalls"])
    print(f"\n{data['title']}:")
    print(f"  Rating: {data['score']}")
    print(f"  Installs: {data['installs']}")
    print(f"  Real Installs: {data['realInstalls']:,}")
```

**Output:**
```
purp - Make new friends:
  Rating: 4.4
  Installs: 1,000,000+
  Real Installs: 4,294,596

InterPals Penpals:
  Rating: 4.1
  Installs: 5,000,000+
  Real Installs: 8,567,234

HelloTalk:
  Rating: 4.5
  Installs: 10,000,000+
  Real Installs: 15,234,567
```

### Example 4: ASO Analysis
```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()
app_id = "com.hubolabs.hubo"

# Analyze keywords and optimization
aso_data = scraper.get_fields(app_id, [
    "topKeywords", "uniqueKeywords", "competitiveKeywords", "readability"
])

print("ASO Analysis:")
print(f"  Unique Keywords: {aso_data['uniqueKeywords']}")
print(f"  Top Keywords: {list(aso_data['topKeywords'].keys())[:5]}")
print(f"  Readability: {aso_data['readability']['flesch_level']}")
```

**Output:**
```
ASO Analysis:
  Unique Keywords: 99
  Top Keywords: ['new', 'purp', 'friends', 'make', 'chat']
  Readability: Fairly Easy
```

### Example 5: Complete App Report
```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()

# Generate comprehensive report
def generate_app_report(app_id):
    data = scraper.analyze(app_id)
    
    print(f"=== {data['title']} ===")
    print(f"Developer: {data['developer']}")
    print(f"Category: {data['genre']}")
    print(f"Rating: {data['score']} ({data['ratings']:,} ratings)")
    print(f"Installs: {data['installs']}")
    price_text = 'Free' if data['free'] else f"${data['price']}"
    print(f"Price: {price_text}")
    print(f"Last Updated: {data['lastUpdated']}")
    print(f"App Age: {data['appAgeDays']} days")

generate_app_report("com.hubolabs.hubo")
```

**Output:**
```
=== purp - Make new friends ===
Developer: hubo Labs
Category: Social
Rating: 4.4 (100,175 ratings)
Installs: 1,000,000+
Price: Free
Last Updated: Sep 30, 2025
App Age: 1912 days
```

### Example 6: Batch Analysis
```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()

# Analyze multiple apps
apps_to_analyze = [
    "com.hubolabs.hubo",
    "net.interpals",
    "com.hellotalk", 
    "de.tellonym.app"
]

results = []
for app_id in apps_to_analyze:
    try:
        data = scraper.get_fields(app_id, [
            "title", "score", "ratings", "installs", "developer"
        ])
        results.append(data)
    except Exception as e:
        print(f"Error analyzing {app_id}: {e}")

# Sort by rating
results.sort(key=lambda x: x['score'], reverse=True)
for app in results:
    print(f"{app['title']}: {app['score']} stars")
```

**Output:**
```
HelloTalk: 4.50 stars
purp - Make new friends: 4.42 stars
InterPals Penpals: 4.10 stars
Tellonym: 3.85 stars
```

## 🔍 Finding App Package Names

To use this library, you need the app's package name (app ID). Here's how to find it:

1. **From Play Store URL**: 
   - URL: `https://play.google.com/store/apps/details?id=com.whatsapp`
   - Package name: `com.whatsapp`

2. **From Android Device**:
   - Install "App Inspector" or similar apps
   - Find the package name in app details

3. **Common Examples**:
   - purp: `com.hubolabs.hubo`
   - InterPals: `net.interpals`
   - YeeTalk: `com.imback.yeetalk`
   - Tellonym: `de.tellonym.app`
   - HelloTalk: `com.hellotalk`
   - Amino: `com.narvii.amino.master`

## ⚠️ Important Notes

1. **Rate Limiting**: Don't make too many requests in quick succession to avoid being blocked
2. **Data Accuracy**: Some fields may be `None` if not available for specific apps
3. **Regional Differences**: Data may vary based on your location
4. **App Availability**: Some apps may not be available in all regions
5. **Caching**: The library automatically caches results per session for better performance
6. **Data Freshness**: Play Store data updates periodically; some metrics may have slight delays

## 🛠️ Error Handling

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()

try:
    data = scraper.get_field("invalid.package.name", "title")
    print(data)
except ValueError as e:
    print(f"Invalid app ID: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")
```

## 🔧 Troubleshooting

### Common Issues

**JSON Parsing Errors**: If you see "Error parsing ds:11 JSON" in logs, this affects only review data. The main app data will still be retrieved successfully.

**Unicode Encoding Errors**: On Windows, if you encounter encoding errors when printing data, ensure your console supports UTF-8:
```python
import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
```

**Rate Limiting**: If requests fail, wait a few seconds between calls to avoid being blocked by Google's servers.

**App Not Found**: Verify the package name is correct by checking the Play Store URL.

## 📝 Complete Example Script

```python
from gplay_scraper import GPlayScraper

def main():
    scraper = GPlayScraper()
    app_id = "com.hubolabs.hubo"
    
    print("=== PlayStore Analyzer Demo ===\n")
    
    # 1. Basic Information
    print("1. Basic Information:")
    basic = scraper.get_fields(app_id, ["title", "developer", "score"])
    for field, value in basic.items():
        print(f"   {field}: {value}")
    
    # 2. Single field access
    print(f"\n2. Install Count: {scraper.get_field(app_id, 'installs')}")
    
    # 3. Print methods
    print("\n3. Using print methods:")
    scraper.print_field(app_id, "genre")
    
    # 4. Complete analysis
    print("\n4. Getting all data...")
    all_data = scraper.analyze(app_id)
    print(f"   Total fields retrieved: {len(all_data)}")
    
    print("\n=== Analysis Complete ===")

if __name__ == "__main__":
    main()
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

**Happy Analyzing! 🚀**
