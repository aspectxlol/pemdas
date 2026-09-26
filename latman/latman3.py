masuk = int(input("Masukkan angka: "))

pecahan_uang = [
  "seribu",
  "dua ribu",
  "lima ribu",
  "sepuluh ribu",
  "dua puluh ribu",
  "lima puluh ribu",
  "seratus ribu",
]

jumlah_pecahan_seratus = masuk // 100_000
jumlah_pecahan_lima_puluh_ribu = (masuk % 100_000) // 50_000
jumlah_pecahan_dua_puluh_ribu = (masuk % 50_000) // 20_000
jumlah_pecahan_sepuluh_ribu = (masuk % 20_000)// 10_000
jumlah_pecahan_lima_ribu = (masuk % 10_000) // 5_000
jumlah_pecahan_dua_ribu = (masuk % 5_000) // 2_000
jumlah_pecahan_seribu = (masuk % 2_000) // 1_000
jumlah_sisa = masuk % 1_000

print("Pecahan uang:")
print(f"{jumlah_pecahan_seratus} = uang {pecahan_uang[6]}")
print(f"{jumlah_pecahan_lima_puluh_ribu} = uang {pecahan_uang[5]}")
print(f"{jumlah_pecahan_dua_puluh_ribu} = uang {pecahan_uang[4]}")
print(f"{jumlah_pecahan_sepuluh_ribu} = uang {pecahan_uang[3]}")
print(f"{jumlah_pecahan_lima_ribu} = uang {pecahan_uang[2]}")
print(f"{jumlah_pecahan_dua_ribu} = uang {pecahan_uang[1]}")
print(f"{jumlah_pecahan_seribu} = uang {pecahan_uang[0]}")
print(f"tersisa: {jumlah_sisa} rupiah")