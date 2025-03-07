import feedparser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def fetch_news(feed_url):
    feed = feedparser.parse(feed_url)
    news_list = []
    
    for entry in feed.entries[:5]:  # Limit to 5 articles
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
    rss_feeds_topstories = {
        "The Hindu": "https://www.thehindu.com/news/national/feeder/default.rss",
        "CNN": "http://rss.cnn.com/rss/edition.rss",
        "TOI": "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
    }
    rss_feeds__sports = {}
    rss_feeds__tech = {}
    rss_feeds__India = {}
    rss_feeds__world = {}
    rss_feeds__business = {}
    
    for source, url in rss_feeds.items():
        print(f"\nNews from {source}:\n" + "="*80)
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
