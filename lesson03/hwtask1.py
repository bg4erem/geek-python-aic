def my_divider(a,b):
    """Returns division of a by b."""
    try:
        return a / b
    except ZeroDivisionError:
        print("ERROR: Division by zero")

a = int(input("Enter argument 'a': "))
b = int(input("Enter argument 'b'. 'b' must not be zero: "))
print(my_divider(a, b))