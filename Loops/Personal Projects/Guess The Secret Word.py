print("Tebak kata rahasia!")
guess = ''

while guess != 'python':
    guess = input("> ").lower()
    if guess != 'python':
        print("Salah, coba lagi!")
    else:
        print("Selamat! Anda benar.")
        break
        

    