from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
        

sia = SentimentIntensityAnalyzer()
# Using Sentiment Intensity Analyzer

def get_sentiment_score(texts):
    if isinstance(texts, list):
        sum_scores = 0
        for text in texts:
            score = sia.polarity_scores(text)['compound']
            # Taking compoud score of the text
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
    # Returning score to use to check whether the text is highly positive or highly negative
    
def sentiment_text(texts):
    positive = []
    negative = []
    sentiment_scores = {text: sia.polarity_scores(text) for text in texts}
    # Extracting sentiment score
    for text, scores in sentiment_scores.items():
        score = scores['compound']
        # Taking compound score

        if score >= 0.5:
            positive.append(text)
            # If sentiment score of text is highly positive you append the text to positive array
        elif score <= -0.5:
            negative.append(text)
            # If sentiment score of text is highly negative you append the text to negative array
    return positive, negative    
