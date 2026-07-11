num = input('Masukkan angka: ')
try:
    hasil = 100 / int(num)
except ValueError:
    print('Input bukan angka yang valid!')
except ZeroDivisionError:
    print('Tidak bisa membagi dengan nol!')
else:
    print(f"Hasil: {hasil}")
finally:
    print('Program selesai.')