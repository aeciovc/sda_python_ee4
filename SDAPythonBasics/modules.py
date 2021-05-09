# Basic import
import math

print(math.log10(10))

# Specific importing
from math import factorial, sqrt

print(factorial(10))

print(sqrt(10))

import random

random_number = random.randint(1, 10)

print("Random number generated: ", random_number)

from time import time

now = time()

print("The time now is ", now)

import datetime

print("The current date time is ", datetime.datetime.now())
