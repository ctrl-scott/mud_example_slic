import json
import random
import os

# Load history and NPC data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

with open(os.path.join(DATA_DIR, "history_snippets_depre.json")) as f:
    history_data = json.load(f)

with open(os.path.join(DATA_DIR, "npcs_depre.json")) as f:
    npc_data = json.load(f)

def enter_region(player):
    region = player.region
    print(f"\nYou have entered {region}.")

    # Display historical fact
    if region in history_data:
        print("Local History Flashback:", random.choice(history_data[region]))

    # Show a local NPC
    if region in npc_data:
        npc = random.choice(npc_data[region])
        print(f"You encounter {npc['name']}.")
        print(f"Description: {npc['description']}")
    else:
        print("This region seems oddly deserted...")