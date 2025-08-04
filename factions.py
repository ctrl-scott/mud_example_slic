import json
import os
import random

FACTIONS_FILE = os.path.join("data", "faction_scores.json")
RELATIONSHIPS_FILE = os.path.join("data", "factions.json")

def load_factions():
    with open(FACTIONS_FILE, "r") as f:
        return json.load(f)

def load_relationships():
    with open(RELATIONSHIPS_FILE, "r") as f:
        return json.load(f)

faction_data = load_factions()
faction_relationships = load_relationships()

class FactionSystem:
    def __init__(self):
        self.scores = {faction: data["start_score"] for faction, data in faction_data.items()}

    def modify_score(self, faction, amount):
        if faction not in self.scores:
            print(f"[!] Unknown faction: {faction}")
            return

        self.scores[faction] += amount
        self.scores[faction] = max(-100, min(100, self.scores[faction]))
        print(f"[~] Faction standing with {faction}: {self.scores[faction]}")

    def get_score(self, faction):
        return self.scores.get(faction, 0)

    def list_scores(self):
        print("\n=== Faction Scores ===")
        for faction, score in self.scores.items():
            desc = faction_data[faction]["description"]
            print(f"- {faction} [{score}]: {desc}")

def get_factions():
    return list(faction_data.keys())

def describe_faction(faction_name):
    return faction_data.get(faction_name, {}).get("description", "No description available.")

def get_npc_reaction(player_faction, npc_faction):
    if not npc_faction:
        return "neutral"

    if not player_faction:
        # Independent player benefit: reduced hostility chance
        if npc_faction in faction_relationships:
            return "neutral" if random.random() < 0.5 else "hostile"
        else:
            return "neutral"

    conflict = faction_relationships.get(player_faction, {}).get("conflict_with", [])
    npc_conflict = faction_relationships.get(npc_faction, {}).get("conflict_with", [])

    if npc_faction in conflict or player_faction in npc_conflict:
        return "hostile"
    elif npc_faction == player_faction:
        return "friendly"
    else:
        return "neutral"

def is_independent(player):
    return player.faction is None
def choose_faction(player):
    import json

    with open("data/factions.json") as f:
        factions = json.load(f)

    print("\nChoose a faction to align with:")
    for i, faction in enumerate(factions, 1):
        print(f"{i}. {faction['name']} - {faction['description']}")
    print("0. Stay Independent (no faction)")

    choice = input("Enter the number of your choice: ").strip()
    if choice == "0":
        print("You remain independent, with unique resilience bonuses.")
        player.faction = None
        player.status_effects.add_status("Independent", "You walk your own path. Some NPCs may trust you more—or less.")
    else:
        try:
            idx = int(choice) - 1
            faction = factions[idx]
            player.faction = faction["name"]
            player.inventory.add_item(faction.get("starting_item", "Faction Patch"))
            player.status_effects.add_status(faction["name"], faction.get("status", "You belong to a tribe now."))
            player.faction_scores.set_score(faction["name"], 1)
            print(f"You've joined the {faction['name']}!")
        except (IndexError, ValueError):
            print("Invalid choice. Staying independent.")
            player.faction = None
            player.status_effects.add_status("Independent", "You walk your own path.")

# This line ensures choose_faction is available to import
#__all__ =["choose_faction"]