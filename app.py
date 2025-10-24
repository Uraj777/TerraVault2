from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ===== Article Data Structure =====
articles = [
    {
        'title': 'Atlantis',
        'desc': 'Legend speaks of a magnificent city lost beneath the waves, a place of unmatched beauty and wisdom.',
        'img': 'atlantis.jpg',
        'url': '/atlantis'  # FIX: Set distinct URL for article page
    },
    {
        'title': 'Chernobyl',
        'desc': 'The site of the world’s worst nuclear disaster, frozen in time since 1986.',
        'img': 'chernobyl.jpg',
        'url': '/chernobyl' # FIX: Set distinct URL for article page
    },
    {
        'title': 'Pompeii Volcano',
        'desc': 'An ancient Roman city buried in ash after Mount Vesuvius erupted in AD 79.',
        'img': 'pompeii.jpg',
        'url': '/pompeii'  # FIX: Set distinct URL for article page
    },
    # Placeholders for other categories to ensure templates always have content
    {
        'title': 'Cosmic Black Holes',
        'desc': 'Regions of spacetime exhibiting such strong gravitational effects that nothing can escape from inside it.',
        'img': 'cosmos.jpg',
        'url': '/cosmos'
    },
    {
        'title': 'The Great Barrier Reef',
        'desc': 'The world\'s largest coral reef system, struggling against climate change and human impact.',
        'img': 'reef.jpg',
        'url': '/environment'
    },
    {
        'title': 'Plastic Pollution',
        'desc': 'Billions of tons of plastic enter the environment each year, contaminating water, and entering the food chain.',
        'img': 'plasticpollution.jpg',
        'url': '/human-impact'
    },
    {
        'title': 'Bermuda Triangle',
        'desc': 'A region in the western Atlantic Ocean where ships and planes are said to mysteriously vanish.',
        'img': 'bermuda.jpg',
        'url': '/myths'
    }
]

# ===== ROUTES =====
@app.route('/')
def home():
    query = request.args.get('q', '')
    # Filter for search results, defaults to all articles if no query
    filtered_articles = [a for a in articles if query.lower() in a['title'].lower() or query.lower() in a['desc'].lower()]
    return render_template('home.html', articles=filtered_articles, query=query)

# --- Category Pages: Filter articles and pass the list ---
@app.route('/environment')
def environment():
    env_articles = [a for a in articles if 'reef' in a['title'].lower() or 'reef' in a['desc'].lower() or 'environment' in a['url']]
    return render_template('environment.html', articles=env_articles, query='')

@app.route('/cosmos')
def cosmos():
    cosmos_articles = [a for a in articles if 'cosmos' in a['title'].lower() or 'black hole' in a['desc'].lower()]
    return render_template('cosmos.html', articles=cosmos_articles, query='')

@app.route('/disasters')
def disasters():
    disaster_articles = [a for a in articles if 'disaster' in a['title'].lower() or 'volcano' in a['title'].lower() or 'chernobyl' in a['title'].lower()]
    return render_template('disasters.html', articles=disaster_articles, query='')

@app.route('/human-impact')
def human_impact():
    # Since this page uses static cards, we don't pass articles via Flask, but you could if needed.
    return render_template('human-impact.html')

@app.route('/myths')
def myths():
    # Since this page uses static cards, we don't pass articles via Flask, but you could if needed.
    return render_template('myths.html')

# --- Article Pages: Dedicated routes for specific articles ---
@app.route('/atlantis')
def atlantis():
    return render_template('atlantis.html')

@app.route('/chernobyl')
def chernobyl():
    return render_template('chernobyl.html')

@app.route('/pompeii')
def pompeii():
    return render_template('pompeii.html')


# FIX: Remove the redundant /search route and redirect to home to handle search
@app.route('/search')
def search():
    query = request.args.get('q', '')
    # Redirect to home, where the search logic lives
    return redirect(url_for('home', q=query))


if __name__ == '__main__':
    # Ensure you create a 'static' folder and put all images/css/js inside it
    app.run(debug=True)