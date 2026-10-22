from statistics import mean


data = [95, 102, 98, 110, 118, 125, 131, 128, 122, 115, 108, 133, 140, 138, 127, 121, 144, 136, 129,
142, 147, 152, 139, 134, 126, 155, 141, 148, 120, 146, 158, 132, 143, 137, 150, 162, 130,
145, 168, 124]

print("Rata-rata data:", mean(data))
print("max data:", max(data))


#90 - 104
kelas1 = [x for x in data if 90 <= x <= 104]
kelas2 = [x for x in data if 105 <= x <= 119]
kelas3 = [x for x in data if 120 <= x <= 134]
kelas4 = [x for x in data if 135 <= x <= 149]
kelas5 = [x for x in data if 150 <= x <= 164]
kelas6 = [x for x in data if 165 <= x <= 179]

print("Kelas 1 (90 - 104):", len(kelas1) / len(data) * 100, "%")
print("Kelas 2 (105 - 119):", len(kelas2) / len(data) * 100, "%")
print("Kelas 3 (120 - 134):", len(kelas3) / len(data) * 100, "%")
print("Kelas 4 (135 - 149):", len(kelas4) / len(data) * 100, "%")
print("Kelas 5 (150 - 164):", len(kelas5) / len(data) * 100, "%")
print("Kelas 6 (165 - 179):", len(kelas6) / len(data) * 100, "%")

