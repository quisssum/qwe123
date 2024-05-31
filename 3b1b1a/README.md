# Simple Text Generation Task

## Task Description
During this task, you will be coding a fun little task from the field of natural language processing. You will be implementing a simple traditional model called the Markov chain model for the task of text generation.

### Steps

1. **Choose a Book**
    - Choose a book that you like (Keep it under 3MB).
    - Download the book in .txt format.

2. **Create a Python File**
    - Open the book file.
    - (Optional) Clean the text file, e.g., lowercase everything, etc.
    - Split the text into a list of its tokens (i.e., words and punctuation). You may use native Python methods or consult other libraries.
    - Create a dictionary object, where:
        - The keys are the unique tokens.
        - The values are lists of the next following words that occur after the key token (1 next word for every occurrence).
    - Generate text. Make it so that:
        - The program chooses the first word randomly from the keys and prints it (you can use a library for this).
        - Then it consults the occurrence list from the dictionary you created to randomly choose the next word to print out (you can use a library for this).
        - Repeat the previous step 200 times.
