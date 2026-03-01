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
def search_memory(keyword):

    memory = load_memory()

    results = []

    for item in memory:

        if keyword.lower() in item["command"].lower():
            results.append(item)

    return results


def show_search(keyword):

    results = search_memory(keyword)

    print("Search Results:")

    for item in results:

        print("Command:", item["command"])
        print("Result:", item["result"])
        print("------------------")
        if __name__ == "__main__":

    store_command("open chrome", "chrome launched")
    store_command("play music", "music started")

    show_memory()

    print("\nSearching chrome:\n")

    show_search("chrome")
