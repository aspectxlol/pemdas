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

def Terbilang(bilangan):
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

    elif n < 1_000_000_000:
        return (Terbilang(n // 1_000_000) + " Juta " + Terbilang(n % 1_000_000)).strip()

    elif n < 1_000_000_000_000:
        return (Terbilang(n // 1_000_000_000) + " Milyar " + Terbilang(n % 1_000_000_000)).strip()

    elif n < 1_000_000_000_000_000:
        return (Terbilang(n // 1_000_000_000_000) + " Triliun " + Terbilang(n % 1_000_000_000_000)).strip()

    elif n < 1_000_000_000_000_000_000:
        return (Terbilang(n // 1_000_000_000_000_000) + " Kuadriliun " + Terbilang(n % 1_000_000_000_000_000)).strip()

    elif n < 1_000_000_000_000_000_000_000:
        return (Terbilang(n // 1_000_000_000_000_000_000) + " Kuintiliun " + Terbilang(n % 1_000_000_000_000_000_000)).strip()

    else:
        return "Angka terlalu besar"

x = int(input("Masukkan angka: "))
huruf = Terbilang(x)
print(f"Terbilang: {huruf}")
