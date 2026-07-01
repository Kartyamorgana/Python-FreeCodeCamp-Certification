if __name__ == '__main__':
    transaksi = [
        ('Kemeja', 5, 80000),
        ('Celana', 3, 120000),
        ('Kaos', 10, 50000),
        ('Jaket', 2, 250000),
        ('Topi', 8, 30000),
        ('Kaos', 4, 50000)  # Kaos muncul dua kali
    ]
    semua_produk = {'Kemeja', 'Celana', 'Kaos', 'Jaket', 'Topi', 'Sepatu', 'Sandal'}

    pendapatan_per_produk = {}
    unit_per_produk = {}

    for produk, jumlah, harga in transaksi:
        total = jumlah * harga

        if produk in pendapatan_per_produk:
            pendapatan_per_produk[produk] += total
        else:
            pendapatan_per_produk[produk] = total

        if produk in unit_per_produk:
            unit_per_produk[produk] += jumlah
        else:
            unit_per_produk[produk] = jumlah

    print("=== RINGKASAN PENDAPATAN PER PRODUK ===")
    for i, (produk, pendapatan) in enumerate(pendapatan_per_produk.items(), start=1):
        print(f"{i}. {produk}: Rp {pendapatan:,}".replace(',', '.'))

    total_pendapatan = 0
    for pendapatan in pendapatan_per_produk.values():
        total_pendapatan += pendapatan
    print(f"\nTotal pendapatan: Rp {total_pendapatan:,}".replace(',', '.'))

    max_unit = 0
    produk_terlaris = ''
    for produk, unit in unit_per_produk.items():
        if unit > max_unit:
            max_unit = unit
            produk_terlaris = produk
    print(f"Produk terlaris (unit): {produk_terlaris} ({max_unit} unit)")

    max_pendapatan = 0
    produk_tertinggi = ''
    for produk, pendapatan in pendapatan_per_produk.items():
        if pendapatan > max_pendapatan:
            max_pendapatan = pendapatan
            produk_tertinggi = produk
    print(f"Produk dengan pendapatan tertinggi: {produk_tertinggi} (Rp {max_pendapatan:,})".replace(',', '.'))

    produk_terjual = set()
    for produk in pendapatan_per_produk.keys():
        produk_terjual.add(produk)
    print("\n=== PRODUK TIDAK TERJUAL ===")
    print(semua_produk - produk_terjual)

    pendapatan_per_produk.pop('Topi')
    print("\nSetelah penghapusan Topi:")
    print(pendapatan_per_produk)