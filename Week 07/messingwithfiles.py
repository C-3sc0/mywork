#create a program that couts how many ties it was run



FILE_NAME = "count.txt"

def text():
    with open(FILE_NAME, "r") as f:
        read = int(f.read())
    return read

def text_overwrites(number):
    with open(FILE_NAME, "wt") as f:
        f.write(str(number))

num = text()
num += 1
print (f"we have run this program {num} times")
text_overwrites(num)
