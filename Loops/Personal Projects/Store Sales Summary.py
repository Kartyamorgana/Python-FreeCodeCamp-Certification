transaksi = [
    ('Kemeja', 5, 80000),
    ('Celana', 3, 120000),
    ('Kaos', 10, 50000),
    ('Jaket', 2, 250000),
    ('Topi', 8, 30000)
]

print("=== REKAP PENJUALAN ===")
total_pendapatan = sum(map(lambda x: x[1] * x[2], transaksi))
print(f"Total pendapatan: Rp {total_pendapatan:,}".replace(',', '.'))

print("\nProduk dengan penjualan terbanyak:")
maxQty = 0
for _, quantity, _ in transaksi:
    if quantity > maxQty:
        maxQty = quantity
produkTerbanyak = [item for item, quantity, _ in transaksi if quantity == maxQty]
for produk in produkTerbanyak:
    print(f"- {produk} ({maxQty} unit)")

print("\nTransaksi bernilai tinggi (> Rp 500.000):")
filtered = (item for item in transaksi if (item[1] * item[2]) >= 500000)
for i, (item, quantity, price) in enumerate(filtered, start=1):
    print(f"{i}. {item} - {quantity} x {price:,} = Rp {(quantity * price):,}".replace(',', '.'))


print("\nTop 3 transaksi terbesar:")
transaksiTerbesar = sorted(transaksi, key=lambda x: x[1] * x[2], reverse=True)[:3]
for i, (item, quantity, price) in enumerate(transaksiTerbesar, start=1):
    print(f"{i}. {item} - Total Rp {quantity * price:,}".replace(',', '.'))


