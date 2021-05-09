# 1 bultin modules
import math
import random

# 2 external library modules

# 3 internal modules
import calculations
from calculations import Calculate

value1 = input("Type the first value:")
value2 = input("Type the second value:")

result = calculations.sum(value1, value2)

print("Result from module calculations is ", result)

import flask

flask.config.ConfigAttribute