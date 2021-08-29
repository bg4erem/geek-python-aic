a = int(input("Input a (distance in the first day): "))
b = int(input("Input b (target distance): "))
k = 1
while a < b:
    a = a * 1.1
    k = k + 1
else:
    print(f"Day when {b} km is reached: {k}")