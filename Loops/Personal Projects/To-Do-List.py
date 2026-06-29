print("""=== MENU TO-DO LIST ===
1. Tambah tugas
2. Lihat tugas
3. Hapus tugas
4. Cari tugas
5. Kosongkan semua
6. Keluar""")
daftar_tugas = []

while True:
    try:
        pilih = int(input("Pilih: "))

        if pilih == 1:
            new_task = input("Masukkan tugas: ")
            daftar_tugas.append(new_task)
            print("Tugas ditambahkan.")
        elif pilih == 2:
            if daftar_tugas:
                print("Daftar Tugas:")
                for index, task in enumerate(daftar_tugas, start=1):
                    print(f"{index}. {task}")
            else:
                print("Belum ada tugas! Mohon tambahkan tugas.")
        elif pilih == 3:
            if daftar_tugas:
                delete_task = int(input("Hapus tugas nomor: "))
                if delete_task <= len(daftar_tugas) and delete_task >= 1:
                    daftar_tugas.pop(delete_task - 1)
                else:
                    print("Nomor tugas tidak valid!")
            else:
                print("Tidak ada tugas untuk dihapus.")
        elif pilih == 4:
            if daftar_tugas:
                search_task = input("Cari tugas: ")
                found = False

                for task in daftar_tugas:
                    if search_task.lower() in task.lower():
                        print("Hasil pencarian: ")
                        print(f"- {task}")
                        found = True
                if not found:
                    print(f"{search_task} tidak ditemukan!")
            else:
                print("Tugas masih kosong!")
        elif pilih == 5:
            if daftar_tugas:
                daftar_tugas.clear()
                print("Semua tugas dihapus.")     
            else:
                print("Tugas masih kosong!")
        elif pilih == 6:
            print("Sampai jumpa!")
            break
        else:
            print("Masukkan angka yang valid!")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        