#GUESSING GAME
"""
[✔]a player
[]a static secret number solved by figuring out the riddle
[]numbers ranging from 1 to 30 only
[✔]a random number
[✔]Win condition and fail condition
[✔]limited guess
"""

import colorama
from colorama import Fore,Style

#guess_limit = 4 #total of 5
#valid_inputs = [range(1,30)]
#print(valid_inputs)

RIDDLE_NUMBER = "21"
number_of_guess = 5

from random import choice


player = input("Register Name: ").title()

print("\n\n\n")

print("It's morb---Guessing time!")

print("""The game is simple, it will generate a random number for you to guess but before that, try to solve this riddle(or not I'm not a cop)\n
        If seven people meet each other, and each shakes hands only
        once with each of the others, how many handshakes will there
        have been?\n""")
first_guess = input(f"Your guess here my good Sir/Lady: ")

def guessingGameFirstGuess():
    if first_guess == RIDDLE_NUMBER:
        print(f"WOW! You guessed it right on the first try!\nYou must be a genius or something, definitely not luck based.\n{Fore.GREEN}{Style.BRIGHT}Congratulations {player}{Style.RESET_ALL}!")
    else:
        print("Oopsy you guessed wrong.\n\nThe game will now begin\n")
        guessingGame()
        #while number_of_guess > 0:


def guessingGame():
    # numbers = [
    # "1","2","3","4","5","6","7","8","9","10",
    # "11","12","13","14","15","16","17","18","19","20",
    # "21","22","23","24","25","26","27","28","29","30"]


    # valid_inputs = {1,2,3,4,5,6,7,8,9,10,
    #             11,12,13,14,15,16,17,18,19,20,
    #             21,22,23,24,25,26,27,28,29,30}
    #print(f"valid print {valid_inputs}")
    #print(type(valid_inputs))

    numbers = [1,2,3,4,5,6,7,8,9,10,
            11,12,13,14,15,16,17,18,19,20,
            21,22,23,24,25,26,27,28,29,30]


    random_number = choice(numbers) #read about randint from random module
    number_of_guess = 10
    #print(random_number)


    if input("Input a number ranging from 1 to 30 only: ") == random_number:
            print("Congratulations You Won!")
    else:
        while number_of_guess > 0:
            if number_of_guess == 10:
                print("""
Wow you didn't get it on your first try? Unbelievable.
You know I was really hoping that you were the next Einstein or something. sadcxzc
I'll give you 5 more tries and a little nudge along the way.\n""")


            #guesses = input(f"You have {number_of_guess} guesses left. Please guess again: ")
            guess_input = input(f"You have {number_of_guess} guesses left. Please guess again: ")
            guesses = int(guess_input)
            number_of_guess -= 1


            if guesses == random_number:
                print(f"{Fore.GREEN}{Style.BRIGHT}Congratulations {player} You Won!{Style.RESET_ALL}")
                break
            elif guesses > random_number:
                 print("Too high!")
            elif guesses < random_number:
                 print("Too low!")


        else:
            print(f"Out of Guesses! Quite Unfortunate {Fore.RED}{Style.BRIGHT}{player}{Style.RESET_ALL}")
            print(f"The hidden number was {Fore.MAGENTA}{random_number}{Fore.RESET}")



#make a scenario here then call the function guessingGameFirstGuess
guessingGameFirstGuess()

#if number_of_guess == guess_limit:
#    print("You lose")