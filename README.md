# Hangman

# Table of contents
1. [Description](#description)
2. [Milestone 1](#milestone-1-set-up-the-environemnt)
3. [Milestone 2](#milestone-2-create-the-variables-for-the-game)
    - [Task 1](#task-1-define-the-list-of-possible-words)
    - [Task 2](#task-2-choose-a-random-word-from-the-list)
    - [Task 3](#task-3-ask-the-user-for-an-input)
    - [Task 4](#task-4-check-out-that-the-input-is-a-single-character)
    - [Task 5](#task-5-update-the-latest-code-changes-to-github)
4. [Milestone 3](#milestone-3-check-if-the-guessed-character-is-in-the-word)
    - [Task 1](#task-1-iteratively-chech-if-the-input-is-a-valid-guess)
    - [Task 2](#task-2-check-wether-the-guess-is-in-the-word)
    - [Task 3](#task-3-create-functions-to-run-the-check)
    - [Task 4](#task-4-update-the-latest-code-changes-to-github)

## Description

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

The aim of this project is to create a simple interactive game using Python where players can have fun guessing words while practicing their vocabulary and logical deduction skills. This project also serves as a learning opportunity to understand fundamental concepts of programming such as data types, control flow, loops, functions, and user input handling.

## Milestone 1: Set up the environemnt

This section correspond to the first part of the project which consits on the creation on the repository of the project.

At the time of creating the repository, we decided to follow the following proccedure:

- Click on “Install Github App “ button on right panel on the Hangman project module of the AI Core portal. A new Github page will appear.
- Select the account on which you want to use for your AiCore projects
- On the next page, select the “All repositories“ checkbox.
- Click “Install & authorize“. You may be prompted to enter your password.
- Once the authorization and installation is complete, you can clone the created repository in the pyhton code editor that you have decided to use.

## Milestone 2: Create the variables for the game

This section requires basic knowledge of python commands, such as if-else statements.

### Task 1: Define the list of possible words

Create a file named **milestone_2.py**. This file will contain the code for the first milestone. In this task, we are going to create a list of words.

1. Create a list containing the names of your 5 favorite fruits.
2. Assign this list to a variable called word_list.
3. Print out the newly created list to the standard output (screen).

```python
# Task 1: Define the list of possible words

fruit_list = ['apple', 'strawberry', 'grape', 'orange', 'pinaple'] # List of my 5 favourite fruits
word_list = fruit_list
print(word_list)
```

### Task 2: Choose a random word from the list

This task of of the section consists on importing the random moduele, which is one of the Python's built-in modules, to select randomly one of the fruits that are in the list.

1. Import the random module
2. Create the random.choice method and pass the word_list variable into the choice method.
3. Assign the randomly generated word to a variable called word.
4. Print out word to the standard output. Run the code several times and observe the words printed out after each run.

```python
import random

# Task 1: Define the list of possible words

fruit_list = ['apple', 'strawberry', 'grape', 'orange', 'pinaple'] # List of my 5 favourite fruits
word_list = fruit_list
print(word_list)

# Task 2: Choose a random word from the list

choice = random.choice(word_list)
print(choice)
```

### Task 3: Ask the user for an input

In this task, you are required to take user input. The input() function that takes input from the screen. Note that the input function returns the user input in form of a string.

1. Using the input function, ask the user to enter a single letter.
2. Assign the input to a variable called guess.

```python
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
```

### Task 4: Check out that the input is a single character

In this section, we want to ensure  that only a single letter is entered and that only alphabetical characters are provided by the user.
To do this, create conditional checks that must be passed before the input can be accepted.

1. Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
2. In the body of the if statement, print a message that says "Good guess!".
3. Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.

```python
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

# Task 4: Check out that the input is not a single character

if len(guess) == 1: # Check that the input has only contains one word
    print('Good guess!')
else:
    print('Oops! That is not a valid input')
```

### Task 5: Update the latest code changes to GitHub
Update your GitHub repository with the latest code changes from your local project.

1. Staging your modifications and creating a commit.
2. Push the changes to your GitHMub repository

## Milestone 3: Check if the guessed character is in the word

In this milestone, we proceed to create a code capable of checking if the chosen letter by the user is in the word selected randomly by the computer.

### Task 1: Iteratively chech if the input is a valid guess

The first task of this milestone consists on create a python file called **milestone_3.py** in which check if the letter selected by the input is a valid guess by using the following proccedure:

1. Create a while loop and set the condition to True.
2. Ask the user to guess a letter and assign this to a variable called guess.
3. Check that the guess is a single alphabetical character by using Python's isalpha method to check if the guess is alphabetical.
4. If the guess passes the checks, break out the loop.
5. If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."

```python
while True:
    guess = input('Introduce a letter: ')
    if guess.isalpha():
        print('Your guess is in correct')
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
```

### Task 2: Check wether the guess is in the word

In this task, we proceeded to introduce in the code the capability of checking if the guess letter guessed by the user is in the randomly selected word by the computer.

1. Import the random module.
2. Create a list that contains words which is assigend to *word_list* variable.
3. Create a variable called *secret_word* in which we use the *random.choice* method to randomly select a word from *word_list*.
4. Create an if statement that checks if the guess is in the word.
5. In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". 
6. Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." 

```python
import random

word_list = ["apple", "banana", "orange", "strawberry", "mango"]

secret_word = random.choice(word_list)

while True:
    guess = input('Introduce a letter: ')
    if guess.isalpha() and len(guess) == 1:
        if guess in secret_word:
            print(f'Good guess! {guess} is in the word.')
            break
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
```

### Task 3: Create functions to run the check

In this task, we proceed to create two functions called **check_guess** and **called_for_input** in which we proceed to check if the guess is the randomly selected word chosen by the coputer and if the character introduced by the user is valid or not.

1. Define a function called **check_guess**. pass in the guess as a parameter for the function.
2. Convert the guess into lower case.
3. Move the code that you wrote to check if the guess is in the word into this function block.
4. Define a function called **ask_for_input**.
5. Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.
6. Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word.
7. Outside the function, call the ask_for_input function to test your code.

```python
def check_guess(guess):
    # Convert the guess into lower case
    guess = guess.lower()
    
    # Check if the guess is in the word
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')


def ask_for_input():
    while True:
        guess = input('Introduce a letter')
        if guess.isalpha() and len(guess) == 1:
            # Call the check_guess function to check if the guess is in the word
            check_guess(guess)
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

ask_for_input()
```

### Task 4: Update the latest code changes to GitHub

Update your GitHub repository with the latest code changes from your local project.

1. Staging your modifications and creating a commit.
2. Push the changes to your GitHMub repository
