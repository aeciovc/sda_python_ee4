
def hello_world():
    return "Hello World"

def execute_func(func):
    print("I am going to execute the func")
    func()

hello_world_result = hello_world

print(hello_world_result)
print(hello_world_result())


execute_func(hello_world)