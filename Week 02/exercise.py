#prompt the user and read in two money amonts (in cent)
#add the to amounts
#print out the answer in a human readable format
#with a euro sign and decimal point between the euro
#and cent of the amount

# print ((65+180)/100)

amount = 65
amount1 = 180

#print (u"\N{euro sign}")

#print (u"\u20ac")

cen = float ((amount + amount1)/100)
euro = u"\u20ac"

print("The sum of these is " f"{euro}" f"{cen}")

