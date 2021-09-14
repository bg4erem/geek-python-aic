def my_func(a, b, c):
    """Возвращает сумму 2 наибольших аргументов"""
    list = (a, b, c)
    list = sorted(list, reverse=True)
    print(f"Сумма 2 наибольших аргументов: {list[0] + list[1]}")

my_func(4,0,2)