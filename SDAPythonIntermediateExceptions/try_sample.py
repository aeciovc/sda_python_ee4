a = 3
b = [1, 0, 2]
for elem in b:
    try:
        result = a / elem
    except ZeroDivisionError:
        continue
        # something you want to do!
    print(f"Result is: {result}")