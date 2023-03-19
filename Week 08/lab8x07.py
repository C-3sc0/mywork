#Write a program that makes a list called ages that has, the same number random
#values as salaries, (range:21 to 65) . Make scatter plot of this data.

import numpy as np
import matplotlib.pyplot as plt


min_salary = 20000
max_salary = 80000
num_of_entries = 100

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, num_of_entries)
ages = np.random.randint(low=21, high = 65, size = num_of_entries)



plt.scatter(ages,salaries)

#Add a line to this plot that shows y= x2 in a different colour.
x_point = np.array(range(1,101))
y_point = x_point * x_point
plt.plot(x_point,y_point, color = "r")
plt.show()