import praw
import requests
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
# Use Reddit credentials to access the API

def fetch_subreddit(request):
    if request.method == "POST":
        subreddit_name = request.POST.get('subreddit')
        # Getting the user input in search bar
        subreddit = reddit.subreddit(subreddit_name)
        # Accessing the subreddit the user inputted
        posts = subreddit.new(limit=10)
        # Extracting last 10 posts from the subreddit
        texts = []

        # Extracting text from each posts
        for post in posts:
            print(post)
            texts.append(f"{post.title}")
            # Appending title of post to array
            post.comments.replace_more(limit=5)
            for comment in post.comments.list():
                texts.append(f"{comment.body}")
                # Appending 5 comments per post to array


        # Sentiment analysis 
        positive, negative = sentiment_text(texts=texts)

        # Summarisation
        positive_summary = summarize_positive_text(positive)
        negative_summary = summarize_negative_text(negative)


        # Calculations for texts and summarisations
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

        # Returning summarises
        return positive_summary, negative_summary
    