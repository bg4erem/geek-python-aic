import os

if os.path.exists('data.txt'):
    os.remove('data.txt')

files = os.listdir()
print(files)