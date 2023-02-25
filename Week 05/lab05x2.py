#pr that puts 10 random numbers into a queue(list)
#the pr should then output all the values in the queue,
#then take the number from the queue on at time,
#print it and the current numbers stil; in the queue.

import random

a = []
for number in range(10):
    a.append(random.randint(1,100))
print(f"queue is {a}")

while len(a) !=0:
    current_number = a.pop(0)
    print(f"Current number is {current_number} and the queue is {a}")

print ("the queue is now empty")
