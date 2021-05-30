import csv
from person import Student

name = input("Your name:")
age = int(input("Your age:"))
scholarship = float(input("Your scholarship:"))

student = Student(name, age, scholarship)

with open("students.csv", 'a') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(student.to_csv().split(','))

print("Success!")

