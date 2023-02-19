#program that takes in a float amount of dollars
#and returns that absolute amount in cent.


a = float (input ("Please enter an amount: "))
b = a *100
answer = int(abs(b))
print (f'That amount in cent is: {answer}')