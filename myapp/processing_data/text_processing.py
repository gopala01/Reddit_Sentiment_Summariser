import spacy
import nltk
import re

nlp = spacy.load('en_core_web_sm')

def clean_text(texts):
    for text in texts:
        text = re.sub(r'https?://\S+', '', text)  # Remove URLs
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Remove bold Markdown, keeping the text
        text = re.sub(r'\*(.*?)\*', r'\1', text)  # Remove italic Markdown, keeping the text
        text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII characters
        text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces and trim

def refine_text_spacy(text):
    doc = nlp(text)
    refined_sentences = []
    for sentence in doc.sents:
        # Advanced grammar and coherency checks
        # For example, checking for subject-verb agreement, missing determiners, etc.
        refined_sentence = refine_sentence(sentence)
        refined_sentences.append(refined_sentence)
    return " ".join(refined_sentences)

def refine_sentence(sentence):
    # Implement custom logic here for refining the sentence
    # This could include reordering sentence parts for better flow, adding missing elements, etc.
    return sentence.text  # Placeholder for custom refinement logic

def post_process_text(text):
    # Check grammar with nltk
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
    # return [sentences]