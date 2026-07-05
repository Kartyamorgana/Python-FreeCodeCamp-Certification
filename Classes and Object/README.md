### 1. Kelas dan Objek: Cara Kerja dan Perbedaan

Di Python, **kelas** (*class*) dan **objek** (*object*) bekerja sama untuk mengatur dan mengelola data. Anda membangun sebuah kelas untuk mendefinisikan perilaku bersama, lalu membuat objek yang menggunakan perilaku tersebut. Dengan kata lain, **kelas adalah seperti cetak biru** (*blueprint*) atau templat yang digunakan untuk menciptakan objek.

#### Membuat Kelas

Gunakan kata kunci `class` diikuti nama kelas dan titik dua. Di dalam kelas, Anda dapat menambahkan *initializer* (`__init__`), serta atribut dan metode.

*   **Atribut** ibarat variabel di dalam kelas, digunakan untuk menyimpan data.
*   **Metode** adalah fungsi yang didefinisikan di dalam kelas, merupakan aksi yang dapat dilakukan oleh objek yang dibuat dari kelas tersebut.

**Sintaks dasar kelas:**

```python
class ClassName:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sample_method(self):               
        print(self.name.upper())
```

*   `class ClassName`: Kata kunci `class` digunakan untuk membuat kelas, diikuti oleh nama kelas (di sini `ClassName`). Lazimnya Python menggunakan konvensi `PascalCase` untuk nama kelas.
*   `def __init__(self, name, age)`: Metode khusus ini (disebut konstruktor) otomatis dipanggil saat objek baru dibuat. Fungsinya untuk menginisialisasi atribut objek yang akan diciptakan. Parameter pertama `__init__` selalu merujuk pada objek spesifik yang sedang dibuat/digunakan. Menurut konvensi, parameter ini dinamai `self` (secara teknis boleh nama lain). `self` memungkinkan akses ke atribut dan metode milik objek itu sendiri.
*   `self.name = name` dan `self.age = age`: Ini adalah atribut yang akan dimiliki objek.
*   `def sample_method(self):`: Ini adalah metode yang dapat dipanggil oleh setiap objek.
*   `print(self.name.upper())`: Ini adalah aksi yang dilakukan metode, dalam contoh ini mencetak nama dalam huruf kapital.

#### Membuat Objek dari Kelas

Setelah kelas didefinisikan, Anda bisa membuat objek (atau instans) dari kelas tersebut dengan sintaks:

```python
object_1 = ClassName(attribute_1, attribute_2)
object_2 = ClassName(attribute_1, attribute_2)
```

Dan memanggil metode pada objek tersebut:

```python
object_1.method_name()
object_2.method_name()
```

**Contoh dengan kelas `Dog`:**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

dog_1.bark()  # Output: JACK says woof woof! I'm 3 years old!
dog_2.bark()  # Output: THATCHER says woof woof! I'm 5 years old!
```

Saat membuat `dog_1`, kita melewatkan `"Jack"` dan `3` yang menetapkan atribut `name` dan `age` untuk *instance* tersebut. Begitu pula `dog_2` dengan `"Thatcher"` dan `5`. Ketika metode `.bark()` dipanggil, masing-masing objek menggunakan atributnya sendiri.

**Kesimpulan perbedaan kelas dan objek:**

*   **Kelas** adalah templat/cetak biru.
*   **Objek** adalah hasil nyata dari cetak biru tersebut (sebuah *instance*).
*   Kelas mendefinisikan data dan perilaku apa yang harus dimiliki objek, sedangkan objek menyimpan data aktual dan menggunakan perilaku itu.
*   Anda menulis kelas satu kali, dan dapat membuat banyak objek darinya, masing-masing dengan data yang berbeda.

---

### 2. Atribut dan Metode: Definisi dan Cara Kerja

#### Atribut

Atribut adalah variabel yang dimiliki oleh suatu objek, digunakan untuk menyimpan data. Terdapat dua jenis atribut: **atribut instans** (*instance attributes*) dan **atribut kelas** (*class attributes*).

*   **Atribut instans** bersifat unik untuk setiap objek yang dibuat dari kelas. Atribut ini biasanya ditetapkan di dalam metode `__init__`.
*   **Atribut kelas** dimiliki oleh kelas itu sendiri dan dibagikan oleh semua instans dari kelas tersebut.

Untuk mengakses atribut, gunakan notasi titik (*dot notation*).

**Contoh:**

```python
class Dog:
    species = "French Bulldog"   # Atribut kelas

    def __init__(self, name):
        self.name = name         # Atribut instans

