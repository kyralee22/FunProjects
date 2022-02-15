import matplotlib.pyplot as plt
import numpy as np


hot = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
crazy = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

plt.plot(hot,crazy)
plt.title('HOT CRAZY MATRIX')
plt.xlabel('HOT LEVEL')
plt.ylabel('CRAZY LEVEL')
plt.show()
