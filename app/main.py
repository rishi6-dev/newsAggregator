import feedparser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk


rss_feeds = {
    "Sports": {
        "The Hindu - Sports": "https://www.thehindu.com/sport/feeder/default.rss",
    },
    "Tech": {
        "TechCrunch": "http://feeds.feedburner.com/TechCrunch/",
    },
    "India": {
        "TOI - India": "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
    },
    "World": {
        "The Hindu - World": "https://www.thehindu.com/news/international/feeder/default.rss",
    },
    "Markets": {
        "CNN - Markets": "http://rss.cnn.com/rss/money_markets.rss",
    }
}

def fetch_news(feed_url):
    feed = feedparser.parse(feed_url)
    news_list = []
    
    for entry in feed.entries[:5]:  # Limit to 5 articles per source
        title = entry.title
        link = entry.link
        description = entry.summary if hasattr(entry, 'summary') else "No description available"
        pub_date = entry.published if hasattr(entry, 'published') else "No date available"
        news_list.append((title, link, description, pub_date))
    
    return news_list

def summarize_text(text, sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences)
    return ' '.join(str(sentence) for sentence in summary)

def main():
    for category, sources in rss_feeds.items():
        print(f"\nCategory: {category}\n" + "="*80)
        
        for source, url in sources.items():
            print(f"\nNews from {source}:\n" + "-"*80)
            news_list = fetch_news(url)
            
            if not news_list:
                print("No news articles found.")
            else:
                for title, link, description, pub_date in news_list:
                    print(f"Title: {title}")
                    print(f"Publication Date: {pub_date}")
                    print(f"Link: {link}")
                    summary = summarize_text(description)
                    print(f"Summary: {summary}\n{'-'*80}\n")

if __name__ == "__main__":
    main()
