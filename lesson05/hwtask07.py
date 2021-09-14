import json

with open("hwtask07_file.txt") as file, open("hwtask07_json.json", "w") as jsonfile:
    data = file.readlines()
    sumprofit_k = 0
    k = 0
    sumprofit = 0
    dict1 = dict()
    dict2 = dict()
    for str in data:
        str = str.replace("\n", "")
        list = str.split(" ")
        if int(list[2]) > int(list[3]):
            print(f"Компания {list[0]} получила прибыль {int(list[2]) - int(list[3])} MONEY")
            sumprofit_k = sumprofit_k + (int(list[2]) - int(list[3]))
            k += 1
        dict1[list[0]] = int(list[2]) - int(list[3])
        sumprofit = sumprofit + (int(list[2]) - int(list[3]))
        dict2["average profit"] = (round(sumprofit / len(data)))
    print(f"Средняя прибыль безубыточных компаний: {round(sumprofit_k / k)} MONEY")
    final_list = [dict1, dict2]
    json.dump(final_list, jsonfile)
