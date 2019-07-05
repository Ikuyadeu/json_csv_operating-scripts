"""
Combine some json or csv files by regurar expression
Usage: combining_json_csv.py file_expresssion out_file
e.g. combine.py data/csv/*.csv data/csv/combined.csv
"""
import collections
import csv
import sys
import glob
import json


argv = sys.argv
args = len(argv)

if args > 2:
    input_file_path = argv[1]
    out_file_path = argv[2]
else:
    print("Usage: combining.py file_expresssion out_file")
    sys.exit()

input_files = glob.glob(input_file_path)

result = []
fieldnames = []
for input_file in input_files:
    with open(input_file, "r") as target:
        if input_file.endswith(".csv"):
            reader = csv.DictReader(target)
            result.extend(list(reader))
            field_names = reader.fieldnames
        elif input_file.endswith("json"):
            data = json.load(target)
            result.extend(data)
            with open(out_file_path, "w") as outfile:
                json.dump(result, outfile)
        else:
            print("You can count for only csv or json file")
            sys.exit()

if out_file_path.endswith(".csv"):
    with open(out_file_path, "w") as outfile:
        writer = csv.DictWriter(outfile, fieldnames)
        writer.writeheader()
        writer.writerows(result)
elif out_file_path.endswith("json"):
    with open(out_file_path, "w") as outfile:
        json.dump(result, outfile)