print(Dog.species)    # Output: French Bulldog

dog1 = Dog("Jack")
print(dog1.name)      # Output: Jack
print(dog1.species)   # Output: French Bulldog

dog2 = Dog("Tom")
print(dog2.name)      # Output: Tom
print(dog2.species)   # Output: French Bulldog
```

Atribut kelas dapat diakses langsung dari kelas itu sendiri (misalnya `Dog.species`). Sementara untuk atribut instans, Anda perlu membuat objek terlebih dahulu dan atribut tersebut akan terisi dengan data objek tersebut (misalnya `dog1.name`).

**Contoh kelas `Car`:**

```python
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.model)   # Output: Toyota Corolla
print(car_2.model)   # Output: Lamborghini Revuelto
print(car_1.color)   # Output: red
print(car_2.color)   # Output: green
```

#### Metode

Metode adalah fungsi yang didefinisikan di dalam kelas. Dengan metode, objek dapat melakukan aksi yang mengoperasikan atau memodifikasi datanya sendiri. Metode juga diakses dengan notasi titik.

**Contoh metode pada kelas `Dog`:**

```python
class Dog:
   species = "French Bulldog"

   def __init__(self, name):
       self.name = name

   def bark(self):
       # Metode bark akan mengembalikan string
       return f"{self.name} says woof woof!"

jack = Dog("Jack")
jill = Dog("Jill")
print(jack.bark())   # Output: Jack says woof woof!
print(jill.bark())   # Output: Jill says woof woof!
```

**Contoh metode pada kelas `Car`:**

```python
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def describe(self):
        return f"This car is a {self.color} {self.model}"

car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")
print(car_1.describe())   # Output: This car is a red Toyota Corolla
print(car_2.describe())   # Output: This car is a green Lamborghini Revuelto
```

#### Pertanyaan

1.  **Apa dua jenis atribut dalam Python?**  
    Jawaban: Atribut instans dan atribut kelas.
2.  **Apa yang diperlukan untuk mengakses atribut instans?**  
    Jawaban: Sebuah instans atau objek dari kelas.
3.  **Bagaimana cara mendefinisikan dan mengakses metode?**  
    Jawaban: Metode didefinisikan di dalam kelas sebagai fungsi, dan diakses pada objek menggunakan notasi titik (misalnya `objek.nama_metode()`).

---

### 3. Metode Spesial (Dunder Methods): Definisi dan Kegunaan

Metode spesial di Python, sering disebut *magic methods* atau *dunder methods* (kependekan dari *double underscores* karena diawali dan diakhiri dengan dua garis bawah), adalah metode yang diawali dan diakhiri dengan dua garis bawah (`__`). Contohnya: `__init__()`, `__len__()`, `__str__()`, `__eq__()`.

Anda mungkin sudah sering menggunakan metode ini tanpa sadar. Setiap kali menulis `3 + 4`, Python diam-diam memanggil `3.__add__(4)`. Memanggil langsung `__add__()` jarang dilakukan karena `3 + 4` jauh lebih jelas dan *Pythonic*.

Anggaplah metode spesial sebagai "sutradara" yang mengatur interaksi antara kode Anda dan interpreter Python.

Metode spesial **tidak perlu dipanggil secara langsung**. Python akan otomatis memanggilnya saat operasi tertentu terjadi:

*   **Operasi aritmetika**: `__add__()` untuk penjumlahan, `__sub__()` untuk pengurangan, `__mul__()` untuk perkalian, `__truediv__()` untuk pembagian, dll.
*   **Operasi string**: `__add__()` untuk penggabungan, `__mul__()` untuk pengulangan, `__format__()` untuk pemformatan, `__str__()` dan `__repr__()` untuk konversi objek ke representasi string.
*   **Operasi perbandingan**: `__eq__()` untuk kesetaraan (`==`), `__lt__()` untuk lebih kecil (`<`), `__gt__()` untuk lebih besar (`>`), dll.
*   **Operasi iterasi**: `__iter__()` untuk mengembalikan iterator, `__next__()` untuk mengambil item berikutnya.
*   **Manajemen konteks**: `__enter__()` dan `__exit__()` untuk penggunaan dengan `with` statement.

Tipe data bawaan (string, angka, dsb.) sudah tahu cara melakukan operasi-operasi tersebut. Namun, saat Anda membuat kelas sendiri, Python tidak otomatis tahu cara menanganinya. Di sinilah metode spesial berperan: Anda dapat menyesuaikan perilaku bawaan untuk objek dari kelas Anda.

**Contoh tanpa metode spesial:**

```python
class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

