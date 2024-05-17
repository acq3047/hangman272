# Milestone 5: Putting all together

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

        The purpose of this metod is to check if the word provided by the user is in the word randomly
        selected by the computer by the developent of an 'if-else' statement.
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

        The puprpose of this method is to check if the letter provided by the user is suitable for the parameters of the game.
        These parameters are based in if the letter provided is in the alphabetical order and if the input is a single character by
        the develpment of an 'if-else' were the input guess needs to follow the parameters specified above.
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
    word_list_game = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon', 'pinapple', 'peach', 'melon']
    play_game(word_list_game)