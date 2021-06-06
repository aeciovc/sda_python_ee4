from car import cars

print(cars)
print(sorted(cars, key=lambda car: car.make, reverse=True))
print(max(cars, key=lambda car: car.price))
print(min(cars, key=lambda car: car.price))

exit()

items = [6, 7, 2, 3, 1, 8, 9]

print(sorted(items))
print(max(items))
print(min(items))

