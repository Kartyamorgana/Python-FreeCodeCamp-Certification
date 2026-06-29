names = ['Andi', 'Budi', 'Citra', 'Dedi']
ages  = [30, 25, 28, 35]

names_ages = list(tuple(zip(names, ages)))

sort_names_ages = sorted(names_ages, key=lambda x: x[1], reverse=True)

for name, ages in sort_names_ages:
    print(f"{name} - {ages} tahun")
