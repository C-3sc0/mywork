#Write a program that plots the function y = x2.

import matplotlib.pyplot as plt
import numpy as np

x_point = np.array(range(1,101))
y_point = x_point * x_point
#y_point = x_point ** 2

plt.plot(x_point, y_point)
plt.show()

