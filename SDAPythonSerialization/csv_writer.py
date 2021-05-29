import csv

with open("students.csv", 'a') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Anna Dylan", 29, 250])
