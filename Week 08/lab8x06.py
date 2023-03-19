#Write a program that plots a histogram of the salaries (from Question 1)

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
num_of_entries = 10

np.random.seed(1)
x_point = np.random.randint(min_salary, max_salary, num_of_entries)


plt.hist(x_point)
plt.show()