"""
create tex table from csv table 
python3 csv2tex_table.py
"""

import csv
import sys

argv = sys.argv
args = len(argv)

if args > 1:
    input_file = argv[1]
else:
    print("Usage: csv2tex_table.py input_file item_name")
    sys.exit()

contents = []

table_head = """\\begin{table}[t]
\\centering
\\caption{TODO}\\label{tab:TODO}"""

table_tail ="""\\hline
\\end{tabular}
\\end{table}"""

def make_tabular_head(fieldnames):
    base = "\\begin{tabular}{"
    end = "}\\hline"
    columns = base + "|"
    column_names = ""
    for fieldname in fieldnames:
        columns += "l|"
        column_names += remove_escape_char(fieldname) + " & "
    column_names = column_names[:-3] + " \\\\hline"
    columns += end
    return columns + "\n" + column_names

def remove_escape_char(contents):
    tmp = ""
    invalid_chars = ["_", "\\"]
    for char in contents:
        if char in invalid_chars:
            tmp += "\\" + char
        else:
            tmp += char
    return tmp

with open(input_file, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    fieldnames = reader.fieldnames
    fieldnames = [x for x in fieldnames]
    field_len = len(fieldnames)
    contents.append(make_tabular_head(fieldnames))
    for row in reader:
        out = [remove_escape_char(row[x]) + " & " for x in fieldnames]  
        out = "".join(out)[:-2] + "\\\\"
        contents.append(out)

print(table_head)
for out in contents:
    print(out)
print(table_tail)