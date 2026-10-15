percobaan = 1
stored_username = "admin"
stored_password = "password123"

class InvalidCredentialsError(Exception):
    def __init__(self, message):
        super().__init__(message)

class AccountLockedError(Exception):
    def __init__(self, message):
        super().__init__(message)

def cekInvalid(username, password):
    if username == "" or password == "":
        raise InvalidCredentialsError("Error: Username/password tidak boleh kosong")
    elif username != stored_username or password != stored_password:
        raise InvalidCredentialsError("Error: Username atau password salah.")

def cekPercobaan(percobaan):
    if percobaan > 3:
        raise AccountLockedError("KESEMPATAN HABIS! AKUN TERKUNCI!")

print("=== SIMPLE LOGIN SYSTEM ===")
print("Masukkan username dan password! Maksimal 3 percobaan!")

while True:
    try:
        cekPercobaan(percobaan)
        username = input('Username: ')
        password = input('Password: ')
        cekInvalid(username, password)
    except InvalidCredentialsError as e:
        print(e)
        percobaan += 1
    except AccountLockedError as e:
        print(e)
        break
    else:
        print("Selamat datang, admin!")
        break
print("Program selesai.")