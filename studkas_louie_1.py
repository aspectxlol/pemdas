def hitung_diskon(total_belanja, status_member):
  diskon = 0
  if total_belanja >= 200_000:
    diskon = 20/100
  elif total_belanja >= 100_000:
    diskon = 10/100

  if status_member == "y":
    diskon += 5/100

  return diskon

try:
  nama_pelanggan = str(input("Masukkan nama_pelanggan : "))
  harga_satuan = int(input("Masukkan harga_satuan : "))
  jumlah_buku = int(input("Masukkan jumlah_buku : "))
  status_member  = str(input("Masukka status_member [y / n] : "))
except:
  print("Sistem mengalami kesalahan")
else:
  total_belanja = harga_satuan * jumlah_buku

  diskon = hitung_diskon(total_belanja, status_member)
  
  total_bayar = total_belanja - (total_belanja * diskon)
  print("total diskon", diskon * 100, "%")

  uang = int(input("Masukkan uang : "))
  kembalian = uang - total_bayar
  if kembalian < 0:
    print("Uang anda kurang")