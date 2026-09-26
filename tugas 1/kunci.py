for kunci in range(1, 6):
  p1 = kunci == 1
  p2 = kunci == 5
  p3 = kunci % 2 == 1
  p4 = kunci == 1
  p5 = kunci == 4

  pernyataan = [p1, p2, p3, p4, p5]
  jumlah_benar = sum(pernyataan)

  if jumlah_benar == 1 and pernyataan[kunci - 1]:
    print(f"Kunci yang benar adalah: {kunci}")