import json

with open("banlist.txt", "r") as ban:
    a = set()
    for i in ban:
        i = i.lower().strip()
        if i:
            a.add(i)
    a = list(a)
    print(len(a))
with open("banlist.json", "w", encoding="utf-8") as jban:
    json.dump(a, jban)
