items = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, items))

print(even_numbers)

# The same of filter
result = []
for x in items:
    if x % 2 == 0:
        result.append(x)

print(result)
