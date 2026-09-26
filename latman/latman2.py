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
    
    elif n < 200:
        return ("Seratus " + Terbilang(n - 100)).strip()

    elif n < 1000:
        return (Terbilang(n // 100) + " Ratus " + Terbilang(n % 100)).strip()

    elif n < 2000:
        return ("Seribu " + Terbilang(n - 1000)).strip()

    elif n < 1_000_000:
        return (Terbilang(n // 1000) + " Ribu " + Terbilang(n % 1000)).strip()
    
    else:
      return "Angka terlalu besar"

masuk = int(input("Masukkan angka: "))
jam = masuk // 3600
menit = (masuk % 3600) // 60
detik = (masuk % 3600) % 60

print(f"{masuk} detik = {Terbilang(jam)} jam {Terbilang(menit)} menit dan {Terbilang(detik)} detik")