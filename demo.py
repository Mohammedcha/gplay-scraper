from flask import Flask, render_template, request
from gplay_scraper import GPlayScraper

app = Flask(__name__)
scraper = GPlayScraper()

CATEGORIES = [
    'APPLICATION', 'ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY', 'BOOKS_AND_REFERENCE', 'BUSINESS',
    'COMICS', 'COMMUNICATION', 'DATING', 'EDUCATION', 'ENTERTAINTAINMENT', 'EVENTS',
    'FINANCE', 'FOOD_AND_DRINK', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME',
    'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'MAPS_AND_NAVIGATION', 'MEDICAL',
    'MUSIC_AND_AUDIO', 'NEWS_AND_MAGAZINES', 'PARENTING', 'PERSONALIZATION',
    'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING', 'SOCIAL', 'SPORTS', 'TOOLS',
    'TRAVEL_AND_LOCAL', 'VIDEO_PLAYERS', 'WEATHER', 'GAME', 'GAME_ACTION',
    'GAME_ADVENTURE', 'GAME_ARCADE', 'GAME_BOARD', 'GAME_CARD', 'GAME_CASINO',
    'GAME_CASUAL', 'GAME_EDUCATIONAL', 'GAME_MUSIC', 'GAME_PUZZLE', 'GAME_RACING',
    'GAME_ROLE_PLAYING'
]

COUNTRIES = {
    'us': 'United States', 'ca': 'Canada', 'mx': 'Mexico', 'pr': 'Puerto Rico',
    'au': 'Australia', 'in': 'India', 'jp': 'Japan', 'my': 'Malaysia',
    'nz': 'New Zealand', 'sg': 'Singapore', 'tw': 'Taiwan', 'at': 'Austria',
    'be': 'Belgium', 'cz': 'Czech Republic', 'dk': 'Denmark', 'ee': 'Estonia',
    'fi': 'Finland', 'fr': 'France', 'de': 'Germany', 'hu': 'Hungary',
    'lt': 'Lithuania', 'lv': 'Latvia', 'ro': 'Romania', 'si': 'Slovenia',
    'sk': 'Slovakia', 'pl': 'Poland', 'ie': 'Ireland', 'it': 'Italy',
    'nl': 'Netherlands', 'no': 'Norway', 'pt': 'Portugal', 'es': 'Spain',
    'se': 'Sweden', 'ch': 'Switzerland', 'gb': 'United Kingdom'
}

@app.route('/')
def index():
    category = request.args.get('category', 'APPLICATION')
    country = request.args.get('country', 'us')
    apps = scraper.list_analyze(collection='TOP_FREE', category=category, country=country, count=100)
    return render_template('index.html', apps=apps, categories=CATEGORIES, countries=COUNTRIES,
                           selected_category=category, selected_country=country)

@app.route('/developer', methods=['GET', 'POST'])
def developer():
    apps = None
    dev_id = ''
    searched = False
    if request.method == 'POST':
        searched = True
        dev_id = request.form['dev_id']
        if dev_id:
            apps = scraper.developer_analyze(dev_id)
    return render_template('developer.html', apps=apps, dev_id=dev_id, searched=searched)

if __name__ == '__main__':
    app.run(debug=True)
