








filename = "data.txt"

try:
    with open(filename) as f:
        print(f.read())
except FileNotFoundError:
    print("file (", filename, ") does not exist")
