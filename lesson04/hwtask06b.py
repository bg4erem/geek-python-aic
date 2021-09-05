# б) итератор, повторяющий элементы некоторого списка, определенного заранее

from itertools import cycle

i = 0
spisok = "ABCDEF"
for el in cycle(spisok):
    if i > 50:
        break
    i += 1
    print(el)