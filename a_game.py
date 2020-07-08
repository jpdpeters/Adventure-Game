import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in a dark forest.")
    print_pause("Rumor has it there are some scary creatures "
                "creeping around these trees.")
    print_pause("...")
    print_pause("crack")
    print_pause("...")
    print_pause("A sound came from the bushes. You are not alone. "
                "You should move.")
    print_pause("You look left and right. To your left, there is a"
                " path to a small town. To your right, there is a small"
                " road leading to a cave.")

def fight(items):
    print_pause("You choose to fight!")
    if "sword" in items:
        print_pause("You draw the sword the people of the twon gave you.")
        print_pause("The trolls don't stand a chance. After a few hits "
                    "with your sword, they give up and run away, never to be "
                    "seen again.")
    else:
        print_pause("The trolls are way too strong. They overpower you and will"
                    " keep you as their pet.")

def run(items):
    print_pause("You choose to run!")
    print_pause("You are back where you started!")
    choose_path(items)

def trolls(items):
    num = random.randint(2, 99)
    print_pause(num, " trolls come out of the cave! They look like they are ready "
                " to fight! What will you do?") #how to loop this correctly so print does not come up again?
    reaction = input("1. Fight\n"
                  "2. Run and hide\n")
    if reaction == '1':
        fight(items)
    elif reaction == '2':
        run(items)
    else:
        print_pause("Sorry, that is not an option. Please choose again.")
        trolls()

def left(items):
    print_pause("You turn left towards the small town.")
    print_pause("After a few moments, you find "
                "yourself in the town square.")
    if "sword" in items:
        print_pause("The town welcomes you back, but you already "
                    "collected the sword, so there is nothing "
                    "more we can do for you.")
    else:
        print_pause("The town welcomes you and proclaims you their savior!")
        print_pause("For years, trolls have terrorized them, but now "
                    "their brave hero has shown up to free them!")
        print_pause("The mayor hands you a sword to defeat the trolls.")
        items.append("sword")
    print_pause("You head back to the forest.")
    choose_path(items)

def right(items):
    print_pause("You turn right towards the cave.")
    print_pause("After a short walk you arrive in front of the dark hole.")
    trolls(item)

def choose_path(items):
    print_pause("Please enter the number for the "
                "path you would like to choose:")
    path = input("1. Left to the twon\n"
                  "2. Right to the cave\n")
    if path == '1':
        left(items)
    elif path == '2':
        right(items)
    else:
        print_pause("Sorry, I don't understand, choose again.")
        choose_path(items)

def play_game():
    items = []
    intro()
    choose_path(items)


play_game()