# print(len(book1))        # TypeError: object of type 'Book' has no len()
print(str(book1))        # Output: <__main__.Book object at 0x...> (representasi default kurang informatif)
print(book1 == book2)    # Output: False (karena Python membandingkan identitas memori, bukan konten)
```

*   `len(book1)` akan menghasilkan `TypeError` karena Python tidak tahu cara menghitung "panjang" objek `Book` tanpa definisi metode `__len__()`.
*   `str(book1)` memberikan representasi default yang kurang informatif tentang konten objek.
*   `book1 == book2` menghasilkan `False` karena, secara *default*, Python hanya membandingkan apakah dua objek adalah objek yang sama di memori, bukan apakah atribut-atributnya memiliki nilai yang sama.

**Solusi dengan metode spesial:**

```python
class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

   def __len__(self):
       # Mendefinisikan bagaimana fungsi len() bekerja untuk objek Book
       return self.pages

   def __str__(self):
       # Mendefinisikan representasi string yang user-friendly
       return f"'{self.title}' has {self.pages} pages"

   def __eq__(self, other):
       # Mendefinisikan kapan dua objek Book dianggap "sama" (berdasarkan jumlah halaman)
       # Penting untuk memeriksa tipe 'other' agar tidak Crash jika 'other' bukan Book
       if not isinstance(other, Book):
           return NotImplemented 
       return self.pages == other.pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1))        # Output: 420
print(len(book2))        # Output: 420
print(str(book1))        # Output: 'Built Wealth Like a Boss' has 420 pages
print(str(book2))        # Output: 'Be Your Own Start' has 420 pages
print(book1 == book2)    # Output: True (karena __eq__ kita membandingkan pages)
```

#### Contoh Nyata: Keranjang Belanja

Bayangkan keranjang belanja yang bisa:

*   Menambah item
*   Menghapus item
*   Mengetahui jumlah item
*   Melihat daftar item
*   Memeriksa apakah suatu item ada
*   Mengambil item berdasarkan indeks

Selain metode biasa (`add`, `remove`, `list_items`), Anda bisa menggunakan metode spesial untuk membuat objek `Cart` lebih intuitif dan "Pythonic":

*   `__len__()` untuk jumlah item (mengimplementasikan `len(cart)`)
*   `__iter__()` untuk mengulangi item (memungkinkan `for item in cart:`)
*   `__contains__()` untuk pengecekan `in` (memungkinkan `'item' in cart`)
*   `__getitem__()` untuk mengakses dengan indeks (memungkinkan `cart[index]`)

```python
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

    def __len__(self):
        # Mendefinisikan perilaku len(cart)
        return len(self.items)

    def __getitem__(self, index):
        # Mendefinisikan perilaku cart[index]
        return self.items[index]

    def __contains__(self, item):
        # Mendefinisikan perilaku 'item' in cart
        return item in self.items

    def __iter__(self):
        # Mendefinisikan perilaku iterasi (for item in cart)
        return iter(self.items)

