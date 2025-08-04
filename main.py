from player import Player
from regions import enter_region
from factions import get_factions, describe_faction
import random

def choose_faction(player):
    print("\n=== Choose Your Faction ===")
    factions = get_factions()
    for i, name in enumerate(factions):
        print(f"{i+1}. {name}")
    print("0. Continue without joining a faction")

    while True:
        try:
            choice = int(input("Enter the number of your chosen faction: "))
            if choice == 0:
                print("\nYou chose to remain independent.")
                break
            elif 1 <= choice <= len(factions):
                selected = factions[choice - 1]
                print("\n" + describe_faction(selected))
                confirm = input("Join this faction? (y/n): ").strip().lower()
                if confirm == 'y':
                    player.join_faction(selected)
                    print(f"\nYou have joined the {selected}!\n")
                    break
                else:
                    print("Faction not joined. Choose again or press 0 to skip.")
            else:
                print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Welcome to Heartland Crawl\n")
    name = input("Enter your name: ")
    player = Player(name)

    choose_faction(player)

    # Example starting regions — can be randomized or selected
    available_regions = ["Suburbia", "Urban Core", "Rural Outskirts", "Squatter Zone"]
    player.region = random.choice(available_regions)
    enter_region(player)

    player.describe()

if __name__ == "__main__":
    main()
