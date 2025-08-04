import random

def find_abandoned_backpack(player):
    print("While exploring, you find an abandoned backpack.")
    player.inventory.add_item("canned_food")

    if random.random() < 0.4:
        player.status_effects.apply_status("Fatigued")

    if player.faction:
        player.faction_scores.modify_score(player.faction, +5)
        print(f"You feel your ties with {player.faction} strengthen.")

def sudden_raid(player):
    print("A sudden raid erupts nearby! You must decide to hide or fight.")
    choice = input("Do you want to (1) Hide or (2) Fight? ")
    if choice == "1":
        print("You hide successfully, but your reputation with local factions suffers.")
        if player.faction:
            player.faction_scores.modify_score(player.faction, -10)
    elif choice == "2":
        print("You fight bravely and earn respect.")
        if player.faction:
            player.faction_scores.modify_score(player.faction, +15)
    else:
        print("You freeze and get caught in the chaos, becoming Injured.")
        player.status_effects.apply_status("Injured")
