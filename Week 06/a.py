

#def average(numbers):
#    avg = sum(numbers) / len(numbers)
 #   return avg
#
#numbers = 10
#print(average)


def menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View new student")
    print("\t(q) Quit")
    choose = input("Type one letter (a/v/q): ")
    return choose

def do_add():
        print("in adding")
        
def do_view():
      print("in viewing")

choose = menu()
while (choose != "q"):
       if choose == "a":
            do_add()
       elif choose == "v":
            do_view()
       else:
            print ("\n\nPlease select either a,v or q")

choose = menu()



    