import file_storage
import time

def store(user_input, output):
    memory = file_storage.load_memory()

    memory.append({
        "input": user_input,
        "output": output,
        "time": time.time()
    })

    file_storage.save_memory(memory)


def search_memory(keyword):
    memory = file_storage.load_memory()
    results = []

    for item in memory:
        score = 0

        if keyword.lower() in item["input"].lower():
            score += 2

        if keyword.lower() in item["output"].lower():
            score += 1

        if score > 0:
            item["score"] = score
            results.append(item)

    results.sort(key=lambda x: x["score"], reverse=True)

    return results


def retrieve(user_input):
    memory = file_storage.load_memory()
    results = search_memory(user_input)

    if results:
        return results[:5]   # best 5 (not last)

    return memory[-5:]
