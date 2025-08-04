# player.py

from effects.status import StatusEffects
from inventory import Inventory

class Player:
    def __init__(self, name):
        self.name = name
        self.region = None
        self.faction = None
        self.faction_score = {}
        self.inventory = Inventory()
        self.status_effects = StatusEffects()

    def update_faction_score(self, faction_name, amount):
        if faction_name not in self.faction_score:
            self.faction_score[faction_name] = 0
        self.faction_score[faction_name] += amount

    def show_status(self):
        print(f"\n{self.name}'s Status")
        print(f"Region: {self.region}")
        print(f"Faction: {self.faction if self.faction else 'Independent'}")
        print("Inventory:", ', '.join(self.inventory.items) if self.inventory.items else "Empty")
        print("Status Effects:")
        for status, description in self.status_effects.list_statuses().items():
            print(f"  - {status}: {description}")
        print("Faction Scores:")
        for faction, score in self.faction_score.items():
            print(f"  - {faction}: {score}")
