text = input("Masukkan string: ").lower().strip()

huruf = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

for h in huruf:
    jumlah = text.count(h)

    if jumlah > 0:
        print(f"{h}: {jumlah}")