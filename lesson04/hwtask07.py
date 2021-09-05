from math import factorial
from itertools import count

def fact():
    for el in count(1):
        yield factorial(el)


generator = fact()
x = 0
for i in generator:
    if x < 10:
        print(i)
        x += 1
    else:
        break