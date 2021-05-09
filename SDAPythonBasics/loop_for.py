animals = ["Dog", "Cat", "Fish"]

print("-------- Manually way")
print(animals[0])
print(animals[1])
print(animals[2])

print("-------- For loop")
# List all animals from the animals list
for animal in animals:
    print(animal)

print("-------- While loop")
i = 0
while i < len(animals):
    print(animals[i])
    i += 1