




import numpy as np
import matplotlib.pyplot as plt

#np.random.seed(1) #the hist will be always the same without it the graph will always change
norm_data = np.random.normal(size=10000)

plt.hist(norm_data)
plt.show()