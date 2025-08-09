import random
import json


def load_verses(path):
    with open(path, "r") as file:
        return json.loads(file.read())


def daily_verse(verses, seed=None):
    random.seed(seed)
    verse = random.choice(verses)
    return verse


def waybar_output(verse):
    return json.dumps({
        "text": verse["ref"],
        "class": "verse",
        "tooltip": verse["text"] + "\n\n" + verse["ref"]
    })


if __name__ == "__main__":
    import sys
    seed = sys.argv[-1] if len(sys.argv) > 1 else None

    verses = load_verses("./compiled.json")
    verse = daily_verse(verses, seed)

    print(waybar_output(verse), flush=True)
