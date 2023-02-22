#program that asks the user to enter in a number, and the program will tell the user if the number is even or odd


a = int(input ("Enter a Number:"))
if (a % 2) == 0:
    print(f"{a} is an even number")
else:
    print(f"{a} is an odd number")