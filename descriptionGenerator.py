from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

model_name = "google/flan-t5-large"

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generateDescription(prompt, max_length=1000, num_return_sequences=1):
    if not model or not tokenizer:
        raise ValueError("Model and tokenizer are not loaded. Please load them before using this function.")

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_beams=8,  
        no_repeat_ngram_size=2,
        num_return_sequences=num_return_sequences,
    )

    generated_texts = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return generated_texts

