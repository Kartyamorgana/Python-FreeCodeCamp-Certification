print("=== TEMPERATURE CONVERTER SYSTEM ===")
print("Pilih konversi! C→F atau F→C.")
print("Ketik exit untuk keluar\n")

def temperatureConverter(opsi, value):
    if opsi == 'c':
        assert value >= -273.15, "Suhu tidak valid: di bawah nol mutlak."
        return f"{value}°C = {(value * 9/5) + 32}°F"
    elif opsi == 'f':
        assert value >= -459.67, "Suhu tidak valid: di bawah nol mutlak."
        return f"{value}°F = {(value - 32) * 5/9}°C"

while True:
    while True:
        opsi = input("Konversi apa (C/F)? ").lower()
        if opsi == "exit":
            break
        if opsi in ("c", "f"):
            break
        print("Pilihan tidak valid, masukkan C atau F.")

    if opsi == "exit":
        break

    while True:
        try:
            if opsi == "c":
                suhu = input("Masukkan suhu Celcsius: ")
            elif opsi == "f":
                suhu = input("Masukkan suhu Farenheit: ")
            
            if suhu == 'exit':
                break

            hasil = temperatureConverter(opsi, float(suhu))
        except ValueError:
            print("Input harus berupa angka.")
        except AssertionError as e:
            print(e)
        else:
            print(hasil)
            break
print("Program selesai.")