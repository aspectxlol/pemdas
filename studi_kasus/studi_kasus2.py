s = input("Masukkan teks: ").lower()
vokal = {
  'a': 0,
  'e': 0,
  'i': 0,
  'o': 0,
  'u': 0,
}
jml_vokal = 0

for c in list(s):
  if c in vokal:
    vokal[c] += 1
    jml_vokal += 1

print("Panjang teks : ", len(s))
print("Jumlah vokal : ", jml_vokal)
print("Jumlah masing masing vokal : ")
for char in vokal.keys():
  print(f"{char}: {vokal[char]}")