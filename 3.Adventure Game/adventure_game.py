import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)


enemy = ["troll", "dragon", "gorgon", "fairie", "pirate"]
wicked = random.choice(enemy)


def intro():
    print_pause(
        "You find yourself standing in an open field, "
        "filled with grass and yellow wildflowers."
    )
    print_pause(
        f"Rumor has it that a {wicked} is somewhere around here, "
        "and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty "
        "(but not very effective) dagger."
    )


def question(items):
    print_pause(
        "Enter 1 to knock on the door of the house."
    )
    print_pause("Enter 2 to peer into the cave.")
    while True:
        option = input(
            "What would you like to do?\n"
            "(Please enter 1 or 2.)"
        ).lower()
        if option == "1":
            home(items)
            break
        elif option == "2":
            cava(items)
            break


def home(items):
    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens and "
        f"out steps a {wicked} ."
    )
    print_pause(f"Eep! This is the {wicked}'s house!")
    print_pause(f"The {wicked} attacks you!")
    if "sword" not in items:
        print_pause(
            "You feel a bit under-prepared for this, "
            "what with only having a tiny dagger."
        )
    while True:

        position = input(
            "Would you like to (1) fight or (2) run away?"
        ).lower()

        if position == "1" and "sword" in items:
            print_pause(
                f"As the {wicked} moves to attack, you unsheath your new "
                "sword."
            )
            print_pause(
                "The Sword of Ogoroth shines brightly in your hand as you "
                "brace yourself for the attack."
            )
            print_pause(
                f"But the {wicked} takes one look at your shiny new toy and"
                "runs away!"
            )
            print_pause(
                f"You have rid the town of the {wicked}. You are victorious!"
            )
            break
        elif position == "1" and "sword" not in items:
            print_pause("You do your best...")
            print_pause(
                f"but your dagger is no match for the {wicked}."
            )
            print_pause("You have been defeated!")
            break
        elif position == "2":
            print_pause(
                "You run back into the field. Luckily, "
                "you don't seem to have been followed."
            )
            break


def play_again():
    while True:
        print_pause("GAME OVER!")
        res = input("Would you like to play again? (y/n)")
        if res.lower() == "n":
            break
        elif res.lower() == "y":
            print_pause(
                "Excellent! Restarting the game ..."
            )
            play_game()
            break


def cava(items):
    print_pause("You peer cautiously into the cave.")
    if "sword" not in items:
        print_pause(
            "It turns out to be only a very small cave."
        )
        print_pause(
            "Your eye catches a glint of metal behind a rock."
        )
        print_pause(
            "You have found the magical Sword of Ogoroth!"
        )
        print_pause(
            "You discard your silly old dagger"
            "and take the sword with you."
        )
        print_pause("You walk back out to the field.")
        items.append("sword")
    else:
        print_pause(
            "You've been here before, and gotten all the good stuff."
            "It's just an empty cava now"
        )
    question(items)


def play_game():
    items = []
    intro()
    question(items)
    play_again()


play_game()
