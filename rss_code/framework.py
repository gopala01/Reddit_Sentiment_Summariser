import praw
# from openai import OpenAI
import nltk
import ssl
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
from flask import Flask, request, render_template
import requests
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch


app = Flask(__name__)

# Reddit API Details

CLIENT_ID = '7o7pycD5otZLxgEpThvvzw'
SECRET_KEY = 'm_sNunTSvyIaJ8Ws0x2jRMqiohqd7g'
username='Rich_Example740'
password='Chandu2001'

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET_KEY,
                     user_agent='test',
                     username=username,
                     password=password)


# Pegasus-X Model
# Summarising the text using Pegasus-X

def generate_summary(text):

    if text != "":
        model_name = "google/pegasus-xsum"
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = PegasusTokenizer.from_pretrained(model_name)
        model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)
        
        batch = tokenizer(text, truncation=True, padding="longest", return_tensors="pt").to(device)
        translated = model.generate(**batch,
                                        # max_length = 150,
                                        max_new_tokens = 100,
                                        # min_length = 75,
                                        # # Try without these two
                                        # do_sample = False,
                                        # top_p = 0.7, 
                                        repetition_penalty = 2.0,
                                        length_penalty = 2.0,
                                        num_beams=2)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text[0]
    else:
        return ""

def summarize_text(texts):
    summaries = [generate_summary(text) for text in texts if text.strip() != ""]
    return summaries

print(generate_summary(text=""))

# Getting sentiment of text and take most positive and most negative text to summarize
def sentiment_text(texts):
    positive = []
    negative = []
    
    sia = SentimentIntensityAnalyzer()

    sentiment_scores = {text: sia.polarity_scores(text) for text in texts}
    # print(sentiment_scores)

    for text, scores in sentiment_scores.items():
        score = scores['compound']
        # print(f"Text: {text}\nScores: {score}\n")

        if score > 0.5:
            positive.append(text)
        elif score < -0.5:
            negative.append(text)
    return positive, negative    

    


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fetch_subreddit', methods=['POST'])
def fetch_subreddit():

    subreddit_name = request.form['subreddit']
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.new(limit=10)

    texts = []

    # Prepare data for display
    for post in posts:
        texts.append(f"{post.title}")
        post.comments.replace_more(limit=5)
        for comment in post.comments.list():
            texts.append(f"{comment.body}")

    positive, negative = sentiment_text(texts=texts)

    positive_summary = summarize_text(positive)
    negative_summary = summarize_text(negative)

    positive_summary = " ".join(positive_summary)
    negative_summary = " ".join(negative_summary)

    return render_template('results.html', positive=positive_summary, negative=negative_summary)

print(summarize_text([""]))

if __name__ == '__main__':
    app.run(debug=True)








