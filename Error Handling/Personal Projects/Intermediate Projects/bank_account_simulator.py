# --- CUSTOM EXCEPTIONS ---
class InsufficientFundsError(Exception):
    def __init__(self, saldo, value):
        self.value = value
        self.saldo = saldo
        super().__init__(f"Error: Saldo tidak mencukupi. Saldo saat ini: Rp {saldo:,}, diminta: Rp {value}:".replace(",", "."))

class InvalidAmountError(Exception):
    def __init__(self, message):
        super().__init__(message)

class DepositLimitError(Exception):
    def __init__(self, message):
        super().__init__(message)


# --- VALIDATION FUNCTIONS (Simetris & Modular) ---
def validasi_jumlah_dasar(value):
    """Validasi dasar untuk memastikan input angka di atas 0"""
    if value <= 0:
        raise InvalidAmountError("Error: Jumlah uang harus lebih besar dari 0.")

def cekDeposit(value):
    validasi_jumlah_dasar(value)
    if value > 1000000:
        raise DepositLimitError("Error: Jumlah melebihi batas! (Maksimal deposit: Rp 1.000.000)")

def cekTarikTunai(saldo, value):
    validasi_jumlah_dasar(value)
    if value > saldo:
        raise InsufficientFundsError(saldo, value)


# --- MAIN PROGRAM ---
saldo = 0
print("=== BANK ACCOUNT SIMULATOR ===")

while True:
    print("\nMenu:\n1. Deposit\n2. Tarik Tunai\n3. Cek Saldo\n4. Keluar")
    
    try:
        pilih = int(input("Pilih menu (1-4): "))
    except ValueError:
        print("Error: Menu yang dimasukkan harus berupa angka!")
        continue

    if pilih == 4:
        break
    elif pilih == 3:
        print(f"Saldo saat ini: Rp {saldo:,}".replace(",", "."))
        print("Transaksi selesai diproses.")
        continue
    elif pilih not in [1, 2]:
        print("Error: Menu tidak tersedia!")
        continue

    try:
        if pilih == 1:
            try:
                nominal = int(input("Jumlah deposit: "))
            except ValueError:
                raise InvalidAmountError("Error: Nominal deposit harus berupa angka bulat!")
            
            cekDeposit(nominal)
            saldo += nominal
            print("Deposit berhasil.")
            
        elif pilih == 2:
            try:
                nominal = int(input("Jumlah penarikan: "))
            except ValueError:
                raise InvalidAmountError("Error: Nominal penarikan harus berupa angka bulat!")
            
            cekTarikTunai(saldo, nominal)
            saldo -= nominal
            print("Tarik tunai berhasil.")
    
    except (InvalidAmountError, DepositLimitError, InsufficientFundsError) as e:
        print(e)
    finally:
        print("Transaksi selesai diproses.")

print("Program selesai. Terima kasih!")