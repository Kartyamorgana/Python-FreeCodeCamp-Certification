class InvalidTemperatureError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Temperature:
    def __init__(self, celcius):
        if celcius <= -273.15:
            raise InvalidTemperatureError("Error: Suhu tidak boleh di bawah nol mutlak.")
        else:
            self.celcius = celcius

    def __str__(self):
        return f"{self.celcius}°C ({(self.celcius * 9 / 5) + 32}°F)"

    def __eq__(self, value):
        if not isinstance(value, Temperature):
            return NotImplemented
        return self.celcius == value.celcius

    def __lt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celcius < other.celcius

    def __gt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celcius > other.celcius

    def __add__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return Temperature(self.celcius + other.celcius)

    @classmethod
    def from_farenheit(cls, value):
        celcius = (value - 32) * 5 / 9
        return cls(celcius)

try:
    
    suhu_1 = Temperature(25)
    suhu_2 = Temperature(30)
    suhu_3 = Temperature.from_farenheit(212)

    print(suhu_1)
    print(suhu_2)
    print(suhu_3)

    print(f"Suhu 1 == Suhu 2? {suhu_1 == suhu_2}")
    print(f"Suhu 1 < Suhu 2? {suhu_1 < suhu_2}")
    print(f"Suhu 1 > Suhu 2? {suhu_1 > suhu_2}")
    print(f"Suhu 1 + Suhu 2 = {suhu_1 + suhu_2}")

    suhu_4 = Temperature(-1000)

except InvalidTemperatureError as e:
    print(e)
        