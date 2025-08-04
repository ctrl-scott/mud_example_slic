from inventory import Inventory
from factions import FactionSystem
from status import StatusManager
class Player:

    #

    def __init__(self, name):
        self.name = name
        self.region = None
        self.inventory = []
        self.faction = None
        self.faction_scores = FactionSystem()  # New
        self.inventory = Inventory()  # New
        self.faction_scores = {}
        self.health = 100
        self.status_effects = StatusManager()
        self.status_effects = []


    def join_faction(self, faction_name):
        self.faction = faction_name
        self.faction_scores[faction_name] = self.faction_scores.get(faction_name, 0) + 1

    def is_independent(player):
        return player.faction is None

    def update_faction_score(self, faction_name, points):
        self.faction_scores[faction_name] = self.faction_scores.get(faction_name, 0) + points

    def describe(self):
        print(f"\n=== Player Summary ===")
        print(f"Name: {self.name}")
        print(f"Region: {self.region}")
        print(f"Faction: {self.faction}")
        print(f"Faction Scores: {self.faction_scores}")
        print(f"Inventory: {self.inventory}")
        print(f"Health: {self.health}")
        print(f"Status Effects: {self.status_effects}")
