data_string = "Belajar Algoritma dan Pemrograman dengan Python"

print("Data String: ", data_string)

jumlah = data_string.count("a")
print(f"Karakter 'a' muncul sebanyak: {jumlah} kali")

jumlah = data_string.count("A")
print(f"Karakter 'A' muncul sebanyak: {jumlah} kali")

indeks = data_string.find("A")
print(f"Karakter 'A' pertama muncul pada indeks: {indeks}")

indeks = data_string.find(" ")
print(f"{data_string[indeks + 1:]}")