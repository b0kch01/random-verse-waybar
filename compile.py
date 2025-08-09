import json

with open("data/nasb.json", "r") as file:
    bible = json.loads(file.read())

with open("data/verses.txt", "r") as file:
    verses = file.readlines()

books = list(bible.keys())
valid_verses = []

for verse in verses:
    split = verse.split(" ")

    book_idx = int(split[0]) - 1
    book_name = books[book_idx]

    reference = split[1].strip().split(":")

    chapter = reference[0]

    verses = []
    for group in reference[1].split(","):
        if "-" in group:
            start, end = group.split("-")
            verses += [str(i) for i in range(int(start), int(end) + 1)]
        else:
            verses.append(group)

    try:
        text = bible[book_name][chapter][verses[0]]
        valid_verses.append({ "ref": book_name + " " + split[1].strip(), "text": text})
    except KeyError:
        pass

with open("compiled.json", "w") as file:
    file.write(json.dumps(valid_verses, indent=2))
