if __name__ == '__main__':
    mahasiswa = [
        {'nim': '001', 'nama': 'Andi', 'nilai': 85},
        {'nim': '002', 'nama': 'Budi', 'nilai': 72},
        {'nim': '003', 'nama': 'Citra', 'nilai': 90},
        {'nim': '004', 'nama': 'Dedi', 'nilai': 55},
        {'nim': '005', 'nama': 'Eka', 'nilai': 68}
    ]

    total = 0
    counter = 0
    maxNilai = 0
    maxNama = ''
    semua_nim = set()

    print("=== DATA MAHASISWA ===")
    for i, m in enumerate(mahasiswa, start=1):
        print(f"{i}. {m['nim']} - {m['nama']} : {m['nilai']}")

        total += m['nilai']
        counter += 1

        if m['nilai'] > maxNilai:
            maxNilai = m['nilai']
            maxNama = m['nama']
        
        semua_nim.add(m['nim'])

    print(f"\nRata-rata nilai: {round(total / counter, 2)}")
    print(f"Mahasiswa dengan nilai tertinggi: {maxNama} ({maxNilai})")

    set_lulus = set()
    set_tidak_lulus = set()
    for m in mahasiswa:
        if m['nilai'] >= 60:
            set_lulus.add(m['nim'])
        else:
            set_tidak_lulus.add(m['nim'])

    print("\n=== KELULUSAN ===")
    print(f"Lulus (NIM): {set_lulus}")
    print(f"Tidak lulus (NIM): {set_tidak_lulus}")

    print(f"\nVerifikasi tidak lulus (difference): {semua_nim - set_lulus}")

    for m in mahasiswa:
        if m['nim'] == '004':
            m['nilai'] = 60
            break

    set_lulus = {m['nim'] for m in mahasiswa if m['nilai'] >= 60}
    set_tidak_lulus = {m['nim'] for m in mahasiswa if m['nilai'] < 60}

    print("\n--- Setelah perbaikan nilai Dedi menjadi 60 ---")
    print(f"Lulus terbaru (NIM): {set_lulus}")
    print(f"Tidak lulus terbaru (NIM): {set_tidak_lulus}")