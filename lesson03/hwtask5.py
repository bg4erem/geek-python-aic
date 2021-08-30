inputlist = input("введите числа через пробел: ")
workedlist = map(int, inputlist.split())
print(sum(workedlist))