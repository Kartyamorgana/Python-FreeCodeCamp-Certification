nilai = [78, 56, 90, 45, 88, 76, 60]

rata_rata = sum(nilai) / len(nilai)

diatas_rata = list(filter(lambda x: x > rata_rata, nilai))
print(f"Nilai di atas rata-rata: {diatas_rata}")