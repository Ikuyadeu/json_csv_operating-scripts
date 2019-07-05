"""
Sort json or csv file by the item
Usage: sort.py input_file output_file item
"""
import csv
import sys
import json

argv = sys.argv
args = len(argv)

if args > 3:
    input_file = argv[1]
    output_file = argv[2]
    item = argv[3]
else:
    print("Usage: sort.py input_file outputfile item")
    sys.exit()

with open(input_file, "r") as target:
    items = []
    if input_file.endswith(".csv"):
        data = list(csv.DictReader(target))
        data = sorted(data, key=lambda x: x[item], reverse=True)

    elif input_file.endswith("json"):
        data = json.load(target)
        data = sorted(data, key=lambda x: x[item], reverse=True)
    else:
        print("You can sort for only csv or json file")
        sys.exit()
    
    if output_file.endswith(".csv"):
        with open(output_file, "w") as outfile:
            writer = csv.writer(outfile)
            writer.writeheader()
            writer.writerows(data)
    elif output_file.endswith("json"):
        with open(output_file, "w") as outfile:
            json.dump(data, outfile)