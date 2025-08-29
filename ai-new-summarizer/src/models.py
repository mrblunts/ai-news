from transformers import pipeline
import requests
from bs4 import BeautifulSoup

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment = pipeline("sentiment-analysis")

def fetch_article(url):
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        # Ensure correct encoding
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])
        # Limit text length for summarizer
        return text[:4000]
    except Exception as e:
        # Optionally log the error: print(f"Error fetching article: {e}")
        return ""

def summarize_text(text):
    if not text.strip():
        return "Could not extract article text."
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def analyze_sentiment(text):
    if not text.strip():
        return "Unknown"
    result = sentiment(text)
    return result[0]['label']