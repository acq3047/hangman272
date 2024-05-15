# Hangman

![All text](https://github.com/acq3047/hangman272/blob/main/hangman_image.jpeg)

# Table of contents
1. [Description](#description)
2. [Milestone 1: Set up the environment](#milestone-1-set-up-the-environemnt)
3. [Milestone 2: Create the variables for the game](#milestone-2-create-the-variables-for-the-game)
    - [Task 1: Define the list of possible words](#task-1-define-the-list-of-possible-words)
    - [Task 2: Choose a random word from the list](#task-2-choose-a-random-word-from-the-list)
    - [Task 3: Ask the user for an input](#task-3-ask-the-user-for-an-input)
    - [Task 4: Check out that the input is a single character](#task-4-check-out-that-the-input-is-a-single-character)
    - [Task 5: Upadate the latest code changes to GitHub](#task-5-update-the-latest-code-changes-to-github)
4. [Milestone 3: Check if the guessed character id in the word](#milestone-3-check-if-the-guessed-character-is-in-the-word)
    - [Task 1: Iteratively check if the input is a valid guess](#task-1-iteratively-chech-if-the-input-is-a-valid-guess)
    - [Task 2: Check wether the guess is in the word](#task-2-check-wether-the-guess-is-in-the-word)
    - [Task 3: Create functions to run the check](#task-3-create-functions-to-run-the-check)
    - [Task 4: Update the latest code changes to GitHub](#task-4-update-the-latest-code-changes-to-github)
5. [Milestone 4: Create the game class](#milestone-4-create-the-class)
    - [Task 1: Create the class](#task-1-create-the-class)
    - [Task 2: Create the methods for running the checks](#task-2-create-the-methods-for-running-the-checks)
    - [Task 3: Define what happens if the letter is in the word](#task-3-define-what-happens-if-the-letter-is-in-the-word)
    - [Task 4: Define what happens if the letter is not in the word](#task-4-define-what-happens-if-the-letter-is-not-in-the-word)
    - [Task 5: Update the latest code changes to GitHub](#task-5--update-the-latest-code-changes-to-github)
6. [Milestone 5: Putting all together](#milestone-5-putting-all-together)
    - [Task 1: Code the logic of the game](#task-1-code-the-logic-of-the-game)
    - [Task2: Update the latest code changes to GitHub](#task-2-update-the-latest-code-changes-to-github)
7. [License](#license)


## Description

The hangman game, a traditional word-guessing activity, is not just a game. It's a captivating intellectual exercise that challenges participants' vocabulary and deductive skills. This uncomplicated yet stimulating game provides a platform for students to engage their minds, making it a valuable and intellectually stimulating exercise.

The primary aim of this project is to develop a sophisticated programming code that enables the user to iteratively guess the word randomly chosen by the computer until the allotted attempts are exhausted. This endeavour involves the creation of four distinct files to progressively construct the code, with an incremental level of complexity from a simple *if-else* statement to the implementation of a *class* incorporating the necessary logic and processing for optimal game performance.

Furthermore, this project is not just about the hangman game. It's an invaluable learning opportunity for participants to delve deeper into fundamental programming concepts such as data types, control flow, loops, functions, and user input handling. These concepts, which have been covered in preceding course modules, are crucial for their programming journey, emphasizing the value and relevance of this project.

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

## Milestone 4: Create the game class

In this milestone, we proceed proceed to use the Object Oriented Programming (OOP) paradigm to develop to complete a Hangman game.

### Task 1: Create the class

In this task, we proceed to create another python file callled **milestone_4.py** in which we proceed to create a class called **Hangman** to contain the required proccesss to create a complete Hangman game.

1. Create a class called **Hangman**
2. Create the contruction method (__init__) to initialise the attributes of the class which are **word_list** and **num_lives**
3. Initialise the attributes:
    - **word**: The word to be guessed, picked randomly from the word_list.
    - **word_guessed**: list - A list of the letters of the word, with _ for each letter not yet guessed.
    - **num_letters**: int - The number of unique letters in the word that have not been guessed yet
    - **num_lives**: int - The number of lives the player has at the start of the game which in this case, we specified as 5
    - **word_list**: list - A list of words
    - **list_of_guesses**: list - A list of the guesses that have already been tried. Set this to an empty list initially

```python
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
```

### Task 2: Create the methods for running the checks

In this task, we willproceed to create a method that will ask the user to guess a letter and another method that will check if the guess is in the word.

1. Define a method called **check_guess** which has *guess* as parameter.
    - Convert the guessed letter to lower case.
    - Create an if statement that checks if the guess is in the word.
    - In the body of the if statement, print a message saying "Good guess! {guess} is in the word.".
2. Define a method called **ask_for_input**. 
    - Create a while loop and set the condition to True.
    - Ask the user to guess a letter and assign this to a variable called *guess*.
    - Create an if statement that runs if the guess is not a single alphabetical character.
    - In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character.".
    - Create an elif statement that checks if the guess is already in the **list_of_guesses**.
    - In the body of the elif statement, print a message saying "You already tried that letter!"
    - If the guess is a single alphabetical character  is not in **list_of_guesses**, create an else block and call the               **check_guess** method. 
    - Append the *guess* to the **list_of_guesses**.

```python
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Testing the code
hangman_game = Hangman(["apple", "banana", "orange"])
hangman_game.ask_for_input()
```

### Task 3: Define what happens if the letter is in the word

In this task, we proceed to extend the **check_guess** method to replace the underscore(s) in the **word_guessed** with the letter guessed by the user.

1. After the print statement, Create a for-loop that will loop through each letter in the **word**.
2. Within the for-loop, do the following:
    - Create an if statement that checks if the letter is equal to the guess
    - In the if block, replace the corresponding "_" in the **word_guessed** with the guess.
3. Outside the for-loop, reduce the variable **num_letters** by 1

```python
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Testing the code
hangman_game = Hangman(["apple", "banana", "orange"])
hangman_game.ask_for_input()
print("Word guessed so far:", hangman_game.word_guessed)
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Testing the code
hangman_game = Hangman(["apple", "banana", "orange"])
hangman_game.ask_for_input()
print("Word guessed so far:", hangman_game.word_guessed)
```

### Task 4: Define what happens if the letter is not in the word

In this task, we proceed to define what happens if the guess is not in the word you are trying to guess.

1. In the **check_guess method**, Create an else statement.
2. Within the else block:
    - Reduce **num_lives** by 1.
    - Print a message saying "Sorry, {letter} is not in the word.".
    - Print another message saying "You have {self.num_lives} lives left."

```python
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1 # Deduction of one attemp in the num_lives attribute
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Testing the code
hangman_game = Hangman(["apple", "banana", "orange"])
hangman_game.ask_for_input()
print("Word guessed so far:", hangman_game.word_guessed)
```

### Task 5:  Update the latest code changes to GitHub 

Update your GitHub repository with the latest code changes from your local project.

1. Staging your modifications and creating a commit.
2. Push the changes to your GitHMub repository

## Milestone 5: Putting all together

In this milestone, we proceed to introduce make the final adjustments of the code to make it work as expected by the introduction of the logic conditions that will specify the conditons that are required to make the code work.

### Task 1: Code the logic of the game

In this task, we proceed to create a script capable to execute the Hangman game as expected. To do it, we decided to create another file called **milestone_5py** 
in whcih we copy the **Hangman** class created in the **milestone_4.py** file and we proceed to create an additional function that will make the game works as usual.

1. Create a function called **play_game** that takes *word_list* as a parameter.
2. Specify the **num_lives** as 5.
3. Create a variable called **game** that will called an instance of the **Hangman** class which has **word_list** and **num_lives** as arguments.
4. Create a while loop and set the condition to True. In the body of the loop, do the following:
    - Check if the **num_lives** is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'
    - Next, check if the **num_letters** is greater than 0. In this case, you would want to continue the game, so you need to call the ask_for_input method.
    - If the **num_lives** is not 0 and the **num_letters** is not greater than 0 Print a message saying 'Congratulations. You won the game!'
5. In the **Hangman** class modify the **ask_for_input** method to make it work when the **num_lives** and **num_letters** are greather than 0.
6. Outside the function, call your **play_game** function to play your game which has a list of words as argument to the function

```Python
import random

# Create a class called Hangman

class Hangman:
    '''
    This class is used to create an interpretation code of the Hangman game.

    Attributes:
        word_list (list of strings): The list of words that the computer can choose for the game.
        num_lives (int): The number of attemps that are available for guessing the word.
        word (string): The word randomly chosen by the computer.
        word_guessed (list of strings): List in which the letters of the word to guess is introduced in the same index as in the word.
        num_letters (int): The number of letters that form the word chosen by the computer.
        list_of_guesses (list of strings): List that contains all the letters guessed by the user.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        This method is used to check if the letter provided by the user is in the word chosen by the computer.

        In the case the guess is in the word the letter is introduce in the word_guessed list in the same position
        as the position that appear in the word.

        However, in the case the letter is not in the word, we dedeucted one attempt of the num_lives.
        '''
        guess = guess.lower() # Convert the user guess to lower case.
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i, letter in enumerate(self.word): # For loop to iterate the letter position in the word selected by the computer.
                if letter == guess:
                    self.word_guessed[i] = guess
                    print(self.word_guessed)
            self.num_letters -= 1
            print('Number of letters left:')
            print(self.num_letters)
        else:
            self.num_lives -= 1 # Deduction of one attemp in the num_lives attribute
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    
    def ask_for_input(self):
        '''
        This method is used to ask the user to introduce a letter along with the checking if the guess of the user is an
        alphabetical character and if the user has not introduce more than one character.

        In the case the letter has passed the check, we introduced into the list_of_guesses in which we store all the letters that the
        user has guessed in which there is no repetitive letters.

        Finally, if the letter is not in the list_of_guesses, we pass the guess to the check_guess method.
        '''
        while self.num_lives > 0  and self.num_letters > 0:
            guess = input('Introduce a letter: ')
            if len(guess) !=1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print('Letters used:')
                print(self.list_of_guesses) # Show in the display the list that contains the words already used
                


# Testing the code

# Create ply_game method

def play_game(word_list):
    '''
    This function is used to run all the code to execute the game as expected.

    The purpose of this function is based on the execution of the Hangman game.
    To do it we decided to call the class Hangman into the function having 
    word_list and mum_lives with the objective to iteratively guess
    the word selectec by the computer before the num_lives becomes 0
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break

        if game.num_letters > 0: # This statement works when the number of letters to guess are greather than 0
            game.ask_for_input()
        else: 
            print('Congratulations. You won the game!')
            break
    
            
# Testing the code

if __name__ == '__main__':  # Execute the code by calling play_game function only when we run this file directly
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon', 'pinapple', 'peach', 'melon']
    play_game(word_list)
```

### Task 2: Update the latest code changes to GitHub

Update your GitHub repository with the latest code changes from your local project.

1. Staging your modifications and creating a commit.
2. Push the changes to your GitHMub repository

## License

When this project's repository was initially established, it was deliberately left unlicensed. This decision allows users to utilize, adapt, and distribute the code without encountering any constraints or limitations.

