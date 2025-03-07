import feedparser
from bs4 import BeautifulSoup


def fetch_news(data):
    source_name, feed_url =  data
    feed = feedparser.parse(feed_url)
    news_list = []
    
    for entry in feed.entries[:20]: 
        title = entry.get("title", "No Title")
        srcurl = entry.get("link", "#")
        desc_raw = entry.get("summary", "No description available")
        date = entry.get("published", "No date available")
        
        soup = BeautifulSoup(desc_raw, "html.parser")
        desc = soup.get_text()
        
        image = None

        if "enclosure" in entry:
            image = entry.enclosure.get("url")
        else:
            soup = BeautifulSoup(desc_raw, "html.parser")
            img_tag = soup.find("img")
            if img_tag:
                image = img_tag.get("src")

        if not image and "media_content" in entry:
            image = entry.media_content[0]["url"]
        elif not image and "content" in entry:
            soup = BeautifulSoup(entry.content[0].value, "html.parser")
            img_tag = soup.find("img")
            if img_tag:
                image = img_tag.get("src")

        if image and desc:
            news_list.append({
                'title': title,
                'desc': desc,
                'src': source_name, #returns name of news and category
                'img': image,
                'srcurl': srcurl,
                'date': date
            })
        
    
    return news_list

#dont need anything below this, just for reference
def main():
    all_news = {}
    
    for category, sources in rss_feeds.items():
        category_news = []
        for source_name, url in sources.items():
            news_list = fetch_news(url, source_name)
            category_news.extend(news_list)
        all_news[category] = category_news
    
    for category, news_list in all_news.items():
        print(f"\nCategory: {category}\n" + "=" * 80)
        for news in news_list:
            print(f"Title: {news['title']}")
            print(f"Date: {news['date']}")
            print(f"Source: {news['src']}")
            print(f"Link: {news['srcurl']}")
            print(f"Image: {news['img']}")
            print(f"Description: {news['desc'][:200]}")  # ... is to truncate content
            print("-" * 80)

if __name__ == "__main__":
    main()
