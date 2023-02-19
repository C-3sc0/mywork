#program that takes in a float and outputs an int
#rounded down.

import math

a = float (input("enter a float number: "))
answer = math.floor(a)

print(f'{a} floored is {answer}')