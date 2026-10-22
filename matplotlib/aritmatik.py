import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 20, 0.2)
y = np.sin(x)

plt.plot(x, y)
plt.title('Grafik Fungsi Sinus')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()