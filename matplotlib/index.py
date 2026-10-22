import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4, 5])
y1 = 2 + x
y2 = 2 * x
y3 = pow(2, x)
plt.plot(x, y1, "r-", x, y2, "b--", x, y3, "bo")
plt.title("Multiple Lines on Same Plot")
plt.ylabel("Y-axis")
plt.xlabel("X-axis")
plt.show()