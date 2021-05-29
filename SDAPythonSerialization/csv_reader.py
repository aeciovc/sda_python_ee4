import csv

with open("students.csv") as in_file:
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
