from newspaper import Article
def fetch_full_article(news_url):
    
    """Fetches full article text using newspaper3k."""
    # TODO: Implement this function
    # url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
    article = Article(news_url)
    print(article)
    article.download()
    article.parse()
    print(article.text)
    return article

fetch_full_article('https://www.thehindu.com/sport/cricket/champions-trophy-final-williamson-ravindra-skirt-talk-of-india-advantage-in-dubai/article69297793.ece')