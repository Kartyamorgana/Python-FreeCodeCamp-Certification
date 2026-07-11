## Catatan Lengkap Python: Pemrograman Berorientasi Objek (OOP)

### 1. Apa Itu Pemrograman Berorientasi Objek (OOP) dan Bagaimana Enkapsulasi Bekerja?

**Pemrograman Berorientasi Objek (OOP)** adalah paradigma pemrograman di mana program diorganisir di sekitar **objek** daripada logika dan fungsi. Dalam OOP, semuanya dipandang sebagai objek, mirip dengan entitas di dunia nyata.

Sebuah **kelas** berfungsi sebagai *blueprint* (cetak biru) untuk membuat objek. Setiap objek yang dibuat dari sebuah kelas memiliki:
*   **Atribut**: Properti atau karakteristik yang menyimpan data terkait objek.
*   **Metode**: Fungsi yang mendefinisikan perilaku atau tindakan yang dapat dilakukan objek.

#### Mengingat Kembali Sintaks Kelas

```python
class ClassName:
    # Metode konstruktor, dipanggil saat objek dibuat
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1 # Inisialisasi atribut objek
        self.attribute2 = parameter2 # 'self' mereferensikan instance objek saat ini

    # Metode lain yang mendefinisikan perilaku objek
    def method_name(self):
        # Logika atau operasi yang berhubungan dengan objek
        print(f"Ini adalah metode dari {self.__class__.__name__}")
```

**Contoh Kelas `Car`:**

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Atribut 'brand'
        self.color = color  # Atribut 'color'

# Membuat dua objek (instance) dari kelas Car
car1 = Car('Toyota', 'red')
car2 = Car('Lambo', 'green')

print('Car 1 Brand:', car1.brand)  # Output: Car 1 Brand: Toyota
print('Car 1 Color:', car1.color)  # Output: Car 1 Color: red

