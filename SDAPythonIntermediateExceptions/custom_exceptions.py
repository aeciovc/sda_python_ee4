
class FileFormatError(Exception):
    pass

class AgeLimitException(Exception):
    pass

class CustomException(Exception):
    def __init__(self, value):
        message = f"the {value} is invalid"
        super().__init__(message)


a = 3
b = [1, 0, 2]
for elem in b:
    if elem == 0:
        raise CustomException(elem)
    result = a / elem
    print(f"Result is: {result}")

