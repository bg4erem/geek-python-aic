numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_numbers = [i for x, i in enumerate(numbers) if numbers[x] > numbers[x-1]]

print(new_numbers)