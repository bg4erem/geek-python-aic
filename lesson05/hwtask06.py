with open("hwtask06_file.txt") as file:
    raw_data = file.readlines()

    subjects = dict()
    for str in raw_data:
        subjects[str.split(":")[0]] = 0
        temp_value = ''.join((ch if ch in '0123456789' else ' ') for ch in str) # temp строка только из чисел
        subj_value = [int(s) for s in temp_value.split()] # преобразование строки в список из чисел
        subjects[str.split(":")[0]] = sum(subj_value)

    print(subjects)
