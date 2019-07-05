"""
Counting json items or csv rows
counting_json_csv.py input_file
"""
import sys
import csv
import json

argv = sys.argv
args = len(argv)

if args > 1:
    input_file = argv[1]
else:
    print("Usage: counting_json_csv.py input_file")
    sys.exit()

with open(input_file, "r") as target:
    if input_file.endswith(".csv"):
        data = csv.DictReader(target)
        print(len(list(data)))
    elif input_file.endswith("json"):
        data = json.load(target)
        print(len(data))
    else:
        print("You can count for only csv or json file")