print('Car 2 Brand:', car2.brand)  # Output: Car 2 Brand: Lambo
print('Car 2 Color:', car2.color)  # Output: Car 2 Color: green
```

#### Empat Pilar Utama OOP

Pemrograman berorientasi objek dibangun di atas empat prinsip utama yang memfasilitasi desain kode yang terstruktur, modular, dan mudah dikelola:

1.  **Enkapsulasi** (*Encapsulation*)
2.  **Pewarisan** (*Inheritance*)
3.  **Polimorfisme** (*Polymorphism*)
4.  **Abstraksi** (*Abstraction*)

Pembahasan di bawah ini akan fokus pada detail **enkapsulasi**.

---

#### Enkapsulasi: Membungkus Data dan Perilaku dalam Satu Unit

**Enkapsulasi** adalah proses pembungkus atribut (data) dan metode (fungsi) yang beroperasi pada data tersebut ke dalam satu unit tunggal, yaitu kelas. Prinsip ini bertujuan untuk:
*   **Melindungi integritas data**: Mencegah akses langsung dan modifikasi data internal objek dari luar kelas.
*   **Menyederhanakan antarmuka**: Objek hanya mengekspos antarmuka publik yang sederhana, menyembunyikan detail implementasi yang kompleks.

Bayangkan sebuah dompet: Anda ingin membiarkan orang menyetor atau menarik uang, tetapi Anda tidak ingin siapa pun dapat mengubah saldo secara langsung tanpa melalui proses yang benar. Enkapsulasi memungkinkan Anda membuat metode `deposit()` dan `withdraw()` yang publik, sementara saldo (`_balance`) disembunyikan sebagai atribut internal.

**Konvensi Aksesibilitas Atribut/Metode dalam Python:**

Python tidak memiliki pengubah akses *private* atau *protected* eksplisit seperti pada bahasa lain (misalnya Java atau C++). Sebaliknya, Python menggunakan **konvensi penamaan** dan teknik **name mangling** untuk mengindikasikan tingkat aksesibilitas:

1.  **Awalan satu garis bawah (`_`): Untuk Penggunaan Internal (Konvensi)**
    Menunjukkan bahwa atribut atau metode tersebut dimaksudkan untuk penggunaan internal di dalam kelas atau modul. Meskipun masih dapat diakses dari luar, praktik terbaik adalah tidak melakukannya.
    ```python
    class Wallet:
        def __init__(self, balance):
            self._balance = balance   # Atribut internal, seharusnya tidak diakses langsung dari luar

        def deposit(self, amount):
            if amount > 0:
                self._balance += amount
                print(f"Deposited {amount}. Current balance: {self._balance}")
            else:
                print("Deposit amount must be positive.")

        def withdraw(self, amount):
            if 0 < amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew {amount}. Current balance: {self._balance}")
            else:
                print("Invalid withdrawal amount or insufficient funds.")

    my_wallet = Wallet(100)
    my_wallet.deposit(50)
    # Anda masih BISA mengakses _balance secara langsung, tapi disarankan untuk TIDAK
    # my_wallet._balance = 1000  # Melanggar enkapsulasi secara konvensional
    ```
    > **Catatan**: Mengakses `_balance` secara langsung dari luar kelas (`my_wallet._balance = 1000`) meski bisa, berpotensi merusak logika internal kelas dan melanggar prinsip enkapsulasi.

2.  **Awalan dua garis bawah (`__`): Untuk Atribut/Metode "Privat" (Name Mangling)**
    Python memberlakukan mekanisme **name mangling** untuk atribut atau metode yang diawali dengan dua garis bawah (`__`). Ini secara efektif menyulitkan akses langsung dari luar kelas dan bertujuan untuk mencegah penimpaan (overriding) yang tidak disengaja oleh *subclass*.

    ```python
    class Wallet:
        def __init__(self, initial_balance):
            self.__balance = initial_balance # Atribut "privat"

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                print(f"Deposited {amount}. Current balance: {self.__balance}")
            else:
                print("Deposit amount must be positive.")

        def withdraw(self, amount):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. Current balance: {self.__balance}")
            else:
                print("Invalid withdrawal amount or insufficient funds.")

    account = Wallet(500)
    # print(account.__balance)  # Ini akan menghasilkan AttributeError
                                # Output: AttributeError: 'Wallet' object has no attribute '__balance'
    ```
    Seperti yang terlihat dari `AttributeError`, `__balance` tidak dapat diakses secara langsung.

    Untuk mengakses atau memodifikasi atribut yang "privat" (dengan `__` prefix) secara terkendali, Anda perlu menyediakan metode publik (sering disebut *getter* dan *setter*).

    ```python
    class Wallet:
        def __init__(self, initial_balance):
            self.__balance = initial_balance

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount

        def withdraw(self, amount):
            if 0 < amount <= self.__balance:
                self.__balance -= amount

        def get_balance(self): # Metode getter untuk mendapatkan saldo
            return self.__balance

    acct_one = Wallet(100)
    acct_one.deposit(50)
    print("Saldo Akun Satu:", acct_one.get_balance()) # Output: Saldo Akun Satu: 150

    acct_two = Wallet(450)
    acct_two.withdraw(28)
    print("Saldo Akun Dua:", acct_two.get_balance()) # Output: Saldo Akun Dua: 422

    acct_two.deposit(150)
    print("Saldo Akun Dua Setelah Deposit:", acct_two.get_balance()) # Output: Saldo Akun Dua Setelah Deposit: 572
    ```

    Anda juga dapat menggunakan metode internal "privat" untuk validasi.

    ```python
    class Wallet:
        def __init__(self):
            self.__balance = 0

        def __validate_amount(self, amount): # Metode privat untuk validasi
            if amount < 0:
                raise ValueError('Amount must be positive')

        def deposit(self, amount):
            self.__validate_amount(amount)
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

        def withdraw(self, amount):
            self.__validate_amount(amount)
            if amount > self.__balance:
                raise ValueError('Insufficient funds')
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

        def get_balance(self):
            return self.__balance

    acct_one = Wallet()
    acct_one.deposit(3)  # Output: Deposited 3. New balance: 3
    print("Saldo:", acct_one.get_balance()) # Output: Saldo: 3

    acct_one.deposit(50) # Output: Deposited 50. New balance: 53
    print("Saldo:", acct_one.get_balance()) # Output: Saldo: 53

    try:
        acct_one.deposit(-4)   # Akan memicu ValueError
    except ValueError as e:
        print(f"Error: {e}")   # Output: Error: Amount must be positive

    try:
        acct_one.withdraw(58)  # Akan memicu ValueError (saldo hanya 53)
    except ValueError as e:
        print(f"Error: {e}")   # Output: Error: Insufficient funds
    ```
    Metode `__validate_amount` adalah "privat" dan bekerja di balik layar dalam metode publik `deposit()` dan `withdraw()` untuk memastikan bahwa jumlah yang dimasukkan selalu valid.

**Kesimpulan tentang Enkapsulasi**: Enkapsulasi melindungi data internal objek dengan menyediakan antarmuka publik yang terkontrol melalui metode (getter, setter, atau metode lain). Ini meningkatkan modularitas, keamanan data, dan mempermudah pemeliharaan kode karena perubahan implementasi internal tidak secara langsung mempengaruhi kode eksternal yang menggunakan objek.

---

#### Pertanyaan Seputar Enkapsulasi

1.  **Apa empat prinsip utama Pemrograman Berorientasi Objek (OOP)?**
    *   **Jawaban**: Enkapsulasi, Pewarisan, Polimorfisme, Abstraksi.

2.  **Mengapa praktik yang disarankan adalah tidak mengakses langsung atribut/metode yang diawali dengan satu garis bawah (`_`)?**
    *   **Jawaban**: Karena melanggar konvensi enkapsulasi, memungkinkan akses dan modifikasi data yang tidak terkontrol, serta berpotensi merusak internal kelas.

3.  **Bagaimana cara Python mengindikasikan atribut atau metode yang dimaksudkan sebagai "privat" dan tidak boleh diakses langsung dari luar kelas?**
    *   **Jawaban**: Dengan awalan dua garis bawah (`__`), yang memicu mekanisme *name mangling*.

---

### 2. Apa Itu Getter dan Setter?

**Getter** dan **setter** adalah metode khusus yang digunakan dalam OOP untuk mengontrol akses dan modifikasi atribut objek.
*   **Getter** (atau *accessor*) adalah metode untuk mengambil (membaca) nilai suatu atribut.
*   **Setter** (atau *mutator*) adalah metode untuk menetapkan (mengubah) nilai suatu atribut.

Di Python, cara paling "Pythonic" untuk membuat getter dan setter adalah dengan menggunakan **properti** (*properties*) melalui dekorator `@property`.

**Properti** memungkinkan Anda mengakses metode seolah-olah metode tersebut adalah atribut biasa. Ini berarti Anda dapat menjalankan logika tambahan (misalnya validasi) saat mengakses atau mengubah atribut, tanpa mengubah cara kode eksternal berinteraksi dengan objek (tetap menggunakan notasi titik `.` alih-alih `()`).

**Mengapa menggunakan *properties* dan bukan metode biasa?**
Properti meningkatkan keterbacaan dan konsistensi kode. Pengguna objek dapat mengakses atau memodifikasi atribut menggunakan sintaks yang sama (`obj.attribute`) seperti atribut biasa, bahkan jika ada logika kompleks yang berjalan di balik layar. Jika di masa mendatang Anda memutuskan memerlukan validasi atau komputasi untuk suatu atribut, Anda dapat mengubahnya menjadi properti tanpa harus mengubah semua kode yang menggunakan atribut tersebut.

#### Decorator `@property` untuk Getter

Di Python, **decorator** adalah konstruksi yang memungkinkan Anda memodifikasi atau memperluas fungsionalitas fungsi atau kelas yang sudah ada tanpa mengubah secara permanen kode aslinya. Untuk membuat *getter* sebagai properti, Anda menggunakan dekorator `@property` di atas definisi metode.

**Contoh Getter untuk Radius dan Luas Lingkaran:**

```python
class Circle:
    def __init__(self, radius):
        # Langsung panggil setter untuk memastikan validasi saat inisialisasi
        self.radius = radius

    @property # Ini mengubah metode 'radius' menjadi getter untuk properti 'radius'
    def radius(self):
        """Getter untuk mendapatkan nilai radius."""
        return self._radius # Mengembalikan nilai dari atribut internal _radius

    @property # Ini mengubah metode 'area' menjadi getter untuk properti 'area'
    def area(self):
        """Getter untuk menghitung dan mendapatkan luas lingkaran."""
        return 3.14159 * (self._radius ** 2)

my_circle = Circle(3) # Saat Circle(3) dipanggil, setter 'radius' akan dipanggil