# Penggunaan
cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

print("Items in cart (iterating):")
for item in cart:
    print(item)
# Output:
# Laptop
# Wireless mouse
# Ergo keyboard
# Monitor

print(f"Total items: {len(cart)}")           # Output: Total items: 4
print(f"Item at index 3: {cart[3]}")         # Output: Item at index 3: Monitor

print(f"'Monitor' in cart? {'Monitor' in cart}")   # Output: 'Monitor' in cart? True
print(f"'banana' in cart? {'banana' in cart}")     # Output: 'banana' in cart? False

cart.remove('Ergo keyboard')
print(f"Items after removal: {cart.list_items()}") # Output: Items after removal: ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana')      # Output: banana is not in cart
```

#### Pertanyaan

1.  **Metode spesial apa yang dipanggil saat operasi penjumlahan?**  
    Jawaban: `__add__()`.
2.  **Dari mana asal kata "dunder"?**  
    Jawaban: Dari singkatan *double underscore* (`__`).
3.  **Metode spesial apa yang dipanggil saat menggunakan operator lebih besar (`>`)?**  
    Jawaban: `__gt__()`.

---

### 4. Menangani Atribut Objek Secara Dinamis

Atribut menyimpan data yang menggambarkan keadaan atau perilaku objek. Biasanya, atribut ditetapkan secara langsung dalam kode, misalnya:

```python
class Car: 
    def __init__(self, brand, model): 
        self.brand = brand 
        self.model = model 

my_car = Car('Lamborghini', 'Gallardo') 
print(my_car.brand) # Output: Lamborghini 
print(my_car.model) # Output: Gallardo 
```

Namun, terkadang Anda tidak tahu atribut apa yang dibutuhkan sampai program berjalan. Misalnya, nama atribut berasal dari input pengguna atau berkas konfigurasi. Di sinilah **penanganan atribut secara dinamis** diperlukan. Python menyediakan empat fungsi bawaan untuk bekerja dengan atribut objek secara dinamis: `getattr()`, `setattr()`, `hasattr()`, dan `delattr()`.

#### `getattr()` – Membaca Atribut Saat Runtime

Fungsi `getattr()` memungkinkan Anda membaca atribut dari objek ketika namanya baru diketahui saat program berjalan. Jika atribut tidak ditemukan, ia melemparkan `AttributeError`, kecuali jika Anda memberikan nilai default opsional.

Sintaks:

```python
getattr(object, attribute_name, default_value_optional)
```

**Contoh:**

```python
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30) 

print(getattr(person, 'name'))          # Output: John Doe 
print(getattr(person, 'age'))           # Output: 30 
print(getattr(person, 'city', 'Unknown')) # Output: Unknown (default, karena 'city' tidak ada pada objek)
```

Keunggulan sesungguhnya terlihat saat nama atribut berasal dari variabel, seperti dari input pengguna:

```python
# Contoh simulasi input pengguna
# attr_name_input = input('Enter the attribute you want to see (name, age, city): ')
attr_name_input = 'name' # Anggap pengguna memasukkan 'name'
print(getattr(person, attr_name_input, 'Attribute not found')) # Output: John Doe

attr_name_input = 'email' # Anggap pengguna memasukkan 'email'
print(getattr(person, attr_name_input, 'Attribute not found')) # Output: Attribute not found
```
Jika pengguna memasukkan `name`, akan muncul `John Doe`; jika `email`, akan muncul `Attribute not found`.

#### `dir()` – Melihat Semua Atribut

Fungsi bawaan `dir()` mengembalikan daftar semua nama atribut dan metode yang tersedia pada suatu objek (atau modul, jika dipanggil tanpa argumen). Sering dikombinasikan dengan `getattr()` untuk menampilkan atribut data saja (mengabaikan metode dan dunder methods).

```python
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    
    def greet(self):
        return f"Hello, I'm {self.name}"

person = Person('John Doe', 30)

print("Semua atribut dan metode:")
print(dir(person))
# Output: ['__class__', ..., 'age', 'greet', 'name'] (daftar lengkap)

