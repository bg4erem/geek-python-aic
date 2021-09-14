# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

file = open("hwtask05_file.txt", "w")
for k in range(2 + round(random.random() * 10)):
    a = round(random.random() * 10)
    file.write(f"{a} ")
file.close()

file = open("hwtask05_file.txt", "r")
data = file.read()
data = [s for s in data.split(" ")]
data.remove("")
data = [int(s) for s in data]
print(f"Сумма чисел в файле: {sum(data)}")
file.close()