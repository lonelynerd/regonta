import os

path = "./memes/"
list_of_files = os.listdir(path)
for name in list_of_files:
    print(name)