number = input("Input number: ")
number = int(number)
maxdigit = 0
divided = 0

while number and divided != 9:
    divided = number % 10
    number = number // 10
    maxdigit = divided if divided > maxdigit else maxdigit

print(f"Max digit found: {maxdigit}")
