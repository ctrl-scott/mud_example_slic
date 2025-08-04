import json
import os

INVENTORY_DATA_FILE = os.path.join("data", "inventory_items.json")

def load_inventory_definitions():
    with open(INVENTORY_DATA_FILE, "r") as f:
        return json.load(f)

inventory_definitions = load_inventory_definitions()

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item_key):
        if item_key not in inventory_definitions:
            print(f"[!] Item '{item_key}' not recognized.")
            return

        item = inventory_definitions[item_key]
        self.items.append({
            "key": item_key,
            "type": item["type"],
            "effects": item["effects"],
            "description": item["description"]
        })
        print(f"[+] You picked up: {item_key} — {item['description']}")

    def remove_item(self, item_key):
        for item in self.items:
            if item["key"] == item_key:
                self.items.remove(item)
                print(f"[-] Removed item: {item_key}")
                return
        print(f"[!] You don’t have {item_key} in your inventory.")

    def list_items(self):
        if not self.items:
            print("[~] Inventory is empty.")
            return

        print("\n=== Your Inventory ===")
        for item in self.items:
            print(f"- {item['key']}: {item['description']}")

    def has_item(self, item_key):
        return any(item["key"] == item_key for item in self.items)

    def get_effects(self):
        all_effects = []
        for item in self.items:
            all_effects.extend(item["effects"])
        return all_effects
