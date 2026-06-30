import math

bangun = {
    'lingkaran': 7,
    'persegi': 5,
    'segitiga_sama_sisi': 6
}

luas = {}

print("Luas Bangun Datar:")
for bentuk, nilai in bangun.items():
    if bentuk == 'lingkaran':
        luasBentuk = math.pi * nilai ** 2
    elif bentuk == 'persegi':
        luasBentuk = nilai ** 2
    elif bentuk == 'segitiga_sama_sisi':
        luasBentuk = (nilai ** 2 * math.sqrt(3)) / 4
    else:
        luasBentuk = 0

    luas[bentuk] = luasBentuk

for bentuk, nilai in luas.items():
    print(f"{bentuk}: {round(nilai, 2)}")