print(f"Radius lingkaran saya: {my_circle.radius}") # Output: Radius lingkaran saya: 3
print(f"Luas lingkaran saya: {my_circle.area}")    # Output: Luas lingkaran saya: 28.27431
```
Perhatikan penggunaan `self._radius` di dalam kelas. Adanya garis bawah (`_`) adalah konvensi untuk menandakan bahwa `_radius` adalah atribut internal yang sejatinya tidak untuk diakses secara langsung dari luar kelas, melainkan melalui properti `radius`.

#### Setter dengan `@<nama_properti>.setter`

Untuk membuat *setter* bagi properti `radius`, Anda mendefinisikan metode dengan nama yang sama persis seperti *getter* (`radius`) dan menggunakan dekorator `@radius.setter`.

```python
class Circle:
    def __init__(self, radius):
        # Saat objek dibuat, setter 'radius' akan dipanggil
        self.radius = radius

    @property
    def radius(self):
        """Getter: Mengembalikan nilai radius."""
        return self._radius

    @radius.setter # Ini mengubah metode 'radius' menjadi setter untuk properti 'radius'
    def radius(self, value):
        """Setter: Mengatur nilai radius dengan validasi."""
        if value <= 0:
            raise ValueError('Radius must be positive and non-zero.')
        self._radius = value # Mengatur atribut internal _radius

my_circle = Circle(3)
print(f"Initial radius: {my_circle.radius}") # Output: Initial radius: 3

my_circle.radius = 8 # Saat ini dipanggil, setter @radius.setter akan dieksekusi
print(f"After modifying the radius: {my_circle.radius}") # Output: After modifying the radius: 8

try:
    my_circle.radius = -5 # Ini akan memicu ValueError karena validasi di setter
except ValueError as e:
    print(f"Error: {e}") # Output: Error: Radius must be positive and non-zero.
```
Pada contoh di atas, *setter* tidak hanya menetapkan nilai tetapi juga menjalankan validasi penting: radius harus positif.

Saat *getter* dan *setter* didefinisikan, Python secara otomatis memanggilnya di balik layar:
*   `my_circle.radius` akan memanggil metode yang dihias dengan `@property` (getter).
*   `my_circle.radius = 4` akan memanggil metode yang dihias dengan `@radius.setter` (setter).

> **Penting**: Di dalam *setter*, hindari menggunakan nama properti yang sama untuk penugasan (misalnya `self.radius = value`). Ini akan menyebabkan *setter* memanggil dirinya sendiri secara rekursif tak terbatas, yang mengakibatkan `RecursionError`. Selalu gunakan atribut internal (dengan garis bawah) untuk menyimpan nilai aktual: `self._radius = value`.

#### Deleter: Mengontrol Penghapusan Atribut

Anda juga dapat mengontrol apa yang terjadi saat atribut dihapus menggunakan operator `del` dengan mendefinisikan *deleter* menggunakan dekorator `@<nama_properti>.deleter`.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @radius.deleter # Ini mengubah metode 'radius' menjadi deleter untuk properti 'radius'
    def radius(self):
        """Deleter: Menangani penghapusan atribut radius."""
        print("Mendelete radius...")
        del self._radius # Menghapus atribut internal _radius

my_circle = Circle(33)
print("Initial radius:", my_circle.radius)  # Output: Initial radius: 33

del my_circle.radius   # Ini akan memanggil @radius.deleter
print("Radius telah dihapus!") # Output: Mendelete radius! \n Radius telah dihapus!

try:
    print(my_circle.radius) # Mencoba mengakses radius setelah dihapus
except AttributeError as e:
    print("Error:", e)  # Output: Error: 'Circle' object has no attribute '_radius'
```

**Ringkasan Penggunaan Getter, Setter, dan Deleter:**

*   **Getter (`@property`)**: Digunakan untuk membaca nilai atribut, bisa juga untuk komputasi nilai dinamis.
*   **Setter (`@nama_properti.setter`)**: Digunakan untuk menetapkan nilai atribut, seringkali dengan validasi atau transformasi data.
*   **Deleter (`@nama_properti.deleter`)**: Digunakan untuk mengontrol apa yang terjadi saat atribut dihapus.

---

#### Pertanyaan Seputar Getter dan Setter

1.  **Mekanisme apa yang memungkinkan Anda menjalankan logika di balik layar saat mengambil atau menetapkan nilai atribut, sambil tetap menggunakan sintaks akses atribut biasa?**
    *   **Jawaban**: Properti.

2.  **Dua dekorator utama apa yang digunakan untuk membuat *getter* dan *setter* untuk sebuah properti di Python?**
    *   **Jawaban**: `@property` untuk *getter* dan `@<nama_properti>.setter` untuk *setter*.

3.  **Mengapa penting untuk menggunakan atribut internal (dengan garis bawah, misal `self._attribute`) di dalam *setter* alih-alih nama properti (misal `self.attribute`)?**
    *   **Jawaban**: Untuk mencegah *setter* memanggil dirinya sendiri secara rekursif tak terbatas, yang akan menyebabkan `RecursionError`. Menggunakan atribut internal secara langsung memodifikasi penyimpanan data tanpa memicu *setter* lagi.

---

### 3. Apa Itu Pewarisan dan Bagaimana Pewarisan Mendorong Penggunaan Kembali Kode?

**Pewarisan** (*inheritance*) adalah salah satu pilar fundamental OOP yang memungkinkan sebuah kelas baru (**kelas anak/subclass**) untuk mengambil (_inherit_) atribut dan metode dari kelas yang sudah ada (**kelas induk/superclass/base class**). Konsep ini sangat efektif untuk:
*   **Penggunaan Kembali Kode (Code Reusability)**: Kode yang ditulis di kelas induk tidak perlu ditulis ulang di kelas anak.
*   **Membangun Hierarki Kelas**: Mengatur kelas-kelas dalam struktur "is-a" (misalnya, `Dog IS A Animal`, `Car IS A Vehicle`).
*   **Spesialisasi**: Kelas anak dapat menambahkan atribut dan metode baru atau mengubah (menimpa) perilaku yang diwarisi dari induknya.

#### Sintaks Dasar Pewarisan

```python
class ParentClass:
    # Atribut dan metode yang akan diwarisi
    pass

class ChildClass(ParentClass): # ChildClass mewarisi dari ParentClass
    # Atribut dan metode spesifik untuk ChildClass
    pass
```
`ChildClass` menerima `ParentClass` sebagai argumen dalam definisinya untuk menunjukkan hubungan pewarisan. Ini disebut **pewarisan tunggal** (*single inheritance*) karena kelas anak hanya mewarisi dari satu kelas induk.

**Contoh Sederhana Pewarisan:**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a generic sound.'

class Dog(Animal): # Kelas Dog mewarisi dari kelas Animal
    breed = 'Golden Retriever' # Atribut spesifik untuk Dog

    def bark(self):
        return 'Woof! Woof!'

