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
