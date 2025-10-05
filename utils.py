import re
from html import unescape

URL_RE = re.compile(r'https?://\S+|www\.\S+')
MENTION_RE = re.compile(r'@\w+')
HASHTAG_RE = re.compile(r'#(\w+)')
MULTI_WS = re.compile(r'\s+')

def clean_text(text: str) -> str:
    if text is None:
        return ''
    txt = unescape(text)
    txt = URL_RE.sub(' ', txt)
    txt = MENTION_RE.sub(' ', txt)
    txt = HASHTAG_RE.sub(r'\1', txt)
    txt = MULTI_WS.sub(' ', txt)
    txt = txt.strip()
    return txt
