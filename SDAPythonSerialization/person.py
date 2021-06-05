class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_finance(self):
        pass

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        super().__init__(name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def as_json(self):
        return {
            "name": self.name,
            "age": self.age,
            "rate": self.rate,
            "num_of_hours": self.num_of_hours
        }

    def show_finance(self):
        return self.rate * self.num_of_hours


class Student(Person):

    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

    def to_csv(self):
        return f"{self.name},{self.age},{self.scholarship}"

    def __str__(self):
        return f"{self.name} is {self.age} years old. Scholarship is {self.scholarship} - {self.show_finance()}"

    @classmethod
    def create_from_string(cls, sentence): #cls is the Student class
        name, age, scholarship = sentence.split()
        age, scholarship = int(age), float(scholarship)
        if cls.is_name_correct(name):
            return cls(name, age, scholarship)

    @classmethod
    def create_from_person(cls, person, scholarship):
        return cls(person.name, person.age, scholarship)

    @staticmethod
    def is_name_correct(name):
        if name[0].isupper() and len(name) > 3:
            return True
        return False


class WorkingStudent(Employee,Student):
    def __init__(self, name, age, rate, num_of_hour, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hour)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.rate * self.num_of_hour + self.scholarship