print("\nHanya atribut data:")
for attr_name in dir(person):
    # Filter atribut 'dunder' dan metode (callable)
    if not attr_name.startswith('__') and not callable(getattr(person, attr_name, None)):
        value = getattr(person, attr_name)
        print(f'{attr_name}: {value}')

# Output:
# age: 30
# name: John Doe
```
`callable()` adalah fungsi bawaan yang mengembalikan `True` jika objek dapat dipanggil (seperti fungsi atau metode). Pemeriksaan `not callable(...)` digunakan untuk melewati metode dan hanya menampilkan atribut data.

#### `setattr()` – Membuat atau Memperbarui Atribut Secara Dinamis

Fungsi `setattr()` digunakan untuk menambahkan atribut baru ke suatu objek atau memperbarui nilai atribut yang sudah ada, dengan menentukan nama atribut sebagai string.

Sintaks:

```python
setattr(object, attribute_name_string, value)
```

**Contoh:** memuat pengaturan dari kamus data (misalnya dari file konfigurasi).

```python
class Configuration:
    pass

settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url)   # Output: https://api.example.com
print(config_obj.timeout_sec)  # Output: 30

# Contoh memperbarui atribut yang sudah ada
setattr(config_obj, 'timeout_sec', 60)
print(config_obj.timeout_sec)  # Output: 60
```

#### `hasattr()` – Memeriksa Keberadaan Atribut

Fungsi `hasattr()` mengembalikan `True` jika objek memiliki atribut dengan nama tertentu, dan `False` jika tidak. Ini sangat berguna untuk mencegah `AttributeError` saat mencoba mengakses atribut yang mungkin tidak ada.

Sintaks:

```python
hasattr(object, attribute_name_string)
```

**Contoh validasi atribut produk:**

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25)
required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missing the required attribute: '{attr}'")
    else:
        print(f'{attr}: {getattr(product_a, attr)}')

# Output:
# name: T-Shirt
# price: 25
# ERROR: Product is missing the required attribute: 'inventory_id'
```

#### `delattr()` – Menghapus Atribut Secara Dinamis

Fungsi `delattr()` digunakan untuk menghapus atribut dari suatu objek. Ini setara dengan pernyataan `del object.attribute_name`. Jika atribut tidak ada, ia akan melemparkan `AttributeError`.

Sintaks:

```python
delattr(object, attribute_name_string)
```

**Contoh:** membersihkan atribut sensitif atau sementara sebelum menyimpan.

```python
class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token   # atribut sensitif
        self.temp_counter = 0     # atribut sementara

session = UserSession(101, 'a1b2c3d4e5')
attributes_to_clean = ['auth_token', 'temp_counter']

for attr in attributes_to_clean:
    if hasattr(session, attr): # Cek keberadaan sebelum menghapus
        delattr(session, attr)
        print(f'Removed attribute: {attr}')
    else:
        print(f'Attribute {attr} not found.')

print('\nFinal attributes remaining:')
for attr in dir(session):
    if not attr.startswith('__') and not callable(getattr(session, attr, None)):
        print(f' - {attr}: {getattr(session, attr)}')

# Output:
# Removed attribute: auth_token
# Removed attribute: temp_counter
# 
# Final attributes remaining:
#  - user_id: 101
```

#### Pertanyaan

1.  **Apa yang dapat dilakukan oleh fungsi `getattr()` dalam Python?**  
    Jawaban: Membaca nilai atribut dari suatu objek menggunakan nama atribut dalam bentuk string, yang berguna ketika nama atribut tidak diketahui hingga runtime.
2.  **Mengapa Anda ingin menangani atribut objek secara dinamis?**  
    Jawaban: Untuk membuat kode lebih fleksibel, terutama saat berinteraksi dengan konfigurasi yang dimuat dari luar, input pengguna, atau data yang strukturnya tidak tetap hingga runtime.
