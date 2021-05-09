
def is_in_range(grade):
    return grade >= 0 and grade <= 10


class Student:

    __MINIMAL_GRADE = 7

    def __init__(self, name, age, grade=None):
        self.name = name
        self.age = age
        self.grade = grade if is_in_range(grade) else None

    def is_approved(self):
        return self.grade >= self.__MINIMAL_GRADE
