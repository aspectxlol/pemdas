import matplotlib.pyplot as plt
import numpy as np

np.random.seed(50)
random_x = np.random.randint(1, 50, 50)
random_y = np.random.randint(1, 50, 50)
plt.scatter(random_x, random_y, s=100, c=random_x, cmap='viridis', alpha=0.6, edgecolors='w')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()