
class User:
    first_name = ''
    last_name = ''
    age = 0
    city = ''

    def __init__(self):
        self.first_name = 'no name'
        self.last_name = 'no name'
        self.age = -1
        self.city = None
        self.country = 'not defined'

    def get_details(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, City: {self.city}"

user1 = User()
user1.first_name = 'Aecio'
user1.last_name = 'Costa'
user1.age = 33
user1.city = 'Tallinn'

user2 = User()
user2.first_name = 'Jaan'
user2.last_name = 'Priit'
user2.age = 22
user2.city = 'Tartu'

user3 = User()

print("The first user has name ", user1.first_name)
print("Details for user 1 are: ", user1.get_details())
print("User1 is ", user1)
print("The second user has name ", user2.first_name)

print("The details for user3 are: ", user3.get_details())
