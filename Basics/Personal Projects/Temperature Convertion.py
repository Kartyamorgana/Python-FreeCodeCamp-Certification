suhu = float(input("Masukkan suhu dalam Celcius: "))

def c_to_f(c):
    return (c * 9/5) + 32

def c_to_k(c):
    return c + 273.15

print(f"Suhu {suhu}°C = {c_to_f(suhu), 2}°F = {c_to_k(suhu), 2}K")