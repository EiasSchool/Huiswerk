import time
import sys
import random

def print_slow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("")

def start_game():
    print_slow("\033[1;33mWelcome to The Lost Treasure of Eldoria!\033[0m")
    print_slow("You are a brave adventurer seeking the legendary treasure hidden within the ruins of Eldoria.")
    first_choice()

def first_choice():
    print_slow("Do you enter the ruins through the dark cave or take the narrow mountain path?")
    print("1. Enter the dark cave")
    print("2. Take the narrow path")
    choice = input("Choose (1/2): ")
    if choice == "1":
        cave_path()
    elif choice == "2":
        mountain_path()
    else:
        print_slow("Invalid choice. Try again.")
        first_choice()

def cave_path():
    print_slow("You enter the cave. It's dark and damp. You see an ancient scroll on the ground.")
    print("1. Pick up the scroll")
    print("2. Ignore it and move forward")
    choice = input("Choose (1/2): ")
    if choice == "1":
        print_slow("You pick up the Scroll of Eldoria! It might be useful later.")
        scroll = True
    else:
        print_slow("You ignore the scroll and continue.")
        scroll = False
    bridge_crossing(scroll)

def mountain_path():
    print_slow("The narrow path is treacherous. You barely avoid falling rocks before reaching an old bridge.")
    bridge_crossing(False)

def bridge_crossing(scroll):
    print_slow("You arrive at a broken bridge. Do you take the risk or find another way?")
    print("1. Cross the bridge")
    print("2. Find another path")
    choice = input("Choose (1/2): ")
    if choice == "1":
        if random.randint(1, 2) == 1:
            print_slow("The bridge collapses! You fall into the abyss. Game Over.")
        else:
            print_slow("You carefully cross the bridge and reach the treasure chamber.")
            treasure_room(scroll)
    else:
        print_slow("You find a hidden passage leading safely to the treasure room.")
        treasure_room(scroll)

def treasure_room(scroll):
    print_slow("You stand before a giant door with strange carvings. A guardian statue blocks the way.")
    print("1. Fight the guardian")
    print("2. Use the Scroll of Eldoria" if scroll else "2. Try to sneak past")
    choice = input("Choose (1/2): ")
    if choice == "1":
        print_slow("The guardian is too powerful! You are defeated. Game Over.")
    else:
        if scroll:
            print_slow("You use the Scroll of Eldoria to deactivate the guardian! The path is clear.")
        else:
            if random.randint(1, 2) == 1:
                print_slow("The guardian spots you and attacks! Game Over.")
                return
        final_choice()

def final_choice():
    print_slow("You reach the treasure chest. A keyhole glows in the center.")
    print("1. Use the Ancient Key to unlock it")
    print("2. Try to force the chest open")
    choice = input("Choose (1/2): ")
    if choice == "1":
        print_slow("You unlock the chest and claim the lost treasure of Eldoria! YOU WIN!")
    else:
        print_slow("A hidden trap triggers, and the ruins collapse on you. Game Over.")

if __name__ == "__main__":
    start_game()
