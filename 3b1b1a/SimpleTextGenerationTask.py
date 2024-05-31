import random

def load_book(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def tokenize(text):
    return text.lower().split()
