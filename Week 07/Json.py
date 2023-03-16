

import json

FILE_NAME = "file.json"
sample = dict(name="Fred", age=31, grades=[1,34,55])

def dict(obj):
    with open(FILE_NAME, "wt") as f:
        json.dump(obj,f)

dict(sample)