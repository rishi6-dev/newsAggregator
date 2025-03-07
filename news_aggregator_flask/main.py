from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template
from rssFeed import rss_feeds


app = Flask(__name__)

# Sample news data categorized
news_data = {
    "tech": [
        {"title": "Tech News 1", "desc": "Description of tech news 1", "src": "CNN", "image": "https://example.com/image1.jpg", "date": "2025-03-07"},
        {"title": "Tech News 2", "desc": "Description of tech news 2", "src": "The Hindu", "image": "https://example.com/image2.jpg", "date": "2025-03-07"}
    ],
    "international": [
        {"title": "International News 1", "desc": "Description of international news 1", "src": "BBC", "image": "https://example.com/image3.jpg", "date": "2025-03-07"}
    ],
    "national": [
        {"title": "National News 1", "desc": "Description of national news 1", "src": "NDTV", "image": "https://example.com/image4.jpg", "date": "2025-03-07"}
    ],
    "sports": [
        {"title": "Sports News 1", "desc": "Description of sports news 1", "src": "ESPN", "image": "https://example.com/image5.jpg", "date": "2025-03-07"}
    ],
    "business": [
        {"title": "Business News 1", "desc": "Description of business news 1", "src": "Forbes", "image": "https://example.com/image6.jpg", "date": "2025-03-07"}
    ],
    "top_picks": [
        {"title": "Top Pick 1", "desc": "Description of top pick news 1", "src": "Reuters", "image": "https://example.com/image7.jpg", "date": "2025-03-07"}
    ]
}

@app.route('/')
def index():
    # categories = list(news_data.keys())
    categories = list(rss_feeds.keys())
    return render_template('index.html', categories=categories)

@app.route('/category/<category>')
def category_page(category):
    if category in news_data:
        return render_template('category.html', category=category, news_list=news_data[category])
    else:
        return "Category not found", 404

@app.route('/get_summary', methods=['GET'])
def get_summary():
    src_url = request.args.get("url")  # Get URL from query parameter
    title = request.args.get("title")
    print(src_url,title)
    if not src_url:
        return jsonify({"error": "No URL provided"}), 400  # Handle missing URL

    # Dummy response for now
    summary = f"Summary for {src_url}"

    return jsonify({"summary": summary, "title":title})  # Return JSON response

if __name__ == '__main__':
    app.run(debug=True)
