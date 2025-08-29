import streamlit as st
from models import fetch_article, summarize_text, analyze_sentiment

def main():
    st.title("News Article Summarizer & Sentiment Analyzer")
    st.write("Paste a news article URL below. The AI will summarize the article and analyze its sentiment (tone).")

    url = st.text_input("News Article URL")

    if st.button("Summarize & Analyze"):
        if url:
            with st.spinner("Fetching and analyzing article..."):
                article = fetch_article(url)
                if not article:
                    st.error("Could not extract text from the provided URL.")
                    return
                summary = summarize_text(article)
                tone = analyze_sentiment(summary)
            st.subheader("Summary")
            st.write(summary)
            st.subheader("Sentiment Tone")
            st.write(tone)
        else:
            st.error("Please paste a valid URL.")

if __name__ == "__main__":
    main()