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

Create a file named milestone_2.py. This file will contain the code for the first milestone. In this task, we are going to create a list of words.

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


