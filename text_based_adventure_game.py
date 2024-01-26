import time

def introduction():
    print("Welcome to the Enchanted Forest Adventure!")
    time.sleep(1)
    print("Your quest is to find the legendary Golden Unicorn.")
    time.sleep(1)
    print("Be prepared for magical encounters and tricky challenges.")

def make_choice(choices):
    print("\nChoose your action:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def enchanted_forest():
    print("\nYou enter the mystical Enchanted Forest.")
    time.sleep(1)
    print("The trees whisper ancient secrets, and magical creatures hide in the shadows.")

    choices = [
        "Follow the sparkling path",
        "Enter the dark cave",
        "Climb the giant tree",
        "Cross the mystical river"
    ]
    choice = make_choice(choices)

    if choice == 1:
        print("You decide to follow the sparkling path.")
        time.sleep(1)
        print("You encounter a friendly fairy who guides you deeper into the forest.")
        fairy_encounter()
    elif choice == 2:
        print("You bravely enter the dark cave.")
        time.sleep(1)
        print("Inside, you find a treasure chest guarded by a tricky leprechaun!")
        leprechaun_encounter()
    elif choice == 3:
        print("You decide to climb the giant tree.")
        time.sleep(1)
        print("From the top, you spot a magical portal to another realm.")
        portal_encounter()
    elif choice == 4:
        print("You choose to cross the mystical river.")
        time.sleep(1)
        print("A water nymph appears and challenges you to a dance-off.")
        dance_challenge()

def fairy_encounter():
    print("\nThe fairy leads you to a magical clearing.")
    time.sleep(1)
    print("In the clearing, you spot a talking rabbit and a magical door.")

    choices = ["Talk to the rabbit", "Open the magical door", "Play with the fairy", "Ask the fairy for a wish"]
    choice = make_choice(choices)

    if choice == 1:
        print("The rabbit shares a riddle with you.")
        time.sleep(1)
        print("Solve the riddle to proceed!")
        riddle_encounter()
    elif choice == 2:
        print("You open the magical door and find yourself in a garden of floating islands.")
        time.sleep(1)
        print("You navigate the islands to find the next clue.")
        island_challenge()
    elif choice == 3:
        print("You decide to play with the fairy and receive a magical blessing.")
        time.sleep(1)
        print("The fairy grants you the ability to understand the language of animals.")
        enchanted_forest()
    elif choice == 4:
        print("You ask the fairy for a wish.")
        time.sleep(1)
        print("The fairy grants your wish, and you find a bag of enchanted seeds.")
        enchanted_seeds_encounter()

def riddle_encounter():
    print("\nRiddle: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind.")
    answer = input("Your answer: ").lower()

    if answer == "echo":
        print("Correct! The rabbit is impressed. You may proceed.")
        island_challenge()
    else:
        print("Incorrect! The rabbit disappears, and you are lost in the forest.")
        time.sleep(1)
        print("Game over. The Enchanted Forest is too tricky for you.")

def leprechaun_encounter():
    print("\nThe leprechaun challenges you to a game of wit.")
    time.sleep(1)
    print("You need to outsmart the leprechaun to claim the treasure.")

    choices = ["Tell a joke", "Challenge to a riddle duel", "Offer a trade", "Sing a magical song"]
    choice = make_choice(choices)

    if choice == 1:
        print("You tell a joke, and the leprechaun bursts into laughter.")
        time.sleep(1)
        print("Congratulations! You claim the treasure.")
        golden_unicorn_encounter()
    elif choice == 2:
        print("You challenge the leprechaun to a riddle duel.")
        riddle_encounter()
    elif choice == 3:
        print("You offer a trade, and the leprechaun gives you a magical compass.")
        time.sleep(1)
        print("The compass points to the Golden Unicorn's lair.")
        golden_unicorn_encounter()
    elif choice == 4:
        print("You sing a magical song that enchants the leprechaun.")
        time.sleep(1)
        print("The leprechaun rewards you with the location of the Golden Unicorn.")
        golden_unicorn_encounter()

def portal_encounter():
    print("\nYou enter the magical realm through the portal.")
    time.sleep(1)
    print("The realm is filled with floating islands and colorful creatures.")

    choices = ["Explore the floating islands", "Visit the Crystal Castle", "Return to the Enchanted Forest", "Summon a flying creature"]
    choice = make_choice(choices)

    if choice == 1:
        print("You explore the floating islands and discover a hidden treasure.")
        time.sleep(1)
        print("Congratulations! You have gained a magical artifact.")
        enchanted_forest()
    elif choice == 2:
        print("You visit the Crystal Castle and meet the wise oracle.")
        time.sleep(1)
        print("The oracle reveals the location of the Golden Unicorn.")
        golden_unicorn_encounter()
    elif choice == 3:
        print("You decide to return to the Enchanted Forest.")
        enchanted_forest()
    elif choice == 4:
        print("You summon a flying creature to explore the realm.")
        time.sleep(1)
        print("You discover a hidden passage that leads to the Golden Unicorn.")
        golden_unicorn_encounter()

def dance_challenge():
    print("\nThe water nymph challenges you to a dance-off.")
    time.sleep(1)
    print("Dance to the rhythm of the enchanted forest to win her favor.")

    choices = ["Dance gracefully", "Improvise a magical dance", "Challenge to a dance duel", "Politely decline"]
    choice = make_choice(choices)

    if choice == 1:
        print("You dance gracefully, impressing the water nymph.")
        time.sleep(1)
        print("She rewards you with a magical potion that reveals the path to the Golden Unicorn.")
        golden_unicorn_encounter()
    elif choice == 2:
        print("You improvise a magical dance, and the forest responds with enchantment.")
        time.sleep(1)
        print("The path to the Golden Unicorn reveals itself.")
        golden_unicorn_encounter()
    elif choice == 3:
        print("You challenge the water nymph to a dance duel.")
        time.sleep(1)
        print("The nymph gracefully accepts, and you dance in harmony.")
        enchanted_forest()
    elif choice == 4:
        print("You politely decline, and the water nymph wishes you luck on your quest.")
        enchanted_forest()

def enchanted_seeds_encounter():
    print("\nThe enchanted seeds start glowing in your hands.")
    time.sleep(1)
    print("You plant the seeds, and magical plants instantly grow around you.")

    choices = ["Climb the magical vines", "Talk to the animated flowers", "Create a potion with the plants", "Continue on the path"]
    choice = make_choice(choices)

    if choice == 1:
        print("You climb the magical vines and discover a hidden platform.")
        time.sleep(1)
        print("From the platform, you see the Golden Unicorn in the distance.")
        golden_unicorn_encounter()
    elif choice == 2:
        print("You talk to the animated flowers and gain insights about the forest.")
        time.sleep(1)
        print("The flowers guide you towards the Golden Unicorn.")
        golden_unicorn_encounter()
    elif choice == 3:
        print("You create a potion with the plants and gain a temporary magical ability.")
        time.sleep(1)
        print("The ability helps you navigate the forest more efficiently.")
        enchanted_forest()
    elif choice == 4:
        print("You continue on the path, carrying the enchanted seeds with you.")
        enchanted_forest()

def golden_unicorn_encounter():
    print("\nYou follow the clues and finally reach the Golden Unicorn's lair.")
    time.sleep(1)
    print("The majestic creature greets you with a nod.")

    print("Congratulations! You have successfully found the Golden Unicorn and completed the quest.")

def main():
    introduction()
    enchanted_forest()

if __name__ == "__main__":
    main()
