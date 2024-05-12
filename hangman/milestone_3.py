# Milestone 3: Check if the guessed character is in the word

# Import packages

import random

# List of words for the computer to choose from
word_list = ["apple", "banana", "orange", "strawberry", "mango"]

# Select a random word from the word list
secret_word = random.choice(word_list)

def check_guess(guess):
    # Convert the guess into lower case
    guess = guess.lower()
    
    # Check if the guess is in the word
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')


def ask_for_input():
    guess = None
    while True:
        # Introduce the guess character
        guess = input('Introduce a letter: ')
        if guess.isalpha() and len(guess) == 1: # Check if the guess has lenght 1 and is in the alphabetical order
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    # Call the check_guess function to check if the guess is in the word     
    check_guess(guess)     

ask_for_input() # Call the ask_for_input function






