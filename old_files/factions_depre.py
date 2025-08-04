import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Load faction data
with open(os.path.join(DATA_DIR, "factions_depre.json")) as f:
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
