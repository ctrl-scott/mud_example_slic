# === regions.py ===
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