import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).with_name("penjualan.csv")
dataset = pd.read_csv(data_file)

sales_by_year = dataset.pivot(
    index="tahun",
    columns="nama_provinsi",
    values="jumlah_produk",
)

sales_by_year.plot(
    kind="line",
    marker="o",
    figsize=(10, 6),
)

plt.title("Penjualan per Provinsi dari Tahun ke Tahun")
plt.xlabel("Tahun")
plt.ylabel("Jumlah Produk (UNIT)")
plt.xticks(sales_by_year.index)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(title="Provinsi")
plt.tight_layout()
plt.show()
