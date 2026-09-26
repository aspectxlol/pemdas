print("Kemungkinan kombinasi angka yang memenuhi kondisi:")
for A in range(0, 10):
  for B in range(0, 10):
    for C in range(0, 10):
      for D in range(0, 10):
        if (A + B + C + D) != 15:
          continue

        if (A % 2 != 0):
          continue

        if (D % 3 == 0):
          continue

        if (B * 2 != C - 1):
          continue

        if len({A, B, C, D}) != 4:
          continue

        print(f"- {A}{B}{C}{D}")