class DataCorruptionError(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    semuaAngka = []
    while True:
        deretAngka = input("Masukkan deret angka (kosong (enter) untuk selesai): ")
        if deretAngka.strip() == "":
            break
        splitDeret = deretAngka.split()
        for elemen in splitDeret:
            try:
                floatDeret = float(elemen)
            except ValueError as e:
                raise DataCorruptionError(f"Error: Data corrupt pada elemen '{elemen}'") from e
            else:
                semuaAngka.append(floatDeret)
    if not semuaAngka:
        print("Tidak ada data valid.")
    else:
        rataRata = sum(semuaAngka) / len(semuaAngka)
except DataCorruptionError as e:
    print(e)
    print(f"Disebabkan oleh:", e.__cause__)
else:
    if semuaAngka:
        print(f"Rata-rata: {rataRata}")