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

# === player.py ===
class Player:
    def __init__(self, name, pronouns, orientation, region):
        self.name = name
        self.pronouns = pronouns
        self.orientation = orientation
        self.region = region
        self.reputation = 50
        self.health = 100
        self.infection_status = []
        self.history = []

# === regions_notmodular.py ===
import random

regions = {
    "Suburbia": {
        "history": "Post-WWII white flight, 2008 housing crisis, COVID lockdowns.",
        "risk": {"crime": 0.2, "disease": 0.15},
        "npcs": ["Divorcee (38)", "HOA President", "Disillusioned Realtor"]
    },
    "Urban Core": {
        "history": "1969 Stonewall, 2020 protests, gentrification displacements.",
        "risk": {"crime": 0.35, "disease": 0.2},
        "npcs": ["Queer Activist", "Artist (nonbinary)", "Club Promoter"]
    },
    "Rural Outskirts": {
        "history": "Factory shutdowns, militia rises, 2016 election impacts.",
        "risk": {"crime": 0.4, "disease": 0.25},
        "npcs": ["Hunter", "Opioid Survivor", "Veteran (PTSD)"]
    },
    "Squatter Zone": {
        "history": "Occupy movement, anarchist collectives, eviction zones.",
        "risk": {"crime": 0.5, "disease": 0.3},
        "npcs": ["Street Medic", "Punk Nomad", "Burner"]
    }
}

def enter_region(player):
    region = regions[player.region]
    print(f"\n-- Entering {player.region} --")
    print(f"Historical Context: {region['history']}")
    print(f"You encounter: {random.choice(region['npcs'])}")

    if random.random() < region['risk']['crime']:
        print("\nYou were mugged by a stranger. Reputation -10.")
        player.reputation -= 10

    if random.random() < region['risk']['disease']:
        print("\nYou've contracted a minor illness. Health -10.")
        player.health -= 10
        player.infection_status.append("Unknown Illness")

# === chat.py ===
def chat_encounter(player):
    print("\nA stranger messages you on LoveLink...")
    responses = [
        "Your aura reads like a Netflix queue I’d binge.",
        "Are you emotionally available or just bored?",
        "I’m looking for something... radical. Like socialism but sexy.",
        "Tell me one historical event that shaped your love life."
    ]
    print("They say:", random.choice(responses))
    action = input("Respond with /flirt, /truth, or /block: ")

    if action == "/flirt":
        print("They flirt back. You gain +5 reputation.")
        player.reputation += 5
    elif action == "/truth":
        print("They appreciate your honesty. You gain +10 reputation.")
        player.reputation += 10
    elif action == "/block":
        print("You blocked them. No harm done.")
    else:
        print("Unrecognized action. The moment passes.")

# === main.py ===
import time
from player import Player
from old_files.regions_notmodular import enter_region
from chat import chat_encounter

def start_game():
    print("Welcome to Heartland Crawl")
    name = input("Enter your name: ")
    pronouns = input("Your pronouns (e.g. they/them): ")
    orientation = input("Your orientation (e.g. bisexual): ")
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
