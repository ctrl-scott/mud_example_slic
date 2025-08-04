import random
# === chat.py ===
def chat_encounter(player):
    print("\nA stranger messages you on LoveLink...")
    responses = [
        "Your aura reads like a Netflix queue I’d binge.",
        "Are you emotionally available or just bored?",
        "I’m looking for something... radical. Like socialism but sexy.",
        "Tell me one historical event that shaped your love life."
    ]
    print("They say:", random.choice(responses))
    action = input("Respond with /flirt, /truth, /lifesaver or /block: ")

#added optional /lifesaver has to be further integrated
    if action == "/lifesaver":
            print("You activate a lifesaver (You only get 3 in the game, infinite lifesavers for \n for helping others.)")
            player.reputation -= 1
    if action == "/flirt":
        print("They flirt back. You gain +5 reputation.")
        player.reputation += 5
    elif action == "/truth":
        print("They appreciate your honesty. You gain +10 reputation.")
        player.reputation += 10
    elif action == "/block":
        print("You blocked them. No harm done.")
    else:
        print("Unrecognized action. The moment passes.")