class InvalidAgeError(Exception):
    """Exception untuk umur tidak valid"""
    def __init__(self, message):
        super().__init__(message)

def validasi_usia(usia):
    if usia < 0:
        raise InvalidAgeError("Usia tidak boleh negatif.")
    elif usia > 120:
        raise InvalidAgeError("Usia tidak boleh lebih dari 120.")

print("=== AGE VALIDATOR ===")
print("Cek validitas usia (0-120)")

while True:
    try:
        usia = int(input('Masukkan usia Anda: '))
        validasi_usia(usia)
    except ValueError:
        print("Masukkan angka yang valid.")
    except InvalidAgeError as e:
        print(e)
    else:
        print(f'Usia valid: {usia}')
        break
print('Program selesai')

