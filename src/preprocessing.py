# src/preprocessing.py
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def preprocess_text(text):
    """
    Lowercase + remove punctuation
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

def tokenizer(text):
    """
    Tokenize text and remove English stopwords
    """
    tokens = re.findall(r'\b\w+\b', text.lower())
    tokens = [word for word in tokens if word not in ENGLISH_STOP_WORDS]
    return tokens
