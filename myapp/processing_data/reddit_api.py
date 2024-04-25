# Reddit API Details
import praw
import requests
from .text_processing import clean_text
from .sentiment_analysis import sentiment_text, get_sentiment_score
from .summarization import summarize_positive_text, summarize_negative_text
CLIENT_ID = '7o7pycD5otZLxgEpThvvzw'
SECRET_KEY = 'm_sNunTSvyIaJ8Ws0x2jRMqiohqd7g'
username='Rich_Example740'
password='Chandu2001'

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET_KEY,
                     user_agent='test',
                     username=username,
                     password=password)

def fetch_subreddit(request):
    if request.method == "POST":
        subreddit_name = request.POST.get('subreddit')
        subreddit = reddit.subreddit(subreddit_name)
        posts = subreddit.new(limit=10)
        texts = []

        # Prepare data for display
        for post in posts:
            print(post)
            texts.append(f"{post.title}")
            post.comments.replace_more(limit=5)
            for comment in post.comments.list():
                texts.append(f"{comment.body}")


        # texts = clean_text(texts=texts)
        positive, negative = sentiment_text(texts=texts)
        positive_summary = summarize_positive_text(positive)
        negative_summary = summarize_negative_text(negative)

        sumPositive = sum(len(p) for p in positive)
        sumNegative = sum(len(n) for n in negative)

        sumPositiveSummary = sum(len(p) for p in positive_summary)
        sumNegativeSummary = sum(len(n) for n in negative_summary)


        print("Positive Texts")
        print("Scores of individual positive text:")
        print(f"Average score of positive text is {get_sentiment_score(positive)}")
        print(f"Number of positive texts is {len(positive)}")
        print(f"Length of original positive text is {sumPositive}")


        print("Positive Summary")
        print("Scores of individual positive summary text is:")
        print(f"Score of positive summary is {get_sentiment_score(positive_summary)}")
        print(f"Number of positive summary texts is is {len(positive_summary)}")
        print(f"Length of positive summary  text is {sumPositiveSummary}")

        print("Negative Texts")
        print("Scores of individual negative text:")
        print(f"Average score of negative text is {get_sentiment_score(negative)}")
        print(f"Number of negative texts is {len(negative)}")
        print(f"Length of negative text is {sumNegative}")

        print("Negative Summary")
        print("Scores of individual negative summary text is:")
        print(f"Score of negative summary is {get_sentiment_score(negative_summary)}")
        print(f"Number of negative summary texts is is {len(negative_summary)}")
        print(f"Length of negative summary  text is {sumNegativeSummary}")

        # positive_summary = post_process_text(positive_summary)
        # negative_summary = post_process_text(negative_summary)

        return positive_summary, negative_summary