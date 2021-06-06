
class EvenAndOddNumbers:

    def __init__(self, low, high, mode):
        self.current = low
        self.high = high
        self.mode = mode

    def __iter__(self):
        return self

    def is_even(self, n):
        return n % 2 == 0

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            current = self.current
            self.current += 1

            if self.is_even(current):
                return current
            else:
                return self.__next__()


list_evens = EvenAndOddNumbers(1, 10, 'evens')
for item in list_evens:
    print(item)
