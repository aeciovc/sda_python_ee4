class List:

    def __init__(self, low, high):
        self.high = high
        self.current = low

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current = self.current + 1
            return self.current - 1


list = List(20, 40)
for item in list:
    print(item)
