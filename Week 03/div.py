#write a program that reads in two numbers and divides the first one 
#by the second and give the integer result and the remainder

a = int(input("Enter the first Number: "))
b = int(input("Enter the number you want to divide by: "))
answer = int(a // b)
remainder = a % b

print(f' {a} divided by {b} is {answer} with remainder {remainder}')