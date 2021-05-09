
class User:

    first_name = 'class attribute'

    def __init__(self):
        self.first_name = 'instance attribute'
        self.last_name = ''
        self.age = -1
        self.city = None
        self.country = ''


user1 = User()
print(user1.first_name)

print(User.first_name)