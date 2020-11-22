import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

animals = [bear, snake]
evil = random.choice(animals)

def start():
    print_pause("You are now in a big green field\n")
    print_pause("On your right you will find a caven\n")
    print_pause("You'll find a house on your left\n")

def choice(items):
    print_pause("Enter 1 to knock on the door of the house.\n")
    print_pause("Enter 2 to peer into the cave.\n")
    while True:
        place = input(
            "What would you like to do?\n"
            "(enter 1 or 2.)")
        if place == "1":
            print_pause("you win the game")
            break
        elif place == "2":
            print_pause(f"you find a big {evil}\n")
            print_pause(f"The {evil} attack on you\n")
            print_pause(f"RUN...RUN...RUN\n")
            print_pause("GAME OVER\n")
            print_pause("You Lose")
            play_again()
            break
        
def play_again():
    while True:
        restart = input("Would you like to play again? ( yes / no )")
        if restart == "no":
            print_pause("good luck")
            break
        elif restart == "yes":
            print_pause("okay! Restarting the game ...")
            play_game0101()
            break
        else:
            play_again()
            break

def play_game0101():
    items = []
    start()
    choice(items)
    play_again()


play_game0101()

    