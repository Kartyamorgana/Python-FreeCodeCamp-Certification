print("=== SAFE DIVISION CALCULATOR ===")
print("    (ketik exit untuk keluar)   ")

while True:
    angka1 = input('Masukkan angka pertama: ')
    if angka1 == 'exit':
        break
        
    angka2 = input('Masukkan angka kedua: ')
    if angka2 == 'exit':
        break

    try:
        hasil = float(angka1) / float(angka2)
    except ZeroDivisionError:
        print('Tidak dapat membagi dengan 0')
    except ValueError:
        print('Input harus berupa angka.')
    else:
        print(f'Hasil: {hasil}')
    finally:
        print('Operasi selesai.')
print('Program selesai.')