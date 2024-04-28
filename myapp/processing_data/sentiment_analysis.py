from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

# Vader Tool
# Getting sentiment of text and take most positive and most negative text to summarize
        

sia = SentimentIntensityAnalyzer()




def get_sentiment_score(texts):
    if isinstance(texts, list):
        sum_scores = 0
        for text in texts:
            score = sia.polarity_scores(text)['compound']
            print(score)
              # Print each score for testing
            sum_scores += score
        average_score = sum_scores / len(texts) if texts else 0
        # Calculate the average score
        return average_score
    else:
        score = sia.polarity_scores(texts)['compound']
        print(f"Summary: {texts} - Score: {score}\n")  
        # Print the score for the single text
        return score
    
def sentiment_text(texts):
    positive = []
    negative = []
    sentiment_scores = {text: sia.polarity_scores(text) for text in texts}
    # print(sentiment_scores)
    for text, scores in sentiment_scores.items():
        score = scores['compound']
        # print(f"Text: {text}\nScores: {score}\n")

        if score >= 0.5:
            positive.append(text)
        elif score <= -0.5:
            negative.append(text)
    return positive, negative    