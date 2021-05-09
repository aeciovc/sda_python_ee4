
class User:
    def __init__(self, first_name, city, age=18, last_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.__age = age

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


class Programmer(User):

    def __init__(self, first_name, city, age=18, last_name='', languages=[]):
        super().__init__(first_name, city, age=18, last_name='')
        self.languages = languages

    def is_python_programmer(self):
        return 'python' in self.languages

programmer1 = Programmer('Aecio', 'Tallinn', languages=['python', 'golang'])

print("The programmer name is", programmer1.name)
print("A python programmer? ", programmer1.is_python_programmer())