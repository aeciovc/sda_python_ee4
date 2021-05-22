
def make_calculations():
    raise IOError

try:
    make_calculations()
except ValueError:
    # handling an exception of ValueError type
    pass
except (ZeroDivisionError, KeyError):
    # handling exceptions ZeroDivisionError and KeyError type
    print("")
except:
    # handling all other exceptions
    pass
