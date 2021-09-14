# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("hwtask02_file.txt") as file:
    file_lines = file.readlines()

    count_lines = len(file_lines)
    print(f"Lines in file: {count_lines}")

    for line in file_lines:
        k = 1
        print(f"Words in line {k}: {line.count(' ') + 1}")
        k += 1