# Membuat objek dari kelas Dog
my_dog = Dog('Buddy')

print(my_dog.name)        # Output: Buddy (Diwarisi dari Animal)
print(my_dog.sound())     # Output: Buddy makes a generic sound. (Diwarisi dari Animal)
print(my_dog.breed)       # Output: Golden Retriever (Atribut spesifik Dog)
print(my_dog.bark())      # Output: Woof! Woof! (Metode spesifik Dog)
```
Kelas `Dog` secara otomatis mendapatkan atribut `name` dan metode `sound()` dari kelas `Animal` tanpa perlu menulis ulang kode tersebut. `Dog` juga menambahkan atribut `breed` dan metode `bark()`-nya sendiri.

#### Menimpa (Overriding) Metode

Kelas anak dapat memberikan implementasi baru untuk metode yang sudah ada di kelas induk. Ini disebut **menimpa** (*overriding*).

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a generic sound.'

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Memanggil konstruktor kelas induk
        self.breed = breed

    def sound(self): # Menimpa metode sound() dari kelas Animal
        return f'{self.name} the {self.breed} barks loudly: WOOF!'

my_dog = Dog('Rex', 'German Shepherd')
print(my_dog.sound()) # Output: Rex the German Shepherd barks loudly: WOOF!
```
Ketika `my_dog.sound()` dipanggil, Python akan menggunakan implementasi `sound()` yang ada di kelas `Dog` karena telah ditimpa.

#### Memperluas (Extending) Metode dengan `super()`

Jika Anda ingin mempertahankan perilaku dari metode induk dan menambahkan fungsionalitas baru di kelas anak, Anda dapat memanggil metode induk menggunakan fungsi `super()`.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f'This is an animal named {self.name}.'

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Memanggil __init__ dari Animal
        self.breed = breed

    def describe(self):
        # Memanggil metode describe() dari kelas Animal dan menambahkan informasi
        parent_description = super().describe()
        return f'{parent_description} It is a {self.breed} and loves to play fetch.'

my_dog = Dog('Max', 'Labrador')
print(my_dog.describe())
# Output: This is an animal named Max. It is a Labrador and loves to play fetch.
```
`super().method_name()` memanggil metode `method_name` dari kelas induk dari kelas saat ini. Ini sangat berguna untuk memperluas fungsionalitas tanpa duplikasi kode.

#### Pewarisan Berganda (Multiple Inheritance)

Python mendukung **pewarisan berganda**, yang memungkinkan sebuah kelas anak mewarisi dari **lebih dari satu** kelas induk. Ini dapat menjadi kuat, tetapi juga dapat memperkenalkan kompleksitas seperti masalah "diamond problem" (konflik metode/atribut dari induk yang berbeda).

Sintaks dasar:

```python
class ParentOne:
    pass

class ParentTwo:
    pass

class Child(ParentOne, ParentTwo): # Child mewarisi dari ParentOne dan ParentTwo
    pass
```

**Contoh Pewarisan Berganda:**

```python
class Walker:
    def walk(self):
        return 'I can walk on land.'

class Swimmer:
    def swim(self):
        return 'I can swim in water.'

class Amphibian(Walker, Swimmer): # Amphibian mewarisi kemampuan walking dan swimming
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}"

frog = Amphibian('Freddy')
print(frog.introduce())
# Output: I'm Freddy the frog. I can walk on land. and I can swim in water.
```
Kelas `Amphibian` dapat menggunakan metode `walk()` dari `Walker` dan `swim()` dari `Swimmer`.

---

#### Pertanyaan Seputar Pewarisan

1.  **Apa tujuan utama pewarisan dalam OOP?**
    *   **Jawaban**: Untuk memungkinkan penggunaan kembali kode dengan memungkinkan kelas anak mewarisi dan memperluas atribut serta metode dari kelas induk, serta membangun hierarki kelas.

2.  **Apa itu pewarisan berganda di Python, dan bagaimana sintaksnya?**
    *   **Jawaban**: Pewarisan berganda adalah ketika sebuah kelas anak mewarisi dari lebih dari satu kelas induk. Sintaksnya adalah `class Child(Parent1, Parent2):`.

3.  **Ketika sebuah kelas anak ingin memanggil metode dari kelas induknya (misalnya, di dalam metode yang ditimpa), fungsi apa yang harus digunakan?**
    *   **Jawaban**: Fungsi `super()`. Contoh: `super().method_name()`.

---

### 4. Apa Itu Polimorfisme dan Bagaimana Polimorfisme Mendorong Penggunaan Kembali Kode?

**Polimorfisme** (*polymorphism*, yang berarti "banyak bentuk") adalah prinsip OOP yang memungkinkan objek dari kelas yang berbeda untuk diperlakukan sebagai objek dari kelas yang sama atau umum melalui antarmuka yang seragam. Ini berarti metode dengan nama yang sama dapat memiliki implementasi yang berbeda di berbagai kelas, dan Python akan secara otomatis memanggil implementasi yang benar berdasarkan jenis objek.

**Inti dari polimorfisme adalah**: Panggil metode yang sama pada objek yang berbeda, dan setiap objek akan merespons dengan caranya sendiri.

#### Sintaks Dasar (Polimorfisme Tanpa Pewarisan Eksplisit)

Python secara inheren mendukung polimorfisme melalui *duck typing* (jika ia berjalan seperti bebek dan bersuara seperti bebek, maka itu adalah bebek). Artinya, selama objek memiliki metode yang diperlukan, kita bisa memanggilnya tanpa peduli jenis kelasnya.

```python
# Kelas-kelas yang berbeda, masing-masing dengan metode 'speak()'
class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet! Tweet!"

class Monkey:
    def speak(self):
        return "Ooh ooh aah aah!"

# Fungsi yang menerima objek dari kelas manapun yang memiliki metode 'speak()'
def animal_sound(animal):
    print(animal.speak())

# Membuat objek dari kelas-kelas yang berbeda
cat = Cat()
bird = Bird()
monkey = Monkey()

# Memanggil fungsi 'animal_sound' dengan objek berjenis berbeda
animal_sound(cat)      # Output: Meow!
animal_sound(bird)     # Output: Tweet! Tweet!
animal_sound(monkey)   # Output: Ooh ooh aah aah!
```
Dalam contoh ini, fungsi `animal_sound()` tidak peduli apakah `animal` adalah `Cat`, `Bird`, atau `Monkey`. Yang penting adalah objek tersebut memiliki metode `speak()`. Inilah esensi polimorfisme di Python.

#### Contoh dengan Platform Media Sosial

```python
class Twitter:
    def __init__(self, content):
        self.content = content
    def post(self):
        return f"🐦 Tweet: '{self.content}' (Maks. 280 karakter)"

