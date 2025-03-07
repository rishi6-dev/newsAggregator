from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

from newspaper import Article

import nltk

nltk.download('punkt_tab')

def fetch_full_article(news_url):
    article = Article(news_url)
    article.download()
    article.parse()

    if not article.text.strip():
        return None

    return article.text  # Return text instead of the article object

def summarize_text(article_text, sentence_count=3):
    parser = PlaintextParser.from_string(article_text, Tokenizer("english"))
    summarizer = TextRankSummarizer()

    summary = summarizer(parser.document, sentence_count)

    final = ' '.join(str(sentence) for sentence in summary)
    return final


def summary(url):
    article_text = fetch_full_article(url)

    if article_text:
        summary = summarize_text(article_text)
        return summary
    else:
        return "Failed to extract article text."
    

print(summary("https://www.thehindu.com/sport/cricket/icc-champions-trophy-final-every-batter-contributed-to-teams-cause-in-its-run-to-final-says-sitanshu-kotak/article69304049.ece"))