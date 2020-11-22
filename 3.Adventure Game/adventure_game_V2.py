import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


animals = ["lion", "tiger"]
animal = random.choice(animals)
results = ["win", "lose"]
result = random.choice(results)


def intro():
    print_pause("welcome")
    print_pause("This is the best game")


def game(items):
    while True:
        start = input(
            "Do you want to go to the forest or desert? \n"
            "if you want forest enter 1 \n"
            "if you ant desert enter 2"
        )
        if start == "1":
            forest(items)
            break
        elif start == "2":
            desert(items)
            break
        else:
            print_pause("Sorry, I don't understand.")
            break
        print_pause("Start game !")
        print_pause(
            "you will find a wild animale take care"
        )


def forest(items):
    print_pause("you will find a wild animale take care")
    print_pause(f"now you faces {animal}.\n")
    print_pause("Kill it !!")
    print_pause(f"you {result}")


def desert(items):
    print_pause("you will find a wild animale take care")
    print_pause(f"now you faces {animal}")
    print_pause("Kill it !!")
    print_pause(f"you {result}")


def play_again():
    while True:
        option = input(
            "Would you like to play agian? "
            "Please say 'yes' or 'no'.\n"
        )
        if option == "no":
            print_pause("OK, goodbye!")
            break
        elif option == "yes":
            print_pause("let's start!")
            play_game()
            break
        else:
            print_pause("good luck")
            play_again()
            break


def play_game():
    items = []
    intro()
    game(items)
    play_again()


play_game()
