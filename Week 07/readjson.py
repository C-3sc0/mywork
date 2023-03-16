
import json

FILE_NAME = "file.json"

def read_dict():
    with open (FILE_NAME, "r") as f:
        return json.load(f)

some_duct = read_dict()
print(some_duct)