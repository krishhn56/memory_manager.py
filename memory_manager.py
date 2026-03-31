memory_store = []

def store(user_input, output):
    memory_store.append({
        "input": user_input,
        "output": output
    })

def retrieve(user_input):
    return memory_store[-3:]  # last 3 memory
