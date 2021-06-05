from datetime import datetime


def run_only_between(from_=7, to_=22):
    # a decorator that only calls a decorated function at certain times
    def dec(func):
        def wrapper():
            if from_ <= datetime.now().hour < to_:
                func()
        return wrapper
    return dec


@run_only_between(8, 10)
def say_something():
    print("Hello world")


say_something()