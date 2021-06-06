
def even_numbers_generator(low, high):
    number = low
    while number <= high:
        if number % 2 == 0:
            yield number
        number += 1


def odd_numbers_generator(low, high):
    number = low
    while number <= high:
        if number % 2 != 0:
            yield number
        number += 1


print("Even Numbers:")
gen = even_numbers_generator(1, 10)
for item in gen:
    print(item)

print("Odd Numbers:")
gen_odd = odd_numbers_generator(2, 20)
for item in gen_odd:
    print(item)