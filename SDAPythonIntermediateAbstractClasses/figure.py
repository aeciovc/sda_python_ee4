from abc import ABC, abstractmethod
from dataclasses import dataclass

class Figure(ABC):

    @abstractmethod
    def circuit(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Figure):
    def circuit(self):
        pass


@dataclass
class Square(Figure):
    a: int
    b: int

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __repr__(self) -> str:
        return f"Rectangle(a={self.a}, b={self.b})"


class Triangle(Figure):
    def circuit(self):
        pass
