kumpulan_soal = [
    (
        "Planet manakah yang dikenal sebagai Planet Merah?",
        "Mars",
        "Venus",
        "Yupiter",
        "A"
    ),
    (
        "Berapakah hasil dari 15 dikalikan dengan 4, lalu dikurangi 20?",
        "30",
        "40",
        "50",
        "B"
    ),
    (
        "Mamalia darat terbesar di dunia saat ini adalah...",
        "Badak",
        "Gajah Afrika",
        "Kudanil",
        "B"
    ),
    (
        "Siapakah penemu lampu pijar yang paling terkenal?",
        "Nikola Tesla",
        "Albert Einstein",
        "Thomas Alva Edison",
        "C"
    ),
    (
        "Jika hari ini adalah hari Jumat, hari apakah 3 hari yang lalu?",
        "Selasa",
        "Rabu",
        "Kamis",
        "A"
    ),
    (
        "Senjata tradisional Kujang berasal dari provinsi...",
        "Jawa Barat",
        "Jawa Tengah",
        "Jawa Timur",
        "A"
    )
]

jumlahSoal = len(kumpulan_soal)
jawabanBenar = 0
listJawabanBenar = []
listJawabanSalah = []

class InvalidChoiceError(Exception):
    def __init__(self, message):
        super().__init__(message)

def cekPilihan(pilihan):
    if pilihan.upper() not in ("A", "B", "C"):
        raise InvalidChoiceError("Error: Pilihan harus A, B, atau C.")

print(f"{"="*15} QUIZ {"="*15}")

for i, (pertanyaan, pilihan_a, pilihan_b, pilihan_c, jawaban_benar) in enumerate(kumpulan_soal, start=1):
    print(f"Pertanyaan {i}: {pertanyaan}\nA. {pilihan_a}\nB. {pilihan_b}\nC. {pilihan_c}")

    while True:
        try:
            jawaban = input("Jawaban (A/B/C): ")
            cekPilihan(jawaban)
        except InvalidChoiceError as e:
            print(e)
        else:
            break
    
    soal_saat_ini = (pertanyaan)

    if jawaban.upper() == jawaban_benar:
        print("Benar!")
        jawabanBenar += 1
        listJawabanBenar.append(soal_saat_ini)
    else:
        print("Salah!")
        listJawabanSalah.append(soal_saat_ini)

print()
print("="*30)
print(f"Skor akhir: {jawabanBenar}/{jumlahSoal}")
print("="*30)

print("="*30)
print("List jawaban benar: ")
for i, pertanyaan in enumerate(listJawabanBenar, start=1):
    if listJawabanBenar:
        print(f"Pertanyaan dengan jawaban benar {i}: {pertanyaan}")
    else:
        print("Tidak ada jawaban yang benar!")
print("="*30)

print("="*30)
print("List jawaban salah: ")
for i, pertanyaan in enumerate(listJawabanSalah, start=1):
    if listJawabanSalah:
        print(f"Pertanyaan dengan jawaban salah {i}: {pertanyaan}")
    else:
        print("Tidak ada jawaban yang salah!")
print("="*30)