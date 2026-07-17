contacts = [
    {"nama": "Andi Pratama", "telepon": "081234567890"},
    {"nama": "Budi Santoso", "telepon": "082198765432"},
    {"nama": "Citra Dewi", "telepon": "085711223344"}
]

class InvalidContactError(Exception):
    def __init__(self, message):
        super().__init__(message)

class ContactNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)

def cekContactError(inputNama, inputNomor):
    if not inputNama.strip():
        raise InvalidContactError("Error: Nama tidak boleh kosong.")
    elif not inputNomor.strip():
        raise InvalidContactError("Error: Nomor tidak boleh kosong.")
    
    if not inputNomor.isdigit():
        raise InvalidContactError("Error: Nomor harus berupa angka.")

def cekFoundContact(input, contacts):
    if cari_kontak(input, contacts) is None:
        raise ContactNotFoundError(f"Error: Tidak ada {input} dalam kontak!")

def cari_kontak(nama, contacts):
    for kontak in contacts:
        if kontak["nama"] == nama:
            return kontak
    return None

def cari_nomor(nomor, contacts):
    for kontak in contacts:
        if kontak["telepon"] == nomor:
            return kontak
    return None

print(f"{"="*15} CONTACT MANAGER {"="*15}")

while True:
    print("\nMenu:\n1. Tambah Kontak\n2. Cari Kontak\n3. Hapus Kontak\n4. Edit Kontak\n5. Tampilkan Semua\n6. Keluar")

    try:
        pilih = int(input("Pilih: "))
    except ValueError:
        print("Error: Menu yang dimasukkan harus berupa angka!")
        continue

    if pilih == 6:
        print("Terimakasih.")
        break
    elif not contacts:
        print("Kontak masih kosong!")  
        continue
    elif pilih == 5:
        print(f"\n{"="*15} DAFTAR KONTAK {"="*15}")
        for i, kontak in enumerate(contacts, start=1):
            print(f"{i}. {kontak["nama"]} - {kontak["telepon"]}")
        print("-"*40)
        continue
    elif pilih == 4:
        print(f"\n{"="*15} DAFTAR KONTAK {"="*15}")
        for i, kontak in enumerate(contacts, start=1):
            print(f"{i}. {kontak["nama"]} - {kontak["telepon"]}")
        print("-"*40)
        try:
            editKontak = int(input("Masukkan index kontak yang akan diedit: "))
        except ValueError:
            print("Error: Index harus berupa angka!")
            continue
    elif pilih not in [1, 2, 3]:
        print("Error: Menu tidak tersedia!")
        continue   

    try:
        if pilih == 1:
            print(f"\n{"="*15} TAMBAH KONTAK {"="*15}")
            namaKontak = input("Masukkan nama kontak: ")
            nomorKontak = input("Masukkan nomor kontak: ")
            
            if cari_kontak(namaKontak, contacts) is not None:
                print(f"Nama {namaKontak} sudah ada di dalam kontak!")
                continue

            elif cari_nomor(nomorKontak, contacts) is not None:
                print(f"Nomor {nomorKontak} sudah ada di dalam kontak!")
                continue
            
            cekContactError(namaKontak, nomorKontak)
        elif pilih == 2 and contacts:
            print(f"\n{"="*15} CARI KONTAK {"="*15}")
            cariNama = input("Masukkan nama kontak yang dicari: ")
            cekFoundContact(cariNama, contacts)
        elif pilih == 3 and contacts:
            print(f"\n{"="*15} HAPUS KONTAK {"="*15}")
            hapusNama = input("Masukkan nama kontak yang akan dihapus: ")
            cekFoundContact(hapusNama, contacts)   
        elif pilih == 4 and contacts:
            if editKontak > 0 and editKontak <= len(contacts):
                namaBaru = input("Masukkan nama kontak yang baru: ")
                nomorBaru = input("Masukkan nomor kontak yang baru: ")
                cekContactError(namaBaru, nomorBaru)
                contacts[editKontak-1] = {"nama": namaBaru, "telepon": nomorBaru}
                print("Kontak berhasil diedit!")
                print("-"*40)
            else:
                print("Error: Index tidak valid!")
                continue
    except InvalidContactError as e:
        print(e)
    except ContactNotFoundError as e:
        print(e)
    except ValueError:
        print("Error: Nomor telepon harus berupa angka.")
    else:
        if pilih == 1:
            kontakBaru = {"nama": namaKontak, "telepon": nomorKontak}
            contacts.append(kontakBaru)
            print(f"Kontak: {namaKontak} ({nomorKontak}) berhasil ditambah ke kontak!")
            print("-"*40)
        elif pilih == 2 and contacts:
            print(f"Kontak: {cariNama} ({cari_kontak(cariNama, contacts)["telepon"]})")
            print("-"*40)
        elif pilih == 3 and contacts:
            print(f"Kontak: {hapusNama} ({cari_kontak(hapusNama, contacts)["telepon"]}) berhasil dihapus!")
            print("-"*40)
            contacts.remove(cari_kontak(hapusNama, contacts))
print("Program selesai.")
