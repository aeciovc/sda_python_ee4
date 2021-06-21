def execute(*args, **kwargs):

    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

    print(kwargs.get("number1"))
    print(kwargs.get("number2"))
    print(kwargs.get("number3"))


execute(1, 2, 3, 4, number1=123)

execute(1, 2, 3, 4, number1=123, number2=5436)


execute(1, 2, 3, 4, number1=123)


execute(1, 2, 3, 4, number1=123)