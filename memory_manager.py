# Nexa OS Memory Manager
# Stores user commands and results

import json
import os

MEMORY_FILE = "nexa_memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    
    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def store_command(command, result):
    memory = load_memory()
    
    entry = {
        "command": command,
        "result": result
    }
    
    memory.append(entry)
    
    save_memory(memory)


def show_memory():
    memory = load_memory()
    
    for item in memory:
        print("Command:", item["command"])
        print("Result:", item["result"])
        print("------------------")


# Test Example

if __name__ == "__main__":
    
    store_command("open chrome", "chrome launched")
    store_command("play music", "music started")
    
    show_memory()
