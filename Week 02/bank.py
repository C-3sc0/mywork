first = input ("Enter Amount1 (in cent):")
second = input ("Enter Amount2 (in cent):")

cen = (int(first) + int(second))/100
euro = u"\u20ac"

print("The sum of these is " f"{euro}" f"{cen}")