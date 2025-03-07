rss_feeds = {
    "Sports": {
        "The Hindu - Sports": "https://www.thehindu.com/sport/feeder/default.rss",
    },
    "Tech": {
        "Verge": "https://www.theverge.com/rss/index.xml",
    },
    "India": {
        "TOI - India": "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
    },
    "World": {
        "The Hindu - World": "https://www.thehindu.com/news/international/feeder/default.rss",
    },
    "Markets": {
        "The Hindu - Markets": "https://www.thehindu.com/business/markets/feeder/default.rss",
    },
    "Business": {
        "NDTV - Business": "https://feeds.feedburner.com/ndtvprofit-latest",
    },
    "Politics":{
        "News18 - Politics": "https://www.news18.com/commonfeeds/v1/eng/rss/politics.xml",
    }
}
for category, sources in rss_feeds.items():
        print(category,sources)
        source_name, url = sources
        print(source_name,url)