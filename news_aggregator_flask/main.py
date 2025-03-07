from flask import Flask, render_template, request, jsonify
from app.fetch_news import fetch_news
from app.summarise import summary
app = Flask(__name__)

rss_feeds = {
    "Sports": [
        "The Hindu - Sports", "https://www.thehindu.com/sport/feeder/default.rss",
    ],
    "Tech": [
        "Verge", "https://www.theverge.com/rss/index.xml",
    ],
    "India": [
        "TOI - India", "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
    ],
    "World": [
        "The Hindu - World", "https://www.thehindu.com/news/international/feeder/default.rss",
    ],
    "Markets": [
        "The Hindu - Markets", "https://www.thehindu.com/business/markets/feeder/default.rss",
    ],
    "Business": [
        "NDTV - Business", "https://feeds.feedburner.com/ndtvprofit-latest",
    ],
    "Politics":[
        "News18 - Politics", "https://www.news18.com/commonfeeds/v1/eng/rss/politics.xml",
    ]
}


categories = list(rss_feeds.keys())

@app.route('/')
def index():
    
    return render_template('index.html', categories=categories)

@app.route('/category/<category>')
def category_page(category):
    if category in categories:
        return render_template('category.html', category=category, news_list=fetch_news(rss_feeds[category]))
    else:
        return "Category not found", 404

@app.route('/get_summary', methods=['GET'])
def get_summary():
    src_url = request.args.get("url")  # Get URL from query parameter
    title = request.args.get("title")
    if not src_url:
        return jsonify({"error": "No URL provided"}), 400  # Handle missing URL
    print(src_url)    
    return jsonify({"summary": summary(src_url), "title":title})  # Return JSON response

if __name__ == '__main__':
    app.run(debug=True)
