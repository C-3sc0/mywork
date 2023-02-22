







count = 0
while (count < 10):
    print ("count is ", count) #-----> the , will print the first part as a string an the sec as int
    count +=1 #---> += is = to count = count + 1

print ("at the end count is", count)

count = 10
while (count >= 0):
    print("countdown ", count)
    count -= 1
print ("Blast off")


#sentinal controlled loop

val = input ("type something (q to quit):")
while val != "q":
    print ("hi mom")
    val = input ("q to quit:")

print ("all done")

