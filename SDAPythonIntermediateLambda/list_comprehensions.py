
# List in loop for
numbers = []
for i in range(1000):
    numbers.append(i)

print(numbers)

# List Comprehension
numbers = [i for i in range(1000)]
print(numbers)


# Task: Create a new list with the odds numbers and print out
items = [1, 2, 3, 4, 5]

result = []
for i in items:
    if i % 2 != 0:
        result.append(i)

print(result)

result = [i for i in items if i % 2 != 0]
print(result)

# Task: Create a new list with the squared numbers and print out
items = [1, 2, 3, 4, 5]

squared = [x**2 for x in items]   # [ squared.append(i**2) for i in items  ]

print(squared)
# [1, 4, 9, 16, 25]