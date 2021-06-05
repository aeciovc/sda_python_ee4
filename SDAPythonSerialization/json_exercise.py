import json
from person import Employee


def initialize():
    with open("employee.json", 'w+') as file:
        content = file.readline()
        if content == '':
            file.write('[]')
            file.close()

initialize()

name = input("Your name:")
age = int(input("Your age:"))
rate = float(input("Your rate:"))
num_of_hours = int(input("Your num of hours:"))

employee = Employee(name, age, rate, num_of_hours)

list_of_employee = []
with open("employee.json") as in_file:
    list_of_employee = json.load(in_file)

list_of_employee.append(employee.as_json())

with open("employee.json", 'w') as out_file:
    json.dump(list_of_employee, out_file)