3.  **Sintaks yang benar untuk memeriksa apakah suatu objek memiliki atribut tertentu adalah?**  
    Jawaban: `hasattr(object, 'attribute_name')`

---

### 5. Ringkasan Kelas dan Objek

Bagian ini merangkum konsep-konsep kunci yang telah dibahas, memberikan gambaran umum untuk memperkuat pemahaman.

#### Kelas dan Objek di Python

*   **Definisi Kelas**: Sebuah cetak biru (templat) untuk menciptakan objek. Kelas mendefinisikan struktur data (atribut) dan perilaku (metode) yang akan dimiliki oleh setiap objeknya.
*   **Membuat Objek**: Objek adalah *instance* (contoh nyata) dari sebuah kelas. Objek dibuat dengan memanggil kelas seperti fungsi, disertai argumen yang diperlukan untuk metode `__init__`.
*   **Memanggil Metode pada Objek**: Metode dapat dipanggil pada objek menggunakan notasi titik, seperti `nama_objek.nama_metode()`.
*   **Perbedaan Kelas dan Objek**: Kelas adalah definisi abstrak yang dapat digunakan kembali, sedangkan objek adalah implementasi konkret dengan data dan *state*-nya sendiri.

**Contoh kelas `Dog`:**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name.upper()} says woof woof!')

dog1 = Dog('Jack', 3) # Membuat objek dog1 dari kelas Dog
dog2 = Dog('Thatcher', 5) # Membuat objek dog2 dari kelas Dog
dog1.bark()  # Output: JACK says woof woof!
dog2.bark()  # Output: THATCHER says woof woof!
```

#### Atribut

*   **Atribut Instans**: Variabel yang unik untuk setiap objek. Didefinisikan dalam metode `__init__()` menggunakan `self.nama_atribut = nilai`.
*   **Atribut Kelas**: Variabel yang dimiliki oleh kelas itu sendiri dan dibagikan oleh semua instans dari kelas tersebut. Didefinisikan langsung di dalam kelas, di luar metode apa pun.

```python
class Dog:
    species = 'Canis familiaris'  # Ini adalah atribut kelas
    def __init__(self, name):
        self.name = name        # Ini adalah atribut instans
```

#### Metode

*   **Metode**: Fungsi yang didefinisikan di dalam kelas dan beroperasi pada atribut objek. Parameter pertama metode instans wajib `self`.
*   **Mengakses Metode**: Panggil metode pada objek dengan notasi titik.

```python
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def describe(self):
        return f'This car is a {self.color} {self.model}'

my_car_1 = Car('red', 'Tesla Model S')
print(my_car_1.describe())   # Output: This car is a red Tesla Model S
```

#### Metode Dunder (Magic Methods)

*   **Definisi**: Metode spesial yang diawali dan diakhiri dengan dua garis bawah (`__`). Contoh: `__init__`, `__len__`, `__str__`, `__eq__`. Python menggunakannya secara internal untuk operasi bawaan.
*   **Pemanggilan tidak langsung**: Python otomatis memanggilnya saat operasi tertentu terjadi (aritmetika, string, perbandingan, iterasi). Anda mendefinisikannya untuk menyesuaikan perilaku objek Anda.
*   **Contoh Kelas `Book`:**

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def __len__(self):
        return self.pages # Memungkinkan len(book_obj)
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages" # Memungkinkan str(book_obj) atau print(book_obj)
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages == other.pages # Memungkinkan book1 == book2

book1 = Book('Built Wealth Like a Boss', 420)
print(len(book1))   # Output: 420
print(str(book1))   # Output: 'Built Wealth Like a Boss' has 420 pages
```

#### Contoh Nyata: Keranjang Belanja dengan Metode Dunder

```python
class Cart:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')
    def list_items(self):
        return self.items
    def __len__(self):
        return len(self.items)
    def __getitem__(self, index):
        return self.items[index]
    def __contains__(self, item):
        return item in self.items
    def __iter__(self):
        return iter(self.items)

cart = Cart()
cart.add('Laptop')
print(len(cart))        # Output: 1
print('Laptop' in cart) # Output: True
```