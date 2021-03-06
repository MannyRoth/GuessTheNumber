"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


#function resets the amount of tries
def number_of_attempts():
    attempts = 0 
    random_number_generator(attempts)


#resets the number you guess
def random_number_generator(attempts):
    random_number = random.randint(0,100)
    return start_game(random_number, attempts)


def start_game(random_number, attempts):
    answer = str(input('Welcome to the Number Guessing Game, Would you like to play?  ')).lower()
    try:
        if answer =="yes" or answer == "y":
            player_guess = int(input('Guess a number 1 to 100  ')) 
            return guess(player_guess,random_number,attempts)
        elif answer == "n" or answer =="no":
            print('Maybe next time!')
            return(start_game(random_number,attempts ))
        else:
            print('Please type Yes or No')    
            return(start_game(random_number,attempts))
    except ValueError:
        print('Please type a number')
        return start_game(random_number, attempts)

#loop that resets until the correct answer is input, also tracks attempts
def guess(player_guess, random_number, attempts): 
   
    attempts = attempts + 1
    try:
        if player_guess > random_number:
            player_guess = int(input('Too High! Guess again.   '))
            return guess(player_guess, random_number, attempts)
        
        
        elif player_guess < random_number:
            player_guess = int(input('Too Low! Guess again.   '))
            return guess(player_guess, random_number, attempts)

        else:
            print('CORRECT ANSWER!')
            print (f'You got it right in {attempts} tries!')
            return play_again(attempts)
    except ValueError:
        print('Please type a number')
        return guess(player_guess, random_number, attempts)
            
#function to either exit or restart game
def play_again(attempts):
    reply = input('Would you like to play again?   ')
    if reply == "n" or reply =="no":
            print('Hope you had FUN!')
            exit()
    elif  reply == "y" or reply =="yes":
            return number_of_attempts()
    else:
            print('Please say Yes or No')

    




number_of_attempts()