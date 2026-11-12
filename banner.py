import os

def load_banner(name):

    folder_name = "banners"

    file_path = os.path.join(folder_name, name + ".txt")
    
    with open(name + "standard.txt") as file:
        lines = file.read().split("\n")

    characters = {}
    for number in range(32, 127):
        start = (number - 32) * 9 + 1
        characters[chr(number)] = lines[start:start + 8]
    

    return characters