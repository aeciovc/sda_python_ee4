
class AgeLimitException(Exception):

    LIMIT_AGE = 18

    def __init__(self, age):
        super().__init__(f'age {age} cannot be less than {self.LIMIT_AGE}')


name = input('Type your name')
if name == '':
    raise ValueError('The name cannot be blank')

while True:
    try:
        age = input('Type your age')

        if int(age) < 18:
            raise AgeLimitException(age)
    except AgeLimitException as e:
        print(e)
        continue

    break
