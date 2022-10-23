import math
import csv
from csv import writer
from turtle import clear # moose

file_path = "/home/christopher/PycharmProjects/Oura_Analysis/oura_analysis.csv"

# Example: Recovery Index Score,Recovery Index Score,1.0000000000000002
rows = []
with open(file_path, 'r') as f_file:
    csvreader = csv.reader(f_file)
    for row in csvreader:
        rows.append(row)

#print(rows)

r_val = []
i = 1
for item in rows:
    r_val.append((abs(float(item[2])), i))
    i += 1
sort_val = sorted(r_val)

amount_values = input("How many values: ")

if amount_values != 0:
    z = sort_val[(len(sort_val) - int(amount_values)):]
    out = [tup[1] for tup in z]
    for items in out:
        out = (rows[items - 1])
        if "REM" or "Deep" or "Light" in out:
            print(out)
else:
    print(sort_val)

