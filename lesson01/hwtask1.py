bookname = "Alice in Wonderland"
city = "Moscow"
current_year = 2021
current_temperature = 23.4
friends_list = ["Danil", "Sasha", "Semen"]
pet_data = {"name": "Pluto", "type": "cat", "bornyear": 2019, "foodvendor": "Purina"}

username = input("Your name >> ")
birthyear = int(input("Year when you were born >> "))
userage = current_year - birthyear
print(f"Hello, {username}, you are {userage} years old this year")