#Add a legend, title and axis labels to this plot.

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size=numberOfEntries)

plt.scatter(ages, salaries, label="salaries")

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints 

plt.plot(xpoints, ypoints, color='r', label = "x squared")
plt.title("lab 8")
plt.xlabel ("Salaries")
plt.ylabel ("age")
plt.legend()
plt.savefig("prettier-plot.png")
