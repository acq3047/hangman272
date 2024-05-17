# Milestone 2: Create the variables for the game

# Imported packages
import random

# Task 1: Define the list of possible words

fruit_list = ['apple', 'strawberry', 'grape', 'orange', 'pinaple'] # List of my 5 favourite fruits
word_list = fruit_list
print(word_list)

# Task 2: Choose a random word from the list

choice = random.choice(word_list) # We use the choice method to allos the computer to randomly choose between the words in the list
print(choice)

# Task 3: Ask the user for an input

guess = input('Enter a single letter: ')

# Task 4: Check out that the input is not a single character

if len(guess) == 1: # Check that the input has only contains one character
    print('Good guess!')
else:
    print('Oops! That is not a valid input')
