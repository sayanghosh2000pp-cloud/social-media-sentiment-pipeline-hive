import re
import math
try:
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    import nltk
except Exception:
    SentimentIntensityAnalyzer = None
    import nltk

class SentimentAnalyzer:
    def __init__(self):
        try:
            nltk.data.find('sentiment/vader_lexicon.zip')
        except Exception:
            nltk.download('vader_lexicon')
        self._sid = SentimentIntensityAnalyzer()

    def score(self, text: str) -> dict:
        if text is None:
            text = ""
        scores = self._sid.polarity_scores(text)
        c = scores.get('compound', 0.0)
        if c >= 0.05:
            label = 'positive'
        elif c <= -0.05:
            label = 'negative'
        else:
            label = 'neutral'
        scores['label'] = label
        return scores

_GLOBAL_SID = None

def get_global():
    global _GLOBAL_SID
    if _GLOBAL_SID is None:
        _GLOBAL_SID = SentimentAnalyzer()
    return _GLOBAL_SID

def analyze_text(text: str):
    sid = get_global()
    scores = sid.score(text)
    return (float(scores['compound']), float(scores['pos']), float(scores['neu']), float(scores['neg']), scores['label'])
