import json
import os

STATUS_FILE = os.path.join("data", "status_effects.json")

def load_status_definitions():
    with open(STATUS_FILE, "r") as f:
        return json.load(f)

status_definitions = load_status_definitions()

class StatusManager:
    def __init__(self):
        self.active_status = []

    def apply_status(self, status_name):
        if status_name not in status_definitions:
            print(f"[!] Unknown status effect: {status_name}")
            return

        if status_name in self.active_status:
            print(f"[~] Status '{status_name}' already active.")
            return

        self.active_status.append(status_name)
        print(f"[+] You are now affected by: {status_name} — {status_definitions[status_name]['description']}")

    def remove_status(self, status_name):
        if status_name in self.active_status:
            self.active_status.remove(status_name)
            print(f"[-] Status removed: {status_name}")
        else:
            print(f"[!] Status '{status_name}' not found.")

    def list_status(self):
        if not self.active_status:
            print("[~] You are not currently affected by any status effects.")
            return

        print("\n=== Active Status Effects ===")
        for status in self.active_status:
            info = status_definitions[status]
            print(f"- {status}: {info['description']} (Impact: {', '.join(info['impact'])})")
