a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# print(a.count(23))
ans = [x for x in a if a.count(x) < 2]
print(ans)