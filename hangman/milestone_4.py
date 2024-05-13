# Milestone 4: Create the game class

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
            self.num_letters -= 1
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
        while True:
            guess = input('Introduce a letter: ')
            if len(guess) !=1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)
                


# Testing the code
hangman_game = Hangman(["apple", "banana", "orange"])
hangman_game.ask_for_input()



