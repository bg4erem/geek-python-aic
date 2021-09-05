from functools import reduce
def myfunc(x,xx):
    return x * xx

even_numbs = [x for x in range(99,1001) if x % 2 == 0]
print(even_numbs)
print(reduce(myfunc,[x for x in range(99,1001) if x % 2 == 0]))