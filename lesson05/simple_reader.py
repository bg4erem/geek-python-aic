my_file = open('data.txt', 'w')

# for line in my_file.readlines():
#     print(line.replace('\n', ''))

# for data in my_file.read(1024):
#     print(data)

if my_file.writable():
    my_file.write("Update")
else:
    print("Cannot write")

my_file.close()