class Instagram:
    def __init__(self, content):
        self.content = content
    def post(self):
        return f"📸 Instagram Post: '{self.content}' + ✨ filters"

class LinkedIn:
    def __init__(self, content):
        self.content = content
    def post(self):
        return f"💼 Artikel LinkedIn: '{self.content}' (Mode Profesional)"

def start_social_media_app(social_media_platform):
    """Fungsi umum untuk 'memposting' di berbagai platform media sosial."""
    print(social_media_platform.post())

tweet = Twitter('Baru belajar Polimorfisme Python!')
photo = Instagram('Indahnya sunset 🌅')
article = LinkedIn('Mengapa OOP Penting di Tahun 2024')

start_social_media_app(tweet)   # Output: 🐦 Tweet: 'Baru belajar Polimorfisme Python!' (Maks. 280 karakter)
start_social_media_app(photo)   # Output: 📸 Instagram Post: 'Indahnya sunset 🌅' + ✨ filters
start_social_media_app(article) # Output: 💼 Artikel LinkedIn: 'Mengapa OOP Penting di Tahun 2024'
```
Fungsi `start_social_media_app` menunjukkan polimorfisme: ia dapat bekerja dengan objek dari berbagai kelas (`Twitter`, `Instagram`, `LinkedIn`) asalkan mereka memiliki metode `post()`.

#### Polimorfisme Berbasis Pewarisan

Polimorfisme seringkali diterapkan bersamaan dengan pewarisan. Dalam skenario ini, kelas induk mendefinisikan sebuah metode (bisa berupa metode abstrak atau dengan implementasi dasar), dan kelas-kelas anak menimpa (*override*) metode tersebut untuk menyediakan implementasi spesifiknya.

```python
class Animal:
    def speak(self):
        return 'Some generic animal sound' # Implementasi dasar

class Cat(Animal): # Cat IS A Animal
    def speak(self): # Menimpa metode speak()
        return 'A cat meows'

class Dog(Animal): # Dog IS A Animal
    def speak(self): # Menimpa metode speak()
        return 'A dog barks woof woof'

class Monkey(Animal): # Monkey IS A Animal
    def speak(self): # Menimpa metode speak()
        return 'A monkey ooh ooh aah aah ooh ooh aah aah'

# Membuat objek dari berbagai kelas anak dan induk
animals = [Cat(), Dog(), Monkey(), Animal()]

# Melakukan iterasi dan memanggil metode speak() pada setiap objek
print("--- Suara berbagai hewan ---")
for animal in animals:
    print(animal.speak())

# Output:
# --- Suara berbagai hewan ---
# A cat meows
# A dog barks woof woof
# A monkey ooh ooh aah aah ooh ooh aah aah
# Some generic animal sound
```
Di sini, semua objek (`Cat`, `Dog`, `Monkey`, `Animal`) di dalam *list* `animals` diperlakukan sebagai `Animal`, tetapi ketika `speak()` dipanggil, implementasi yang sesuai dengan jenis objeknya akan dieksekusi. Ini adalah contoh kuat dari polimorfisme berbasis pewarisan, yang meningkatkan fleksibilitas dan ekstensibilitas kode.

---

#### Pertanyaan Seputar Polimorfisme

1.  **Apa itu polimorfisme dalam konteks Pemrograman Berorientasi Objek?**
    *   **Jawaban**: Prinsip di mana objek dari kelas yang berbeda dapat merespons panggilan metode yang sama dengan perilaku yang berbeda, berdasarkan implementasi spesifik di kelasnya masing-masing.

2.  **Bagaimana Polimorfisme berbasis pewarisan bekerja?**
    *   **Jawaban**: Kelas induk mendefinisikan sebuah metode, dan kelas-kelas anak kemudian menimpa metode tersebut dengan implementasi spesifik mereka sendiri. Saat metode dipanggil pada objek anak, implementasi anak yang relevan akan dieksekusi.

3.  **Apa manfaat utama dari penggunaan polimorfisme dalam desain perangkat lunak?**
    *   **Jawaban**: Meningkatkan fleksibilitas, ekstensibilitas, dan penggunaan kembali kode. Kode dapat ditulis untuk bekerja dengan antarmuka umum, dan dapat dengan mudah diperluas untuk mendukung jenis objek baru tanpa mengubah kode yang sudah ada.

---

### 5. Apa Itu Name Mangling dan Bagaimana Cara Kerjanya?

Seperti yang sudah dibahas di bagian Enkapsulasi, atribut atau metode yang diawali dengan satu garis bawah (`_`) hanyalah **konvensi** untuk menunjuk penggunaan internal. Atribut ini tetap dapat diakses dan diubah secara langsung dari luar kelas.

Namun, atribut atau metode yang diawali dengan **dua garis bawah (`__`)** bekerja secara berbeda di Python. Ini memicu mekanisme yang disebut **name mangling**.

**Name mangling** adalah proses di mana interpreter Python secara otomatis mengubah nama atribut atau metode yang diawali dengan **dua garis bawah (`__`)** (dan tidak diakhiri dengan dua garis bawah, misal `__init__`) menjadi format `_ClassName__attributeName`. Ini dilakukan untuk:
*   Secara efektif membuat atribut/metode tersebut "semi-privat" atau "dilindungi" dari akses langsung dari luar kelas.
*   Mencegah konflik penamaan atau penimpaan yang tidak disengaja dalam hierarki pewarisan.

**Demonstrasi `_` vs `__` dan Name Mangling:**

```python
class Example:
    def __init__(self):
        self._internal_attribute = 'Saya atribut internal (konvensi).'
        self.__mangled_attribute = 'Saya atribut mangled (semi-privat).'

obj = Example()

# Mengakses atribut dengan satu garis bawah (konvensi) - bisa diakses
print("Akses _internal_attribute:", obj._internal_attribute)
# Output: Akses _internal_attribute: Saya atribut internal (konvensi).

# Mencoba mengakses atribut dengan dua garis bawah secara langsung - akan gagal
try:
    print("Akses __mangled_attribute:", obj.__mangled_attribute)
except AttributeError as e:
    print(f"Error saat mengakses __mangled_attribute: {e}")
    # Output: Error saat mengakses __mangled_attribute: 'Example' object has no attribute '__mangled_attribute'
