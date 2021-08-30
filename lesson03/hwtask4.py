def my_func_1(x,y):
    """Возводит x в степень y"""
    return x ** y

print(my_func_1(3,5))


def my_func_2(x,y):
    """Возводит x в степень y"""
    a = x
    def my_func_2_processor(x,y):
        for i in range(1, y):
            nonlocal a
            a = a * x
    my_func_2_processor(x,y)
    return a

print(my_func_2(3,5))