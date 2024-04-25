from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
# from myapp.views import fetch_subreddit_view
from myapp.processing_data.sentiment_analysis import sentiment_text
from myapp.processing_data.summarization import generate_positive_summary as generate_summary
from myapp.processing_data.reddit_api import fetch_subreddit, praw
# Create your tests here.

class TestRedditAPI(TestCase):
    def setUp(self):
        self.client = Client()
        self.subreddit_url = reverse('fetch_subreddit')
    @patch('myapp.processing_data.reddit_api.reddit')  # Updated patch location
    def test_fetch_subreddit_posts(self, mock_reddit):
        mock_subreddit = MagicMock()
        mock_reddit.subreddit.return_value = mock_subreddit

        mock_post = MagicMock(title="Example Post", comments=MagicMock())
        mock_post.comments.list.return_value = [MagicMock(body="Example comment")]
        mock_subreddit.new.return_value = [mock_post]

        # Simulate a POST request to fetch subreddit
        response = self.client.post(self.subreddit_url, {'subreddit': 'python'})

        # Assertions to verify praw was called as expected
        mock_reddit.subreddit.assert_called_once_with('python')
        mock_subreddit.new.assert_called_once_with(limit=10)
        self.assertEqual(response.status_code, 200)
# class TestSentimentText(TestCase):
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
# class TestSummarizeText(TestCase):
#     def test_single_text_summary(self):
#         text = "This is a long text that needs to be summarized. It contains multiple sentences with various information. The goal is to create a concise summary."
#         summaries = [generate_summary(text)]
#         self.assertEqual(len(summaries), 1)
#         self.assertTrue(len(summaries[0]) < len(text))

#     def test_multiple_texts_summary(self):
#         texts = ["This is the first long text that needs to be summarized. It contains multiple sentences with various information. The goal is to create a concise summary.", "Second text that requires summarization is a little longer. This is another long text that needs to be summarized. It contains multiple sentences with various information. The goal is to create a concise summary."]
#         summaries = [generate_summary(text) for text in texts]
#         self.assertEqual(len(summaries), 2)
#         for i in range(len(summaries)):
#             self.assertTrue(len(summaries[i]) < len(texts[i]))

#     def test_empty_text_summary(self):
#         texts = ""
#         summaries = generate_summary(texts)
#         self.assertEqual(summaries, "")

#     def test_very_long_text_summary(self):
#         text = ["This is a very long text " * 100 + "that needs to be summarized."]
#         summary = generate_summary(text)
#         self.assertTrue(len(summary[0]) < len(text[0]))