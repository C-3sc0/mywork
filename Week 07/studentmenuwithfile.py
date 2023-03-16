
student = []

def menu():
    print("What would you like to do?")
    print("\t(a) Add a new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choose = input("Type one letter (a/v/q):")
    return choose

#print (f"You choose {choose}")


def do_add(student):
    print("in adding")

def save(student):
    print("in save")

def do_view():
    print("in viewing")

choose = menu()
while choose != "q":
    if choose == "a":
        do_add(student)
    elif choose == "v":
        do_view()
    elif choose != "q":
        print("\n\nPlease select either a,v or q")
    choose = menu()
