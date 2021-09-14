file = open("hwtask04_file1.txt", "r")
file2 = open("hwtask04_file2.txt", "w")

eng_count = [a for a in file]
eng_count_dict = dict()
for el in eng_count:
    proc = el.split(" — ")
    eng_count_dict[proc[0]] = proc[1].replace("\n","")

for el in eng_count_dict.items():
    if el[0] == "One":
        print(f"Раз — {el[1]}", file = file2)
    if el[0] == "Two":
        print(f"Два — {el[1]}", file = file2)
    if el[0] == "Three":
        print(f"Три — {el[1]}", file = file2)
    if el[0] == "Four":
        print(f"Четыре — {el[1]}", file = file2)

file.close()
file2.close()