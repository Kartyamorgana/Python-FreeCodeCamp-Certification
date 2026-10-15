class InvalidAmountError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InsufficientFundsError(Exception):
    def __init__(self, message):
        super().__init__(message)

def InvalidCheck(amount):
    if amount < 0:
        raise InvalidAmountError("Error: Jumlah harus lebih dari 0.")

def BalanceCheck(balance, amount):
    if balance < amount:
        raise InsufficientFundsError("Error: Saldo tidak mencukupi.")

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        InvalidCheck(amount)
        self.balance += amount
        print(f"Deposit Rp. {amount:,} berhasil. Saldo: Rp. {self.balance:,}".replace(',', '.'))

    def withdraw(self, amount):
        InvalidCheck(amount)
        BalanceCheck(self.balance, amount)
        self.balance -= amount
        print(f"Tarik Rp. {amount:,} berhasil. Saldo: Rp. {self.balance:,}".replace(',', '.'))

    def __str__(self):
        return f"{self.account_number} - {self.owner}: Rp. {self.balance:,}".replace(',', '.')

    def __eq__(self, value):
        if not isinstance(value, BankAccount):
            return NotImplemented
        return self.account_number == value.account_number

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            return NotImplemented
        InvalidCheck(amount)
        BalanceCheck(self.balance, amount)
        self.balance -= amount
        target_account.balance += amount
        print(f"Transfer Rp. {amount:,} ke {target_account.owner} berhasil. Saldo: Rp. {self.balance:,}".replace(',', '.'))

rekening_1 = BankAccount("ACC001", "Andi", balance=150000)
rekening_2 = BankAccount("ACC002", "Budi")

print(f"Keadaan Awal -> {rekening_1}")

# 1. Uji coba transaksi normal
print("\n--- Transaksi Normal ---")
try:
    rekening_1.deposit(50000)
    rekening_1.withdraw(20000)
except (InvalidAmountError, InsufficientFundsError) as e:
    print(e)

# 2. Uji coba error: Saldo kurang
print("\n--- Uji Coba Error: Saldo Kurang ---")
try:
    rekening_1.withdraw(500000) # Saldo tidak akan cukup
except (InvalidAmountError, InsufficientFundsError) as e:
    print(e)

# 3. Uji coba error: Nominal minus
print("\n--- Uji Coba Error: Nominal Minus ---")
try:
    rekening_1.deposit(-5000)
except (InvalidAmountError, InsufficientFundsError) as e:
    print(e)

# 4. Uji coba Method Magic (__eq__ dan transfer)
print("\n--- Uji Coba Fitur Akun ---")
print(f"Apakah Rekening 1 sama dengan Rekening 2? {rekening_1 == rekening_2}")

try:
    rekening_1.transfer(rekening_2, 30000)
except (InvalidAmountError, InsufficientFundsError) as e:
    print(e)

print(f"\nKeadaan Akhir -> Rekening 1: Rp. {rekening_1.balance:,} | Rekening 2: Rp. {rekening_2.balance:,}".replace(',', '.'))

