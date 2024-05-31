import random

def load_book(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def tokenize(text):
    return text.lower().split()

def build_markov_chain(tokens):
    markov_chain = {}
    for i in range(len(tokens) - 1):
        current_token = tokens[i]
        next_token = tokens[i + 1]
        if current_token not in markov_chain:
            markov_chain[current_token] = []
        markov_chain[current_token].append(next_token)
    return markov_chain
