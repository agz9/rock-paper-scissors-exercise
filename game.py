# game.py

# a game simulating rock, paper, scissors 
# with the user competing with the computer

import os
import random
from dotenv import load_dotenv

load_dotenv() #invokes/uses the function we got from the third party package

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One") # uses os module to read name

print("-------------------")
print(f"Welcome {Player One} to my Rock-Paper-Scissors game...")
print("-------------------")
# introduces the user to the game 

user_choice=input("Please choose either 'rock', 'paper', or 'scissors': ")
# asks the user to choose one of the options 
rock_paper_scissors_list=['rock', 'paper', 'scissors']
# a list of the different choices for the game
computer_choice=random.choice(rock_paper_scissors_list)
# the computer will randomly choose from the above list of choices 

# a series of conditionals for different user and computer choices 
if user_choice == "rock":
    # the second if statement is nested inside of the first, allowing for there to be more conditions
    if computer_choice == "rock":
        print("You and the computer chose rock, so it's a tie!")
        # the user and the computer chose the same choice of "rock"
    elif computer_choice == "paper":
    # elif means else if, so allows there to be variations from the if clause
        print("You chose rock. The computer chose paper and won! Sorry!")
    elif computer_choice == "scissors":
        print("You chose rock and won! The computer chose scissors. Nice job.")
    print("Thanks for playing. Please play again!")
    # this print statement will come at the end of the game, no matter what the computer chose
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You chose paper and won! The computer chose rock. Nice job.")
    elif computer_choice == "paper":
        print("You and the computer chose paper, so it's a tie!")
        # the user and the computer chose the same choice of "paper"
    elif computer_choice == "scissors":
        print("You chose paper. The computer chose scissors and won! Sorry!")
    print("Thanks for playing. Please play again!")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("You chose scissors. The computer chose rock and won! Sorry!")
    elif computer_choice == "paper":
        print("You chose scissors and won! The computer chose paper. Nice job.")
    elif computer_choice == "scissors":
        print("You and the computer chose scissors, so it's a tie!")
        # the user and the computer chose the same choice of "scissors"
    print("Thanks for playing. Please play again!")
else:
    print("OOPS SOMETHING WENT WRONG.")
    # this message will come up if the user says anything besides rock, paper, or scissors

exit()
# will exit out of the program completely 