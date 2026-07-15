angkaRahasia = 42
percobaan = 1

class InvalidGuessError(Exception):
    def __init__(self, message):
        super().__init__(message)

class GameOverError(Exception):
    def __init__(self, message):
        super().__init__(message)

def cekGuess(angka):
    if angka > 100 or angka < 1:
        raise InvalidGuessError('Error: Tebakan harus antara 1 dan 100.')

def cekGame(kesempatan):
    if kesempatan > 5:
        raise GameOverError(f'GAME OVER! Jawaban: {angkaRahasia}')
    
print("=== GUESSING GAME ROBUST ===")
print("Tebak angka rahasia! Hanya ada 5 kesempatan menebak!")

while True:
    try:
        cekGame(percobaan)
        angka = int(input('Tebak angka (1-100): '))
        cekGuess(angka)
    except ValueError:
        print('Error: Input harus berupa bilangan bulat.')
    except InvalidGuessError as e:
        print(e)
    except GameOverError as e:
        print(e)
        break
    else:
        if angka > angkaRahasia:
            print('Terlalu besar!')
            percobaan += 1
        elif angka < angkaRahasia:
            print('Terlalu kecil!')
            percobaan += 1
        else:
            print('Benar!')
            break
print('Game selesai.')