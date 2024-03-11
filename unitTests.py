import unittest
from unittest.mock import patch, MagicMock
from rss_code import framework
from rss_code.framework import sentiment_text, generate_summary, fetch_subreddit
from nltk.sentiment import SentimentIntensityAnalyzer


# class TestRedditAPI(unittest.TestCase):
#     @patch('Reddit_Sentiment_Summariser.framework.praw.Reddit') 
#     def test_fetch_subreddit_posts(self, mock_reddit):
#         with framework.app.test_client() as client:
#             response = client.post('/fetch_subreddit', data={'subreddit': 'marvel'})
#             self.assertEqual(response.status_code, 200)



# class TestSentimentText(unittest.TestCase):
#     def test_all_positive(self):
#         texts = ["I love sunny days", "This is wonderful!"]
#         expected_positive = ["I love sunny days", "This is wonderful!"]
#         expected_negative = []
#         positive, negative = sentiment_text(texts)
#         self.assertEqual(positive, expected_positive)
#         self.assertEqual(negative, expected_negative)

#     def test_all_negative(self):
#         texts = ["I hate rainy days", "This is terrible!"]
#         expected_positive = []
#         expected_negative = ["I hate rainy days", "This is terrible!"]
#         positive, negative = sentiment_text(texts)
#         self.assertEqual(positive, expected_positive)
#         self.assertEqual(negative, expected_negative)

#     def test_mixed_sentiments(self):
#         texts = ["I love sunny days", "This is terrible!"]
#         expected_positive = ["I love sunny days"]
#         expected_negative = ["This is terrible!"]
#         positive, negative = sentiment_text(texts)
#         self.assertEqual(positive, expected_positive)
#         self.assertEqual(negative, expected_negative)

#     def test_neutral_texts(self):
#         texts = ["This is a book.", "Just a normal day."]
#         expected_positive = []
#         expected_negative = []
#         positive, negative = sentiment_text(texts)
#         self.assertEqual(positive, expected_positive)
#         self.assertEqual(negative, expected_negative)

class TestSummarizeText(unittest.TestCase):
    def test_single_text_summary(self):
        texts = "This is a long text that needs to be summarized. It contains multiple sentences with various information. The goal is to create a concise summary."
        summaries = generate_summary(texts)
        self.assertEqual(len(summaries), 1)
        self.assertTrue(len(summaries[0]) < len(texts[0]))

    # def test_multiple_texts_summary(self):
    #     texts = ["First text to summarize.", "Second text that requires summarization."]
    #     summaries = summarize_text(texts)
    #     self.assertEqual(len(summaries), 2)
    #     for summary, text in zip(summaries, texts):
    #         self.assertTrue(len(summary) < len(text))

    # def test_empty_text_summary(self):
    #     texts = ""
    #     summaries = generate_summary(texts)
    #     self.assertEqual(summaries, "")

    # def test_very_long_text_summary(self):
    #     text = ["This is a very long text " * 100 + "that needs to be summarized."]
    #     summary = summarize_text(text)
    #     self.assertTrue(len(summary[0]) < len(text[0]))
        


if __name__ == '__main__':
    unittest.main()
