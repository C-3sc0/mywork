# get the program to generate a random number between 0 and 100 to
#guess


import random
num_to_guess = random.randint(1,100) 
a = int(input("Please guess the Number:"))


while a != num_to_guess:
    if a < num_to_guess:
        print("too low")
    else:
        print ("too high")
    a = int(input("please guess again:"))
print ("Well Done!, Yes the number was", num_to_guess)
