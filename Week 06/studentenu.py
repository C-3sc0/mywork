

def menu():
    print("Waht would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ")
    return choice

choice = menu()
#print (f"You choose {choice}")

def read_modules():
    modules = []
    module_name = input ("\tEnter the first Modue name (Blank to quit):").strip()

    while module_name != "":
        module = {}
        module ["name"] = module_name
        module ["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        module_name = input ("\tEnter nxt module name (Blank to quit): ").strip()
        return modules

def do_add(students):
    current_student = {}
    current_student ["Name"]=input("Enter name: ")
    current_student ["modules"]= read_modules()

    students.append(current_student)
    
students = []
choice = menu()
        
def do_view(students):
    print(students)
    
while (choice != "q"):
    if choice == "a":
        do_add(students)
    elif choice =="v":
        do_view(students)
    elif choice != "q":
        print("\n\nPlease select either a,v or q")
    choice = menu()
