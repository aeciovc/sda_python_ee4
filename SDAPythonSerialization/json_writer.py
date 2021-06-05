import json

students = [
    {
        'name': "Adam",
        'surname': "Smith",
        'number of points': 20
    },
    {
        'name': "John",
        'surname': "Shadow",
        'number of points': 17
    }
]

with open("students.json", 'w') as out_file:
    json.dump(students, out_file)
