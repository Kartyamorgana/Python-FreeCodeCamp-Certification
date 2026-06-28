teks = input("Masukkan kalimat: ")

print(f"Panjang kalimat: {len(teks)} karakter")
print(f"Mengandung kata 'Python'? {'python' in teks.lower()}")
print(f"Huruf besar: {teks.upper()}")
print(f"Huruf kecil: {teks.lower()}")
print(f"Terbalik: {teks[::-1]}")
print(f"Jumlah huruf 'a': {teks.lower().count('a')}")