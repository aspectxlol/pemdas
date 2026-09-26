huruf_vokal = ["a", "i", "u", "e", "o"]
huruf_konsonan = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

text = input("Masukkan string: ").lower().strip()

jumlah_vokal = 0
jumlah_konsonan = 0

for h in huruf_vokal:
    jumlah = text.count(h)
    if jumlah > 0:
        jumlah_vokal += jumlah

for h in huruf_konsonan:
    jumlah = text.count(h)
    if jumlah > 0:
        jumlah_konsonan += jumlah

print(f"Jumlah huruf vokal: {jumlah_vokal}")
print(f"Jumlah huruf konsonan: {jumlah_konsonan}")