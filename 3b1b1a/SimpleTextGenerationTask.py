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

def generate_text(markov_chain, num_words=200):
    current_token = random.choice(list(markov_chain.keys()))
    generated_text = [current_token]

    for word_count in range(num_words - 1):
        next_tokens = markov_chain[current_token]
        current_token = random.choice(next_tokens)
        generated_text.append(current_token)

    return ' '.join(generated_text)

def main():
    book_path = '/Users/klishchyuriy/Documents/GitHub/Additional_Points_Tasks/3b1b1a/TheGreatGatsby.txt'

    text = load_book(book_path)
    tokens = tokenize(text)
    markov_chain = build_markov_chain(tokens)
    generated_text = generate_text(markov_chain)

    print(generated_text)


if __name__ == "__main__":
    main()