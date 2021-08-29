# password = input("Введите пароль >>>")
#
# original_password = "correct"
#
# if original_password == password:
#     print("Password is correct")
# else:
#     print("Password is incorrect")

age = int(input("Input your age >>> "))

if age >= 14:
    print("You are eligible to apply for the passport")
    if age >= 20 and age < 45:
        print("You can renew your passport")
else:
    print("Sorry, you are not eligible to apply for the passport")