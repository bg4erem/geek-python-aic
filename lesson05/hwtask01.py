# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("hwtask01_created_file.txt", "w") as c_file:
    user_string = input("Input data. Leave blank to stop the program >>> ")
    for item in user_string:
        print(user_string, file=c_file)
        user_string = input("Input data. Leave blank to stop the program >>> ")
        if len(user_string) == 0:
            print("Program is now stopped")
            break