# chat/reaction.py

def respond_to_player(reaction, npc_name):
    """Generate a dynamic response based on reaction type."""
    if reaction == "hostile":
        return f"{npc_name} glares at you. 'I don’t deal with your kind around here.'"
    elif reaction == "friendly":
        return f"{npc_name} smiles warmly. 'Good to see someone from our crew out here.'"
    elif reaction == "neutral":
        return f"{npc_name} nods politely but keeps their distance."
    else:
        return f"{npc_name} looks confused and doesn’t know how to react."
