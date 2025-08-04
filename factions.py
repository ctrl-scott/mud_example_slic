import json
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Load faction data
with open(os.path.join(DATA_DIR, "factions.json")) as f:
    factions_data = json.load(f)


def get_factions():
    return list(factions_data.keys())

def get_faction_info(name):
    return factions_data.get(name, {})

def describe_faction(name):
    faction = get_faction_info(name)
    if not faction:
        return "Unknown faction."
    return (
        f"Faction: {name}\n"
        f"Alignment: {faction['alignment']}\n"
        f"Description: {faction['description']}\n"
        f"Regions of Influence: {', '.join(faction['bonus_regions'])}\n"
        f"Opposed to: {', '.join(faction['conflict_with'])}"
    )

def get_npc_reaction(player_faction, npc_faction):
    if not npc_faction:
        return "neutral"

    if not player_faction:
        # Independent player benefit: reduced hostility
        if npc_faction in [f for f in factions_data if "conflict_with" in factions_data[f]]:
            return "neutral" if random.random() < 0.5 else "hostile"
        else:
            return "neutral"

    if npc_faction in factions_data.get(player_faction, {}).get("conflict_with", []):
        return "hostile"
    elif player_faction in factions_data.get(npc_faction, {}).get("conflict_with", []):
        return "hostile"
    elif npc_faction == player_faction:
        return "friendly"
    else:
        return "neutral"
