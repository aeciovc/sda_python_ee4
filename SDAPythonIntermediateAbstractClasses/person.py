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

    def show_finance(self):
        return self.rate * self.num_of_hours


class Student(Person):

    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

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


p2 = Person("Jane", 32)
s2 = Student(p2.name, p2.age, 300)

p1 = Person("Henry", 54)
print(p1)

s1 = Student("Jack", 34, 1000)
print(s1)

e1 = Employee("Jhonson", 22, 14.5, 20)
print(e1)


from polymorphism import check_finance

check_finance(s1)  # an instance of the Employee class
check_finance(e1)  # an instance of the Student class


#ws1 = WorkingStudent("Peter", 23, 10.7, 25, 500)
#print(ws1)

s2 = Student.create_from_string("Alice 21 600")
print(s2)

print(Student.is_name_correct("alice"))

s3 = Student.create_from_person(p1, 300)
print(s3)
print(s3.show_finance())


my_student = "Aecio 33 500"

s1 = Student("Fernando", 34, 500)

stundet_aecio = s1.create_from_string(my_student)

