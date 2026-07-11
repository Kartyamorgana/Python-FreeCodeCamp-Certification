class SaldoTidakCukupError(Exception):
    def __init__(self, saldo, jumlah):
        self.saldo = saldo
        self.jumlah = jumlah
        message = f'Saldo tidak mencukupi. Saldo: {saldo}, diminta: {jumlah}'
        super().__init__(message)

def tarik_tunai(saldo, jumlah):
    if jumlah > saldo:
        raise SaldoTidakCukupError(saldo, jumlah)
    
    return saldo - jumlah

try:
    transaksi = tarik_tunai(1, 45)
except SaldoTidakCukupError as e:
    print(f"Transaksi gagal: {e}")
else:
    print("Transaksi berhasil! Sisa saldo:", transaksi)