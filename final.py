# Import necessary libraries

import newspaper
from newspaper import Article
from transformers import pipeline
import gradio as gr

# Function to scrape and summarize news articles
def summarize_news(topic):
    # Scrape articles from Al Jazeera
    articles = []
    aljazeera_url = f"https://www.aljazeera.com/topics/{topic}"
    paper = newspaper.build(aljazeera_url, memoize_articles=False)
    for article in paper.articles:
        try:
            article.download()
            article.parse()
            articles.append(article.text)
        except Exception as e:
            print(f"Error scraping article: {e}")

    # Translate articles to English
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ar-en")
    translated_articles = [translator(article, max_length=512)[0]['translation_text'] for article in articles]

    # Summarize articles
    summarizer = pipeline("summarization")
    summaries = [summarizer(article, max_length=150, min_length=50, do_sample=False)[0]['summary_text'] for article in translated_articles]

    return summaries

# Interface for the web app
interface = gr.Interface(
    fn=summarize_news,
    inputs="text",
    outputs="text",
    title="News Summarizer",
    description="Enter a topic to summarize news articles from Al Jazeera.",
    examples=[
        ["Afghanistan"],
        ["Syria"],
        ["COVID-19"]
    ]
)

# Launch the web app
interface.launch()