```
AttributeError terjadi karena nama `__mangled_attribute` telah diubah secara internal oleh Python.

**Melihat Nama yang Dimangled Menggunakan `__dict__`:**
Setiap objek Python memiliki atribut `__dict__` yang menyimpan kamus (dictionary) dari atribut-atributnya. Kita bisa melihat bagaimana nama `__mangled_attribute` diubah:

```python
class Example:
    def __init__(self, internal_val, private_val):
        self._internal = internal_val
        self.__private = private_val

example1 = Example(
    'Ini adalah atribut internal dengan satu garis bawah.',
    'Ini adalah atribut "privat" dengan dua garis bawah.'
)

print(example1.__dict__)
# Output:
# {
#   '_internal': 'Ini adalah atribut internal dengan satu garis bawah.',
#   '_Example__private': 'Ini adalah atribut "privat" dengan dua garis bawah.'
# }
```
Dapat dilihat bahwa `__private` telah diubah menjadi `_Example__private`. Walaupun ini "semi-privat", Anda masih bisa mengaksesnya jika Anda tahu nama yang dimangled:

```python
print(example1._Example__private)
# Output: Ini adalah atribut "privat" dengan dua garis bawah.
```
Namun, melakukan ini sangat tidak disarankan karena melanggar tujuan enkapsulasi dan dapat menyebabkan kode yang sulit dipelihara.

#### Tujuan Name Mangling

Tujuan utama name mangling adalah untuk **mencegah penimpaan atribut atau metode secara tidak sengaja** ketika menggunakan pewarisan, terutama dalam kasus pewarisan berganda.

**Contoh: Mencegah Konflik dalam Pewarisan (dengan Name Mangling):**

```python
class Parent:
    def __init__(self):
        self.__secret_data = 'Data Rahasia Induk'

    def get_secret(self):
        return self.__secret_data # Akses menggunakan nama asli di dalam kelas

class Child(Parent):
    def __init__(self):
        super().__init__() # Pastikan konstruktor induk dipanggil
        self.__secret_data = 'Data Rahasia Anak' # Atribut ini dimangled secara terpisah

    def get_child_secret(self):
        return self.__secret_data

c = Child()
print("Data rahasia induk (melalui induk):", c.get_secret())      # Output: Data Rahasia Induk
print("Data rahasia anak (melalui anak):", c.get_child_secret()) # Output: Data Rahasia Anak
print(c.__dict__)
# Output:
# {'_Parent__secret_data': 'Data Rahasia Induk', '_Child__secret_data': 'Data Rahasia Anak'}
```
Dengan name mangling, `__secret_data` di `Parent` dan `__secret_data` di `Child` menjadi dua atribut yang berbeda (`_Parent__secret_data` dan `_Child__secret_data`) dalam objek `Child`. Ini mencegah `Child` secara tidak sengaja menimpa `_Parent__secret_data` milik `Parent`.

**Contoh: Konflik Tanpa Name Mangling (`_` atau tanpa awalan):**

```python
class Parent:
    def __init__(self):
        self._data = 'Data Induk' # Menggunakan satu garis bawah

class Child2(Parent):
    def __init__(self):
        super().__init__()
        self._data = 'Data Anak' # Ini akan menimpa _data dari Parent

c2 = Child2()
print(c2.__dict__)
# Output: {'_data': 'Data Anak'}
# Atribut _data milik Parent telah sepenuhnya digantikan oleh _data milik Child.
```
Pada contoh ini, atribut `_data` milik `Parent` ditimpa habis oleh `Child2`. Ini mungkin bukan perilaku yang diinginkan jika `Parent` menggunakan `_data` secara internal dan mengharapkannya tidak berubah.

#### Kapan Menggunakan `_` vs `__`?

*   **Satu garis bawah (`_`)**: Digunakan untuk atribut atau metode yang dimaksudkan sebagai **internal dan non-publik**, tetapi Anda tidak terlalu khawatir tentang penimpaan oleh kelas anak (atau Anda sengaja ingin anak dapat menimpa). Ini adalah konvensi bagi pengembang lain untuk tidak mengutak-atiknya secara langsung.
*   **Dua garis bawah (`__`)**: Digunakan ketika Anda membuat kelas yang mungkin akan diwarisi, dan Anda ingin **mencegah atribut/metode penting** agar tidak secara eksplisit diakses dari luar kelas atau ditimpa secara tidak sengaja oleh kelas anak. Ini memberikan tingkat perlindungan yang lebih kuat melalui name mangling.

---

#### Pertanyaan Seputar Name Mangling

1.  **Apa perbedaan mendasar antara awalan satu garis bawah (`_`) dan dua garis bawah (`__`) pada atribut kelas di Python?**
    *   **Jawaban**: Satu garis bawah adalah konvensi untuk atribut internal, tanpa memblokir akses langsung. Dua garis bawah memicu name mangling yang mengubah nama atribut, secara efektif membuatnya "semi-privat" dan sangat sulit diakses langsung dari luar.

2.  **Jelaskan apa itu name mangling dan bagaimana ia mengubah nama atribut/metode?**
    *   **Jawaban**: Name mangling adalah proses Python secara otomatis mengubah nama atribut/metode `__nama_asli` menjadi `_ClassName__nama_asli` untuk instance kelas.

3.  **Apa tujuan utama dari name mangling dalam konteks pewarisan?**
    *   **Jawaban**: Untuk mencegah atriburt/metode dari kelas induk ditimpa secara tidak sengaja oleh atribut/metode dengan nama yang sama di kelas anak, sehingga menghindari konflik penamaan dan menjaga integritas internal kelas.

---

### 6. Apa Itu Abstraksi dan Bagaimana Abstraksi Membantu Menjaga Sistem Kompleks Tetap Terorganisir?

Setelah membahas enkapsulasi, pewarisan, dan polimorfisme, mari kita selidiki pilar keempat OOP: **abstraksi**.

**Abstraksi** adalah proses menyederhanakan representasi sistem yang kompleks dengan menyembunyikan detail implementasi yang tidak relevan dan hanya menampilkan fitur-fitur esensial atau perilaku kunci yang diperlukan. Ini memungkinkan kita untuk fokus pada *apa* yang dilakukan sesuatu, bukan *bagaimana* ia melakukannya. Abstraksi membantu dalam mengelola kompleksitas dan merancang sistem agar lebih modular dan mudah dipahami.

**Analogi Mobil**: Saat Anda mengemudikan mobil, Anda menggunakan antarmuka yang disederhanakan seperti setir, pedal gas, dan rem. Anda tidak perlu memahami detail rumit bagaimana mesin membakar bahan bakar, bagaimana transmisi mengubah gigi, atau mekanik sistem pengereman. Ini adalah bentuk abstraksi: Anda berinteraksi dengan mobil melalui antarmuka yang relevan dengan tujuan Anda (mengemudi), sementara detail internal yang kompleks disembunyikan.

Dalam OOP di Python, abstraksi sering diimplementasikan menggunakan **Kelas Abstrak (Abstract Base Classes - ABCs)**.

#### Implementasi Abstraksi di Python: Modul `abc`

Python menyediakan modul bawaan `abc` untuk membuat kelas abstrak. Modul ini menawarkan:
*   **`ABC`**: Sebuah meta-kelas yang berfungsi sebagai dasar untuk mendefinisikan kelas abstrak.
*   **`@abstractmethod`**: Dekorator yang menandai sebuah metode sebagai metode abstrak.

**Aturan untuk Kelas Abstrak:**
1.  **Kelas Abstrak tidak dapat diinstansiasi secara langsung.** Anda tidak bisa membuat objek dari kelas yang memiliki setidaknya satu metode abstrak yang belum diimplementasikan.
2.  **Kelas Turunan (Concrete Subclass) harus mengimplementasikan semua metode abstrak** dari kelas induk abstraknya. Jika tidak, kelas turunan tersebut juga akan dianggap abstrak dan tidak dapat diinstansiasi.
3.  Tujuan utama adalah **mendefinisikan sebuah kontrak** atau antarmuka umum yang harus diikuti oleh semua kelas turunan.

**Sintaks Dasar Kelas Abstrak:**

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC): # Kelas Abstrak mewarisi dari ABC
    @abstractmethod      # Dekorator untuk menandai metode ini sebagai abstrak
    def abstract_method(self):
        """Metode abstrak yang harus diimplementasikan oleh subkelas."""
        pass # Biasanya tidak ada implementasi di sini

    def concrete_method(self):
        """Metode konkret yang memiliki implementasi."""
        print("Ini adalah metode konkret di kelas abstrak.")

# Contoh subkelas konkret yang mengimplementasikan metode abstrak
class ConcreteClassOne(AbstractClass):
    def abstract_method(self): # Implementasi wajib dari 'abstract_method'
        print('Implementasi di ConcreteClassOne')

# Contoh subkelas lain
class ConcreteClassTwo(AbstractClass):
    def abstract_method(self): # Implementasi wajib dari 'abstract_method'
        print('Implementasi di ConcreteClassTwo')

# Membuat objek dari kelas konkret
obj1 = ConcreteClassOne()
obj1.abstract_method()   # Output: Implementasi di ConcreteClassOne
obj1.concrete_method()   # Output: Ini adalah metode konkret di kelas abstrak.

obj2 = ConcreteClassTwo()
obj2.abstract_method()   # Output: Implementasi di ConcreteClassTwo

# Akan menghasilkan TypeError karena AbstractClass tidak bisa diinstansiasi
# abstract_obj = AbstractClass()
# Output: TypeError: Can't instantiate abstract class AbstractClass with abstract method abstract_method
```

