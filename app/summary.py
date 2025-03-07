from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

import nltk
nltk.download('punkt_tab')

def summarize_text(article_text, sentence_count=5):
    parser = PlaintextParser.from_string(article_text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    
    summary = summarizer(parser.document, sentence_count)
    
    final = ' '.join(str(sentence) for sentence in summary)
    return final

