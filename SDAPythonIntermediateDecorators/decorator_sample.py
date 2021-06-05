from datetime import datetime


def disable_at_night(func):
    # a decorator that only calls a decorated function during the day
    def wrapper():
        print("Starting the decorator")
        if 7 <= datetime.now().hour < 22:
            func()
        print("Finishing the decorator")
    return wrapper


@disable_at_night
def say_something():
    print("Hello world")



say_something()