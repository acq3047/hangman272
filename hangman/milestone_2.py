# Milestone 2: Create the variables for the game

# Imported packages
import random

# Task 1: Define the list of possible words
fruit_list = ['apple', 'strawberry', 'grape', 'orange', 'pinaple'] # List of my 5 favourite fruits
word_list = fruit_list
print(word_list)

# Task 2: Choose a random word from the list

choice = random.choice(word_list)
print(choice)

# Task 3: Ask the user for an input
guess = input('Enter a single letter: ')

if len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! That is not a valid input')
