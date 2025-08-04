import json
import random
import os
from factions import get_npc_reaction
from chat.reaction import respond_to_player


NPC_DATA_FILE = os.path.join("data", "npcs.json")
HISTORY_DATA_FILE = os.path.join("data", "history_snippets.json")

with open(NPC_DATA_FILE) as f:
    npc_data = json.load(f)

with open(HISTORY_DATA_FILE) as f:
    history_data = json.load(f)

available_regions = [
    "Suburbia",
    "Urban Core",
    "Rural Outskirts",
    "Squatter Zone"
]
def enter_region(player):
    region = player.region
    print(f"\nYou have entered {region}.")

    # Show historical snippet
    if region in history_data:
        print("Local History Flashback:", random.choice(history_data[region]))

    # Encounter NPC with faction reaction
    if region in npc_data:
        npc = random.choice(npc_data[region])
        print(f"\nYou encounter {npc['name']}.")
        print(f"Description: {npc['description']}")
        npc_faction = npc.get("faction")
        reaction = get_npc_reaction(player.faction, npc_faction)
        print(f"{npc['name']}'s reaction to you is: {reaction.upper()}")
        print(respond_to_player(reaction, npc['name']))
    else:
        print("This region seems oddly deserted...")

__all__ = ["enter_region", "available_regions"]
