
def simple_function():
    print("Simple function executed")
    return "This is not a generator"

def simple_generator():
    print("Simple generator execution")
    print("More one")
    yield "This is a generator"

    a = 9
    print("The second yield")
    yield "Second part!"

    b = True
    print("The third yield")
    yield "Third part!"

result_function = simple_function()

result_generator = simple_generator()

print(result_function)
print(result_generator)

for item in result_generator:
    print(item)

#result_generator.__next__()