income = input("your income >> ")
spendings = input("your spendings >> ")

if income.isdigit() and spendings.isdigit():
    income = int(income)
    spendings = int(spendings)
else:
    print("Please check your inputs. Only numbers are valid")
    exit()

if spendings >= income:
    print("your business is not profitable")
else:
    print("your business is profitable")
    print(f"rate of return is {((income-spendings)/spendings)*100:.2f}%")
    stuff = int(input("How many stuff do you have >> "))
    print(f"Profit per stuff is {(income-spendings)/stuff}")