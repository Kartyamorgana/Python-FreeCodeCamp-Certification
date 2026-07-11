def hitung_diskon(harga, persen):
    if persen > 100 or persen < 0:
        print('Masukkan persen yang valid!')
        return
    elif harga < 0:
        print('Masukkan harga yang valid')
        return
    else:
        hargaDiskon = harga * persen / 100
        print(f'Memproses harga={harga}, persen={persen}')
        print(f'Potongan={hargaDiskon}, harga akhir={harga - hargaDiskon}')
        return harga - hargaDiskon
    
print(hitung_diskon(999, 8))