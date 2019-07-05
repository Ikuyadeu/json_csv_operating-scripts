"""
Sampling large size csv/json
sampling.py input_file output_file sample_size
"""
import sys
import random
import csv
import json

argv = sys.argv
args = len(argv)

if args > 3:
    input_file = argv[1]
    output_file = argv[2]
    sample_size = int(argv[3])
else:
    print("Usage: sampling.py input_file output_file sample_size")
    sys.exit()

with open(input_file, "r") as target:
    if input_file.endswith(".csv"):
        reader = csv.DictReader(target)
        fieldnames = reader.fieldnames
        result = random.sample(list(reader), sample_size)

        with open(output_file, "w") as targets:
            writer = csv.DictWriter(targets, fieldnames)
            writer.writeheader()
            writer.writerows(result)
    elif input_file.endswith("json"):
        reader = json.load(target)
        result = random.sample(reader, sample_size)

        with open(output_file, "w") as targets:
            json.dump(result, targets, indent=2)
    else:
        print("You can do sampling for only csv or json file")