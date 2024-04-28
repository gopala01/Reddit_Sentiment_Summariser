import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification
from optimum.pipelines import pipeline as opt_pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline, T5ForConditionalGeneration, T5Tokenizer

def generate_positive_summary(text):
    # Generate summary using Pegasus-X model
    if text != "":
        model_name = "google/pegasus-xsum"
        # Use GPU if available otherwise use CPU
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Load tokenizer and modeul using Pegasus-X
        tokenizer = PegasusTokenizer.from_pretrained(model_name)
        model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)
        
        # Preparing the text
        batch = tokenizer(text, truncation=True, padding="longest", return_tensors="pt").to(device)

        # Generating summary with all the parameters
        translated = model.generate(**batch,
                                        # max_length = 150,
                                        max_new_tokens = 100,
                                        # Max tokens to generate in a summary

                                        # do_sample = False,
                                        # top_p = 0.7, 
                                        repetition_penalty = 2.0,
                                        # Setting a penalty for repeated phrases
                                        length_penalty = 2.0,
                                        # Promoting longer sentences 
                                        num_beams=2)
                                        # Number of beams to use

        # Translate the tokens to text
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        positive_summary = tgt_text[0]
        return positive_summary
    else:
        return ""
    

def detoxify_text(text):
    # Detoxify using T5-Small model
    if text != "":
        model_name = "erfansadraiye/detoxify"
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = T5Tokenizer.from_pretrained(model_name)
        model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)
        
        batch = tokenizer(text, truncation=True, padding="longest", return_tensors="pt").to(device)
        translated = model.generate(**batch,
                                        # max_length = 150,
                                        max_new_tokens = 100,
                                        
                                        # do_sample = False,
                                        # top_p = 0.7, 
                                        repetition_penalty = 2.0,
                                        length_penalty = 2.0,
                                        num_beams=2)
        detoxified_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        return detoxified_text
    else:
        return ""


def generate_negative_summary(text):
    # Generate summary using Pegasus-X model

    if text != "":
        model_name = "google/pegasus-xsum"
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = PegasusTokenizer.from_pretrained(model_name)
        model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)
        
        batch = tokenizer(text, truncation=True, padding="longest", return_tensors="pt").to(device)
        translated = model.generate(**batch,
                                        # max_length = 150,
                                        max_new_tokens = 100,
                                        
                                        # do_sample = False,
                                        # top_p = 0.7, 
                                        repetition_penalty = 2.0,
                                        length_penalty = 2.0,
                                        num_beams=2)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        negative_summary = detoxify_text(tgt_text[0])
        return negative_summary
    else:
        return ""
    

# Returning summarises as arrays

def summarize_positive_text(texts):
    positive_summary = [generate_positive_summary(text) for text in texts]
    return positive_summary

def summarize_negative_text(texts):
    negative_summary = [generate_negative_summary(text) for text in texts]
    return negative_summary
