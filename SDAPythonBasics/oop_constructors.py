from datetime import datetime

class User:
    def __init__(self, first_name, city, age=18, last_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.__age = age

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def year_of_birth(self):
        return datetime.today().year - self.__age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be greater than 0.")


user1 = User('Aecio', 'Tallinn')
user1.age = -10


print("The age is ", user1.age)
print("The full name is ", user1.name)

print(f"User name is {user1.first_name} and his year of birth was {user1.year_of_birth}")

