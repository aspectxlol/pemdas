kode_morse = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.', 
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---', 
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---', 
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-', 
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--', 
    'Z': '--..',   
    '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',  '5': '.....', 
    '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',  '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',  '-': '-....-',
    '(': '-.--.',  ')': '-.--.-'
}

morse_kode = {value: key for key, value in kode_morse.items()}

def enkripsi(pesan):
  msg = str(pesan).upper()
  words = msg.split(" ")
  return "  ".join(
    " ".join(kode_morse[letter] for letter in word)
    for word in words
  )

def dekripsi(pesan):
  words = str(pesan).split("  ")
  return " ".join(
    "".join(morse_kode[code] for code in word.split())
    for word in words
  )

pesan = input("Masukkan Pesan :")
pesan = pesan.upper()
encrypted = enkripsi(pesan)
decrypted = dekripsi(encrypted)

print(f"Encrypted : {encrypted}")
print(f"Decrypted : {decrypted}")