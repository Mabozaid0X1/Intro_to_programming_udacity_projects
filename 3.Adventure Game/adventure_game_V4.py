import time
import random

# this is the function which gives the user some time to read!
def print_pause(
    message_to_print
):
    print(message_to_print)
    time.sleep(2)

# here is a list that includes some kinds of sights.
prizes = [
    " chocelate",
    " lollipop",
    " dessert",
    " present",
    " kiss",
]
rewards = random.choice(prizes)
sights = [
    " giant buildings",
    " beautiful animals",
    " fountains",
    " old houses",
]
views = random.choice(sights)


# this is the intro of the game
def intro():  
    print_pause("Welcome! \n")
    print_pause("I'm Rana, \n")
    print_pause(
        "Can you help me to deliver food to my grandmother, \n"
    )
    print_pause(
        "on the other side of town. \n"
    )

# it tells you what happens when you are at home
def ways(
    items
):
    print_pause(
        "Please enter the number for the \n"
    )
    print_pause(
        "way I will go: \n"
    )
    print_pause(
        "1. The way of the forest \n"
    )
    print_pause(
        "2. Across the city \n"
    )
    while True:
        que = input("Please choose 1 or 2 \n").lower()
        if que == "1":
            road_1(items)
            break
        elif que == "2":
            road_2(items)
            break

# it tells you what happens when you are at work
def road_1(
    items
):
    print_pause(
        "Oops I've missed the way \n"
    )
    print_pause(
        "Would you like to ask someone about the way ?\n"
    )
    print_pause("1.yes \n")
    print_pause("2.no \n")
    while True:
        que = input("please write yes or no! \n").lower()
        if que == "yes":
            asking(items)
            break
        elif que == "no":
            print_pause("I don't understand you!")
            break
        else:
            print_pause("fail")
            road_1()
            break

# it tells you what happens when you want to go fishing, but you havn't worked
def asking(items):
    print_pause(
        "One of them showed me on the way, \n"
    )
    print_pause(
        "and came to my grandmother's house \n"
    )
    print_pause(
        "we arrived there \n"
    )
    print_pause(
        f"my grandmother gave me a {rewards} ! \n"
    )
    print_pause(
        "you won the game\n"
    )


# it tells you what happens when you want to go fishing after working
def failing(items):
    print_pause(
        "Rana lost the way \n"
    )
    print_pause(
        "she couldn't get to her grandmother's house \n"
    )
    print_pause(
        "she felt bad now! \n"
    )
    print_pause(
        "you lost the game\n"
    )

# it tells you what happens when force the seller to give you a hook
def road_2(items):
    print_pause(
        "Rana knows the way well from here!\n"
    )
    print_pause(
        f"She enjoys watching {views}! \n"
    )
    print_pause(
        "she arrived at her grandmother's house \n"
    )
    print_pause(
        "you won the game!\n"
    )
    ways(items)

def again():
    while True:
        que = input(
            "Do you want to play again ? (y/n) \n"
        ).lower()

        if que.lower() == "n":
            print_pause(
                "Ok , have a great time!"
            )
            break
        elif que.lower() == "y":
            print_pause(
                "Excellent! Restarting the game ..."
            )
            play_the_game()
            break
        else:
            print_pause("Fail")
            play_the_game()
            break

# this function starts the game
def play_the_game():
    items = []
    intro()
    ways(items)
    again()


play_the_game()
