semua_karyawan = {101, 102, 103, 104, 105, 106, 107, 108, 109, 110}
hadir_hari_ini = {101, 102, 105, 108, 110}

print(f"Karyawan yang tidak hadir: {semua_karyawan - hadir_hari_ini}")
print(f"Apakah ID 105 hadir? {105 in hadir_hari_ini}")

hadir_hari_ini.add(103)
print(f"Setelah penambahan ID 103: {hadir_hari_ini}")

hadir_hari_ini.remove(108)
hadir_hari_ini.discard(999)
print(f"Setelah penghapusan ID 108 dan discard 999: {hadir_hari_ini}")

print(f"Daftar tidak hadir terbaru: {semua_karyawan - hadir_hari_ini}")