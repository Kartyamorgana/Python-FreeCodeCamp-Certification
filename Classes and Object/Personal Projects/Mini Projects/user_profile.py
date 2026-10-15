class UserProfile:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def add_attribute(self, name, value):
        if hasattr(self, name):
            print(f"Attribute {name} already exist!")
            return
        setattr(self, name, value)
        print(f"Atribut '{name}' ditambahkan: {value}")

    def get_attribute(self, name):
        return getattr(self, name, "Attribute not found")

    def has_attribute(self, name):
        return hasattr(self, name)

    def remove_attribute(self, name):
        if not hasattr(self, name):
            print(f"Attribute {name} doesn't exist!")
            return
        delattr(self, name)
        print(f"Atribut '{name}' dihapus.")

    def list_attributes(self):
        for attr_name in dir(self):
            if not attr_name.startswith("__") and not callable(getattr(self, attr_name, None)):
                value = getattr(self, attr_name)
                print(f"- {attr_name}: {value}")

    def __str__(self):
        return f"User: {self.username} ({self.email})"

    def load_from_dict(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                print(f"Skip '{key}': sudah ada!")
                continue
            setattr(self, key, value)

john_doe = UserProfile("john_doe", "john@example.com")
print(john_doe)
john_doe.add_attribute("age", 30)
john_doe.add_attribute("city", "Jakarta")

print("\n=== Daftar Atribut Data ===")
john_doe.list_attributes()
print()

print(f"Apakah 'age' ada? {john_doe.has_attribute('age')}")
print(f"Apakah 'phone' ada? {john_doe.has_attribute('phone')}")
print(f"Apakah 'city' ada? {john_doe.has_attribute('city')}")
john_doe.remove_attribute("city")

print("\n=== Daftar Atribut Data Baru ===")
john_doe.list_attributes()
print()

budi = UserProfile('budigamertzy6767', 'budiganteng123@example.com')
budi.load_from_dict({'name': 'Yanto', 'age': 17})
print(budi)

print("\n=== Daftar Atribut Budi ====")
budi.list_attributes()
print()
