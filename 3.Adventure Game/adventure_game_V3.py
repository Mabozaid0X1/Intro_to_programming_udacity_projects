import time

import random


def print_pause(message_to_print, wait = 2):
    print(message_to_print)
    time.sleep(wait)
danger = ["lion", "armed man"]
animal = random.choice(danger)
results = ["win", "lose"]
result = random.choice(results)
def opening():
    print_pause("Welcome to Adventure Game!.\n")
    print_pause("This is the best game ever!.\n")
    print_pause("Start game !\n")
    print_pause("You are now landing by Helicopter.\n")
    print_pause("You have landed on the ground.\n")
def game():
    while True:
        start= input("Do you want to go to the house or forest? \n"
                     "if you want house enter 1. \n"
                     "if you ant forest enter 2.\n"
        )
        if start == "1":
            house()
            break
        elif start == "2":
            forest()
            break
        else :
            print_pause("Sorry!,\n I don't understand what do you mean!")
            game()


            break
def house():
    while True:
        print_pause("You now ahead of house! \n")
        print_pause("if you want to broke the door and enter the"
                    "house ,please enter 1 \n")
        print_pause("if you want enter house from the behind the"                 
                    "door enter 2 \n")
        door = input("What would you like to do?\n"
                     "(Please enter 1 or 2.)\n")
        if door == "1":
            print_pause("Good! \n")
            print_pause("You had broken the door well.\n")
            print_pause("Ohhh nooo!\n"
                        "There is an armed man!")
            print_pause("kill him!")
            print_pause(f"you{result}!")
            break
        elif door == "2":
            print_pause("Oh that's amazing!\n"
                      "There is a treasure\n")
            print_pause("Get It !")
            print_pause("You WIN The GAME")
            print_pause("GOOD GAME")
            break
        else :
            print_pause("Sorry, I don't understand any thing!")
            house()
            break
def forest():
    while True:
        danger = input("You are now in the forest !\n"
                       "There is two ways that you can go.\n"
                       "if you want to go right ,please enter 1 \n"
                       "if you want go left enter 2 \n")
        if danger == "1":
            print_pause("You are now in the right way !"
                        "OMG!. There is a lion!\n")
            print_pause("kill him by your gun!")
            print_pause(f"you {result}!")
            break
        elif danger == "2":
            print_pause("There are many trees and beautiful herbs.\n"
                        "You are now safe.\n")
            print_pause("Congratulations you won !.")
            break
        else :
            print_pause("Sorry, I don't understand any thing!")
            forest()
            break
def play_again():
    while True:
        choise = input(
             "Would you like to play again? "
             "Please say 'yes' or 'no'.\n"
        )
        if choise == "no":
            print_pause("OK, goodbye!")
            break
        elif choise == "yes":
            print_pause("let's start!")
            play_game()
            break
        else:
            print_pause("good luck")
            play_again()
            break
           
def play_game():
    opening()
    game()
    play_again()
play_game()
 
        