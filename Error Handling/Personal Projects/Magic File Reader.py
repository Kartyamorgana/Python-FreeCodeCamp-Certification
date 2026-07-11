file = input('Masukkan nama file: ')

try:
    with open(file, 'r') as f:
        data = f.read()
        hasil = int(data)
except FileNotFoundError:
    print('File tidak ditemukan!')
except ValueError:
    print('Isi file bukan angka!')
else:
    print('Angka keberuntungan:', hasil)
