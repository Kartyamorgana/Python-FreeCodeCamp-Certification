items = ['Buku', 'Pensil', 'Penghapus']
prices = [5000, 2000, 1000]

items_prices = list(zip(items, prices))
for index, items in enumerate(items_prices, start=1):
    item, price = items
    print(f"{index}. {item} Rp{price}")