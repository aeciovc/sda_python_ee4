
class InvalidPersonName(Exception):
    pass


import random
try:
    random.randint()
except ValueError as e:
    pass
except KeyError as ex:
    ex.message
except (ImportError, NotImplemented):
    pass
finally:
    pass