import json

with open("students.json") as in_file:
    data = json.load(in_file)

print(data)

print(len(data))
print(f"{data[0]['name']} has {data[0]['number of points']} number of points")
