
# Given the list of cars, create a new list (filter, lambda) for cars cheaper than 1000.

class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def __repr__(self):
        return f"{self.make} {self.model} {self.price}"

cars = [
    Car("Ford", "Focus", 1200),
    Car("Kia", "Optima", 2300),
    Car("Citroen", "C3", 900),
    Car("BMW", "x3", 800),
    Car("BMW", "x1", 500),
]

cars_cheaper = list(filter(lambda car: car.price <= 1000, cars))  # [Citroen C3 900, BMW x3 800]

print(cars)  # [Ford Focus 1200, Kia Optima 2300, Citroen C3 900, BMW x3 800]
print(cars_cheaper)


