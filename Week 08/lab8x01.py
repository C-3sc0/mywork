#Write a program that makes a list, called salaries, 
#that has (say 10) random numbers (20000 – 80000).

import numpy as np

min_salary = 20000
max_salary = 80000
num_of_entries = 10

#Modify the program so that the “random” salaries are the same each time the
#program is run, to make the program easier to test, ie “seed” the random number
#generator. 

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, num_of_entries)
#salaries = np.random.randint(20000, 80000, 10)

#Modify the program, to make another array of numbers that has the salaries plus
#5000 (numpy is great for matrix operations)
new_salary = salaries + 500

#Modify the program so that it increases all the salaries by 5% (store in another
#array).
Salary_perc = salaries*(1+0.05)
new_salary_perc = new_salary*(1+0.05)

print(salaries)
print(new_salary)
print (Salary_perc)
print (new_salary_perc)
