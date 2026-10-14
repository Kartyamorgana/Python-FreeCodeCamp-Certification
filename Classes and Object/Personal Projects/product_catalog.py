class Product:
    currency = "IDR"

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.currency} {self.price} ({self.category})"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.category == other.category

    def __add__(self, other):
        return self.price + other.price

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __gt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price
    
class Catalog:
    def __init__(self):
        self.products = []

    def add_product(self, item):
        self.products.append(item)

    def total_value(self):
        total = 0
        for item in self.products:
            total += item.price
        return total

    def __len__(self):
        return len(self.products)

    def __contains__(self, item):
        if isinstance(item, str):
            return any(product.name == item for product in self.products)
        return item in self.products

    def filter_by_category(self, category):
        return [p for p in self.products if p.category == category]

laptop = Product("Laptop", 15000000, "Teknologi")
mouse = Product("Mouse", 250000, "Teknologi")
list_belanja = Catalog()

list_belanja.add_product(laptop)
list_belanja.add_product(mouse)

print(f"Total produk: {len(list_belanja)}")
print(f"Total nilai: {Product.currency} {list_belanja.total_value():,}".replace(',', '.'))

print("Produk dalam kategori Teknologi:")
for p in list_belanja.filter_by_category("Teknologi"):
    print(f"- {p}")

print(f"Apakah 'Laptop' ada? {'Laptop' in list_belanja}")
