import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('penjualan.csv')
dataset['tahun'] = dataset["tahun"]
dataset['tot_produk'] = dataset["jumlah_produk"]

dataset.groupby(['tahun', 'nama_provinsi'])['tot_produk'].sum().unstack().plot(cmap='Set1')

plt.title('Trend Penjualan Produk di Lima Provinsi', loc='center', fontsize=20, color='Blue', fontweight='bold')
plt.xlabel("Tahun")
plt.ylabel("Jumlah Produk (UNIT)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.ylim(ymin=0)
plt.legend(loc='lower right', title='Provinsi')
plt.gcf().set_size_inches(10, 6)
plt.tight_layout()
plt.show()