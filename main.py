import sys

with open("standard.txt", "r") as file:
    content = file.read()

    lines = content.split("\n")
    print(lines)
