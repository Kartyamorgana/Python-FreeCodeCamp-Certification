nilai = int(input("Masukkan nilai (0 - 100): "))

def tentukan_grade(nilai):
    if nilai < 0 or nilai > 100:
        return 'Masukkan angka yang valid! (0-100)'
    else:
        if nilai < 50:
            grade = 'E'
            status = 'Gagal'
            return grade, status
        elif 50 <= nilai < 60:
            grade = 'D'
            status = 'Gagal'
            return grade, status
        elif 60 <= nilai < 70:
            grade = 'C'
            status = 'Gagal'
            return grade, status
        elif 70 <= nilai < 85:
            grade = 'B'
            status = 'Lulus'
            return grade, status
        else:
            grade = 'A'
            status = 'Lulus'
            return grade, status

grade, status = tentukan_grade(nilai)
print(f"Grade Anda: {grade}")
print(f"Status: {status}")

