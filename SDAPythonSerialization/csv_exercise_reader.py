import csv
from person import Student

list_students = []

with open("students.csv") as in_file:
    reader = csv.reader(in_file)
    for row in reader:
        if len(row) >= 3:
            name, age, scholarship = row[0], row[1], row[2]
            student = Student(name, age, scholarship)
            list_students.append(student)

for student in list_students:
    print(student)
