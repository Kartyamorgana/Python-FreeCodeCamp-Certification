listHargaBarang = []
kodeDiskon = "DISKON10"

class InvalidPriceError(Exception):
    def __init__(self, message):
        super().__init__(message)

def cekInvalidInput(value):
    if value <= 0:
        raise InvalidPriceError("Error: Harga tidak boleh negatif atau nol.")

try: 
    while True:
        try:
            jumlahBarang = int(input("Masukkan jumlah barang: "))
            cekInvalidInput(jumlahBarang)
        except ValueError:
            print("Error: Input jumlah barang harus berupa angka!")
        except InvalidPriceError:
            print("Error: Input jumlah harus lebih dari 0.")
        else:
            break

    for i in range(jumlahBarang):
        while True:
            try:
                hargaBarang = float(input(f"Harga barang ke-{i+1}: "))
                cekInvalidInput(hargaBarang)
            except ValueError:
                print("Error: Input harga barang harus berupa angka!")
            except InvalidPriceError as e:
                print(e)
            else:
                listHargaBarang.append(hargaBarang)
                break

    inputDiskon = input("Kode diskon: ")
    if inputDiskon == kodeDiskon:
        hargaSetelahDiskon = sum(listHargaBarang) * 90 / 100
        diskon = "10%"
    else:
        hargaSetelahDiskon = sum(listHargaBarang)
        diskon = "0%"
except Exception as e:
    print(f"Error: {e}")
else:
    print("--- Ringkasan ---")
    print(f"Jumlah barang: {len(listHargaBarang)}")
    print(f"Total sebelum diskon: Rp. {sum(listHargaBarang):,}".replace(",", "."))
    print(f"Diskon: {diskon}")
    print(f"Total akhir: Rp. {hargaSetelahDiskon:,}".replace(",", "."))
    print(f"Harga termurah: Rp. {min(listHargaBarang):,}".replace(",", "."))
    print(f"Harga termahal: Rp. {max(listHargaBarang):,}".replace(",", "."))
finally:
    print("Terima kasih telah berbelanja!")