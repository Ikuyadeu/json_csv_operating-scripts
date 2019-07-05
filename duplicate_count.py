"""
Counting duplicate items from json or csv
Usage: duplicate_count.py input_file item_name
"""
import sys
import csv
import json
import collections

argv = sys.argv
args = len(argv)

if args > 2:
    input_file = argv[1]
    item = argv[2]
else:
    print("Usage: duplicate_count.py input_file item_name")
    sys.exit()

with open(input_file, "r") as target:
    items = []
    if input_file.endswith(".csv"):
        reader = list(csv.DictReader(target))
        for i in reader:
            items.append(i[item])
        c = collections.Counter(items)

        for i in c.most_common():
            print(i)

    elif input_file.endswith("json"):
        data = json.load(target)
        for i in data:
            items.append(i[item])
        c = collections.Counter(items)

        for i in c.most_common():
            print(i)
    else:
        print("You can count for only csv or json file")
        sys.exit()