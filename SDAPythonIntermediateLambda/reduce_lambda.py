from functools import reduce

items = [1, 2, 3, 4, 5]

items_sum = reduce(lambda x, y: x + y, items)  # 15

print(items_sum)
