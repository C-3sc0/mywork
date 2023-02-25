#program that keeps reading number until the user
#enters a 0. the program should then prnt out
#each of the numbers entered and the average of them

number = int(input("Enter a number (0 to quit): "))
numbers = []

while number != 0:
    numbers.append(number)
    number = int(input("Enter another (0 to quit): "))

for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers)
print (f'the average is {average}')

    