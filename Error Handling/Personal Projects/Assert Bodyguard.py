def validasi_usia(nama, usia):
    assert usia >= 0 and usia <= 120, 'Usia tidak boleh negatif atau lebih dari 120'
    assert nama != '', 'Nama tidak boleh kosong'
    return 'Data Valid'

try:
    print(validasi_usia('', 100))
except AssertionError as e:
    print(f"Error: {e}")