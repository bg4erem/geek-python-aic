# а) итератор, генерирующий целые числа, начиная с указанного

from itertools import count

a = int(input("Please input a start number: "))

for el in count(a):
    if el > a*10:
        break
    else:
        print(el)