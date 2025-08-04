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
