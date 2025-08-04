# main.py

import random
from player import Player
from factions import choose_faction
from regions import available_regions, enter_region
from event_manager import EventManager
import events

def main():
    print("\n=== Welcome to Heartland Crawl ===")
    name = input("Enter your character's name: ").strip()
    player = Player(name)

    # Faction selection or independent path
    choose_faction(player)

    # Assign region randomly
    player.region = random.choice(available_regions)
    print(f"\nYou are now entering the {player.region}...\n")

    # Region logic: load history, NPCs, interactions
    enter_region(player)

    # Trigger a random event from event manager
    event_manager = EventManager()
    event_manager.register_event("Find Abandoned Backpack", events.find_abandoned_backpack)
    event_manager.register_event("Sudden Raid", events.sudden_raid)
    event_manager.trigger_random_event(player)

    # Display current game status
    print("\n--- STATUS REPORT ---")
    print(f"Player: {player.name}")
    print(f"Faction: {player.faction if player.faction else 'Independent'}")
    print(f"Region: {player.region}")
    print("\nInventory:")
    player.inventory.list_items()
    print("\nStatus Effects:")
    player.status_effects.list_statuses()
    print("\nFaction Scores:")
    player.faction_scores.list_scores()

    print("\n=== End of Cycle ===")

if __name__ == "__main__":
    main()
