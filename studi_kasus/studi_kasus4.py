def encrypt(text, s):
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""
    for karakter in text:
        if karakter.isupper():
            posisi = huruf_besar.index(karakter)
            hasil += huruf_besar[(posisi + s) % 26]
        elif karakter.islower():
            posisi = huruf_kecil.index(karakter)
            hasil += huruf_kecil[(posisi + s) % 26]
        else:
            hasil += karakter
    return hasil

teks = input("Masukkan teks: ")
pergeseran = 5

print("Plain Text: ", teks)
print("Shift Pattern: ", pergeseran)
print("Encrypted Text: ", encrypt(teks, pergeseran))