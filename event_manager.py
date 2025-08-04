import random

class EventManager:
    def __init__(self):
        self.events = {}

    def register_event(self, event_name, event_func):
        if event_name in self.events:
            raise ValueError(f"Event '{event_name}' already registered.")
        self.events[event_name] = event_func

    def trigger_event(self, event_name, player):
        if event_name not in self.events:
            print(f"[!] No such event registered: {event_name}")
            return
        print(f"\n[Event Triggered]: {event_name}")
        self.events[event_name](player)

    def trigger_random_event(self, player):
        if not self.events:
            print("[!] No events registered.")
            return
        event_name = random.choice(list(self.events.keys()))
        self.trigger_event(event_name, player)

    def list_events(self):
        print("Registered Events:")
        for name in self.events:
            print(f"- {name}")
