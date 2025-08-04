# Heartland Crawl - Modular Text-Based Online Dating MUD Engine
#
# Sources and References:
# - Cohen, Lizabeth. *A Consumers' Republic: The Politics of Mass Consumption in Postwar America*. Vintage, 2003.
# - Klinenberg, Eric. *Palaces for the People: How Social Infrastructure Can Help Fight Inequality, Polarization, and the Decline of Civic Life*. Crown, 2018.
# - Gillon, Steven M. *The Long Shadow of the Great Recession: Economic Policy and the Future of the American Dream*. Polity, 2021.
# - Schulman, Sarah. *The Gentrification of the Mind: Witness to a Lost Imagination*. University of California Press, 2012.
# - Boyd, Danah. *It's Complicated: The Social Lives of Networked Teens*. Yale UP, 2014.
# - Turkle, Sherry. *Reclaiming Conversation: The Power of Talk in a Digital Age*. Penguin, 2015.
# - Centers for Disease Control and Prevention. "HIV Basics." www.cdc.gov/hiv/basics.
# - Pew Research Center. "The State of Online Dating in 2023." www.pewresearch.org.
# - OpenAI ChatGPT, model GPT-4, used to assist with code structure and game logic development.

# Heartland Crawl - Modular Text-Based Online Dating MUD Engine
# === main.py ===
import time
from player import Player
from old_files.regions_notmodular import enter_region
from chat import chat_encounter


def start_game():
    print("Welcome to Heartland Crawl")
    name = input("Enter your name: ")
    pronouns = input("Your pronouns (e.g. they/them): ")
    orientation = input("Your orientation (e.g. het, hom, bis): ")
    print("Choose a region: Suburbia, Urban Core, Rural Outskirts, Squatter Zone")
    region = input("Your starting region: ")


    player = Player(name, pronouns, orientation, region)




    for day in range(1, 6):
        print(f"\nDay {day} in {player.region}...")
        enter_region(player)
        chat_encounter(player)
        time.sleep(1)

    print("\nGame Over. Summary:")
    print(f"Reputation: {player.reputation}, Health: {player.health}")
    if player.infection_status:
        print(f"Infections: {', '.join(player.infection_status)}")
    else:
        print("You remained healthy.")

if __name__ == "__main__":
    start_game()
