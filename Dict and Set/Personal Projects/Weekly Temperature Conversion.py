suhu_c = {
    'Senin': 30,
    'Selasa': 32,
    'Rabu': 29,
    'Kamis': 31,
    'Jumat': 33,
    'Sabtu': 28,
    'Minggu': 30
}

suhu_f = {}

print("Suhu Celcius:")
for i, (hari, suhu) in enumerate(suhu_c.items(), start=1):
    suhuF = (suhu * 9 / 5) + 32
    suhu_f[hari] = suhuF

    print(f"{i}. {hari}: {suhu}")

print("\nSuhu Fahrenheit:")
for i, (hari, suhu) in enumerate(suhu_f.items(), start=1):
    print(f"{i}. {hari}: {suhu}")


total = 0
suhuLength = 0
for suhu in suhu_c.values():
    total += suhu
    suhuLength += 1
print(f"\nRata-rata suhu Celcius: {round(total / suhuLength, 2)}")