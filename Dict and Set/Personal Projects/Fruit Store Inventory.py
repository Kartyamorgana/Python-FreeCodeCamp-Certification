inventory = {
    'apel': 10,
    'jeruk': 5,
    'mangga': 8,
    'anggur': 0,
    'pisang': 12
}

print("=== DAFTAR STOK ===")
for i, (productNames, quantity) in enumerate(inventory.items(), start=1):
    print(f"{i}. {productNames}: {quantity}")

total = 0
for quantity in inventory.values():
    total += quantity
print(f"\nTotal stok: {total}")

maxQty = 0
maxProduct = ''
for product, quantity in inventory.items():
    if quantity > maxQty:
        maxQty = quantity
        maxProduct = product
print(f"Buah dengan stok terbanyak: {maxProduct} (stok: {maxQty})")

inventory['jeruk'] += 3
print(f"Stok jeruk setelah penambahan: {inventory['jeruk']}")

inventory.update({'mangga': inventory['mangga'] + 2, 'nanas': 6})
inventory.pop('anggur')
print("Menghapus anggur...")

print("\n=== DAFTAR STOK AKHIR ===")
for i, (productNames, quantity) in enumerate(inventory.items(), start=1):
    print(f"{i}. {productNames}: {quantity}")
