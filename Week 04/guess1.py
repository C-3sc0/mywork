#program that prompts the user to guess a number, 
#the program should keep prompting the user to guess 
#the number until the user gets the right on 

a = int(input("please guess the Number:"))
num_to_guess = 67

while a != num_to_guess:
    print("wrong")
    a = int(input ("Please guess again:"))

print ("Well Done! Yes the number was", num_to_guess)

