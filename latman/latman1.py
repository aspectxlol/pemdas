angka = [
  "",
  "Satu",
  "Dua",
  "Tiga",
  "Empat",
  "Lima",
  "Enam",
  "Tujuh",
  "Delapan",
  "Sembilan",
  "Sepuluh",
  "Sebelas"
]

def Terbilang(bilangan: int) -> str:
    n = int(bilangan)
    if 0 <= n <= 11:
        return angka[n]

    elif n < 20:
        return (Terbilang(n - 10) + " Belas").strip()

    elif n < 100:
        return (Terbilang(n // 10) + " Puluh " + Terbilang(n % 10)).strip()
    else:
      return "Angka terlalu besar"

masuk = int(input("Masukkan angka: "))
tahun = masuk // 365
bulan = (masuk % 365) // 30
minggu = ((masuk % 365) % 30) // 7
hari = ((masuk % 365) % 30) % 7

print(f"{masuk} hari = {Terbilang(tahun)} tahun {Terbilang(bulan)} bulan {Terbilang(minggu)} minggu dan {Terbilang(hari)} hari")
