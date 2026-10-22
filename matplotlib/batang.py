import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge
from matplotlib.text import Text
from typing import cast

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

sebaran_data = {"21 buah Jakpus",
                "16 buah jaktim",
                "16 buah Jakut",
                "27 buah Jaksel",
                "15 buah Jakbar",}

data = [float(x.split()[0]) for x in sebaran_data]
keterangan = [x.split()[-1] for x in sebaran_data]

def func(pct, allvals):
    absolute = int(pct / 100. * np.sum(allvals))
    return "{:.1f}%\n({:d} buah)".format(pct, absolute)

wedges, texts, autotexts = cast(
    tuple[list[Wedge], list[Text], list[Text]],
    ax.pie(data, autopct=lambda pct: func(pct, data),
           textprops=dict(color="w")),
)

ax.legend(wedges, keterangan,
          title="Keterangan",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Sebaran Data Buah di Jakarta")
plt.show()