**Contoh Abstraksi dengan Hewan dan Suara:**

```python
from abc import ABC, abstractmethod

class Animal(ABC): # Kelas dasar abstrak
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        """Metode abstrak: Setiap hewan harus membuat suara."""
        pass

    def description(self):
        """Metode konkret: Deskripsi umum untuk semua hewan."""
        return f"Saya adalah {self.name}, seekor hewan."

class Dog(Animal):
    def make_sound(self): # Mengimplementasikan metode abstrak
        print('Woof! Woof!')

class Cat(Animal):
    def make_sound(self): # Mengimplementasikan metode abstrak
        print('Meow! Meow!')

class Duck(Animal):
    def make_sound(self): # Mengimplementasikan metode abstrak
        print('Quack! Quack!')

# Membuat objek-objek hewan
my_dog = Dog('Buddy')
my_cat = Cat('Whiskers')
my_duck = Duck('Donald')

animals = [my_dog, my_cat, my_duck]

for animal in animals:
    print(animal.description()) # Memanggil metode konkret diwarisi
    animal.make_sound()         # Memanggil metode abstrak yang diimplementasikan

# Output:
# Saya adalah Buddy, seekor hewan.
# Woof! Woof!
# Saya adalah Whiskers, seekor hewan.
# Meow! Meow!
# Saya adalah Donald, seekor hewan.
# Quack! Quack!
```
Kelas `Animal` mendefinisikan bahwa setiap hewan harus memiliki cara untuk `make_sound()`, tetapi tidak mendikte bagaimana suara itu dibuat. Setiap subkelas (`Dog`, `Cat`, `Duck`) kemudian menyediakan implementasi konkretnya sendiri untuk `make_sound()`. Ini memastikan bahwa setiap objek `Animal` (atau turunannya) akan memiliki kemampuan `make_sound()`, memungkinkan kita untuk menulis kode yang lebih umum dan fleksibel.

**Contoh Abstraksi dengan Mainan yang Bisa Berbicara:**

```python
from abc import ABC, abstractmethod

class TalkingToy(ABC): # Kelas dasar abstrak untuk semua mainan berbicara
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        """Metode abstrak: Setiap TalkingToy harus bisa berbicara."""
        pass

    def introduce(self):
        """Metode konkret: Perkenalan umum untuk semua TalkingToy."""
        return f"Halo, saya {self.name}!"

class RobotToy(TalkingToy):
    def speak(self): # Implementasi spesifik RobotToy
        print(f'{self.name} says beep boop! Saya robot!')

class TeddyBearToy(TalkingToy):
    def speak(self): # Implementasi spesifik TeddyBearToy
        print(f"{self.name} says peluk saya! Saya lucu!")

class DinosaurToy(TalkingToy):
    def speak(self): # Implementasi spesifik DinosaurToy
        print(f'{self.name} says ROOOOAR!')

rusty = RobotToy('Rusty')
fluffy = TeddyBearToy('Fluffy')
rex = DinosaurToy('Rex')

# Iterasi pada berbagai jenis TalkingToy
print("--- Mainan Berbicara ---")
for toy in [rusty, fluffy, rex]:
    print(toy.introduce()) # Memanggil metode konkret
    toy.speak()            # Memanggil metode abstrak yang diimplementasikan
    print("-" * 20)

# Output:
# --- Mainan Berbicara ---
# Halo, saya Rusty!
# Rusty says beep boop! Saya robot!
# --------------------
# Halo, saya Fluffy!
# Fluffy says peluk saya! Saya lucu!
# --------------------
# Halo, saya Rex!
# Rex says ROOOOAR!
# --------------------
```
Dengan Abstraksi, kita mendefinisikan antarmuka `TalkingToy` dengan metode `speak()` yang wajib diimplementasikan. Ini memastikan bahwa semua mainan yang termasuk jenis `TalkingToy` akan memiliki kemampuan berbicara, meskipun cara mereka berbicara sangat berbeda. Ini membantu menjaga sistem tetap terorganisir, fleksibel, dan mudah diperluas.

