#this program reads in a string and strips
#any leading or trailing spaces.
#It also converts all the letters to low case.
#It then outputs the lenghts of the original string
#and the normalised one.

string = input ("Please enter a String: ")

b = string.strip().lower()

length = len(string)
length1 = len(b)

print (f" That string normalised is: {b}")
print(f"we reduced the input string from {length} to {length1} characters")