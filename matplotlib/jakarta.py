import matplotlib.pyplot as plt
import numpy as np

lokasi = ['Jakarta Pusat', 'Jakarta Utara', 'Jakarta Timur', 'Jakarta Selatan', 'Jakarta Barat']
jumlah_mall = [21, 16, 16, 27, 15]

fig, axs = plt.subplots(1, 3, figsize=(12, 6), sharey=True)
fig.suptitle('Sebaran Mall di Jakarta', fontsize=16)
axs[0].bar(lokasi, jumlah_mall, color='skyblue')
axs[0].set_title('Bar Chart')
axs[1].plot(lokasi, jumlah_mall, marker='o', linestyle='-', color='orange')
axs[1].set_title('Line Chart')
axs[2].scatter(lokasi, jumlah_mall, color='green')
axs[2].set_title('Scatter Plot')
plt.show()