**Kesimpulan tentang Abstraksi**: Abstraksi adalah alat yang ampuh untuk manajemen kompleksitas. Ini memungkinkan desainer sistem untuk fokus pada antarmuka publik dan perilaku yang *diperlukan* tanpa harus terbebani dengan detail implementasi yang spesifik. Dengan mendefinisikan kelas abstrak dan metode abstrak, kita dapat membuat kontrak yang harus dipenuhi oleh subkelas, mempromosikan desain yang konsisten dan kode yang mudah dipelihara serta diperluas.

---

#### Pertanyaan Seputar Abstraksi

1.  **Apa tujuan utama abstraksi dalam Pemrograman Berorientasi Objek?**
    *   **Jawaban**: Untuk menyembunyikan detail implementasi yang tidak penting dan hanya mengekspos fitur-fitur esensial, menyederhanakan cara interaksi dengan sistem yang kompleks.

2.  **Bagaimana Python mengimplementasikan abstraksi secara formal?**
    *   **Jawaban**: Melalui penggunaan modul `abc` (Abstract Base Classes), yang menyediakan kelas `ABC` dan dekorator `@abstractmethod`.

3.  **Mengapa sebuah kelas abstrak tidak dapat diinstansiasi secara langsung?**
    *   **Jawaban**: Karena ia mungkin memiliki satu atau lebih metode abstrak yang belum diimplementasikan, sehingga ia tidak memiliki perilaku yang lengkap atau konkret. Hanya kelas turunan yang sepenuhnya mengimplementasikan semua metode abstraknya yang dapat diinstansiasi.

---

## Rangkuman Pemrograman Berorientasi Objek (OOP)

**Pemrograman Berorientasi Objek (OOP)** adalah paradigma pemrograman yang mengatur kode di sekitar **objek** (entitas yang menggabungkan data dan fungsi). OOP memiliki empat pilar utama yang sangat penting:

### 1. Enkapsulasi (*Encapsulation*)
*   **Definisi**: Proses membungkus data (atribut) dan kode (metode) yang beroperasi pada data tersebut ke dalam satu unit (kelas).
*   **Tujuan**: Melindungi integritas data, menyembunyikan detail implementasi internal, dan menyediakan antarmuka publik yang terkontrol.
*   **Implementasi di Python**:
    *   **Konvensi (`_` prefix)**: Menunjukkan atribut/metode internal, tidak boleh diakses langsung, tetapi secara teknis masih bisa.
    *   **Name Mangling (`__` prefix)**: Python mengubah nama atribut (`__attribute` menjadi `_ClassName__attribute`), mempersulit akses langsung dari luar kelas dan mencegah penimpaan yang tidak disengaja dalam pewarisan.
    *   **Getter & Setter (@property)**: Metode publik yang menyediakan akses terkontrol ke atribut internal, memungkinkan validasi atau logika komputasi.

### 2. Pewarisan (*Inheritance*)
*   **Definisi**: Mekanisme di mana sebuah kelas baru (kelas anak/subclass) dapat mewarisi atribut dan metode dari kelas yang sudah ada (kelas induk/superclass).
*   **Tujuan**: Mendorong penggunaan kembali kode, membangun hierarki kelas (hubungan "is-a"), dan memungkinkan spesialisasi kelas.
*   **Fitur**:
    *   **Pewarisan Tunggal**: Satu kelas anak mewarisi dari satu kelas induk.
    *   **Pewarisan Berganda**: Satu kelas anak mewarisi dari beberapa kelas induk.
    *   **`super()`**: Digunakan untuk memanggil metode atau konstruktor dari kelas induk.
    *   **Override**: Kelas anak dapat menyediakan implementasi baru untuk metode yang diwarisi.

### 3. Polimorfisme (*Polymorphism*)
*   **Definisi**: Konsep "banyak bentuk", di mana objek dari kelas yang berbeda dapat diperlakukan sebagai objek dari tipe umum melalui antarmuka yang seragam. Metode dengan nama yang sama dapat memiliki implementasi yang berbeda di berbagai kelas.
*   **Tujuan**: Meningkatkan fleksibilitas, ekstensibilitas, dan penggunaan kembali kode. Memungkinkan programmer menulis kode yang bekerja dengan objek dari berbagai jenis asalkan mereka berbagi antarmuka yang sama.
*   **Implementasi di Python**: Didukung secara inheren melalui *duck typing* dan juga dapat terlihat jelas dalam pewarisan saat metode ditimpa.

### 4. Abstraksi (*Abstraction*)
*   **Definisi**: Proses menyembunyikan detail implementasi yang rumit dan hanya menampilkan fitur-fitur penting yang relevan. Fokus pada *apa* yang dilakukan, bukan *bagaimana* ia dilakukan.
*   **Tujuan**: Mengelola kompleksitas, menyederhanakan desain sistem, dan mendefinisikan kontrak yang harus dipenuhi oleh kelas turunan.
*   **Implementasi di Python**: Menggunakan **Abstract Base Classes (ABCs)** dari modul `abc`, dengan kelas-kelas yang mewarisi dari `ABC` dan menggunakan dekorator `@abstractmethod` untuk mendefinisikan metode yang harus diimplementasikan oleh kelas turunan konkret. Kelas abstrak tidak dapat diinstansiasi secara langsung.

**Name Mangling (`__` prefix)**:
*   Sebuah mekanisme Python yang mengubah nama atribut/metode `__nama` menjadi `_ClassName__nama`.
*   Tujuan utamanya adalah mencegah konflik nama atribut/metode yang tidak disengaja dalam hierarki pewarisan. Ini bukan sistem privasi yang ketat seperti di beberapa bahasa lain.

Menguasai keempat pilar OOP ini memungkinkan Anda untuk merancang dan menulis kode Python yang lebih terorganisir, modular, aman, fleksibel, mudah dipelihara, dan dapat diskalakan.