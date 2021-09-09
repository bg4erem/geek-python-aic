# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("hwtask03_file.txt") as file:
    raw_data = [a for a in file]
    salaries = dict()
    for el in raw_data:
        prc_data = el.split(" ")
        salaries[prc_data[0]] = float(prc_data[1].replace("\n",""))

    print("1) Лица с зарплатой менее 20000: ")
    for k, v in salaries.items():
        if v < 20000:
            print(k)

    mean = sum(salaries.values())/len(salaries.values())
    print(f"2) Средняя зарплата: {round(mean, 2)}")