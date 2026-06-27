# Apa Itu Python?

Python adalah bahasa pemrograman serbaguna yang dikenal karena kesederhanaan dan kemudahan penggunaannya. Bahasa ini banyak digunakan di berbagai bidang, seperti ilmu data (data science), pembelajaran mesin (machine learning), pengembangan web, skrip dan otomatisasi, sistem tertanam, Internet of Things (IoT), dan masih banyak lagi.

## Kasus Penggunaan Umum

Python digunakan dalam:
*   Data science
*   Machine learning
*   Pengembangan web
*   Keamanan siber
*   Otomatisasi
*   Proyek mikrokomputer seperti Raspberry Pi dan papan yang kompatibel dengan MicroPython.

## Variabel

### Mendeklarasikan Variabel

Untuk mendeklarasikan variabel, Anda perlu:
1.  Menulis nama variabel.
2.  Mengikuti dengan operator penugasan (`=`).
3.  Diakhiri dengan nilai yang akan disimpan, yang bisa berupa angka, string, boolean, dan lain-lain.

**Contoh:**
```python
name = 'John Doe'
age = 25
```

### Aturan Penamaan Variabel

Berikut adalah aturan-aturan penting yang harus Anda ikuti saat menamai variabel di Python:
*   Nama variabel hanya boleh diawali dengan huruf atau garis bawah (`_`), tidak boleh dengan angka.
*   Nama variabel hanya boleh mengandung karakter alfanumerik (a-z, A-Z, 0-9) dan garis bawah (`_`).
*   Nama variabel bersifat *case-sensitive*. Artinya, `age`, `Age`, dan `AGE` dianggap sebagai variabel yang berbeda.
*   Nama variabel tidak boleh menggunakan kata kunci bawaan Python seperti `if`, `class`, atau `def`.
*   Untuk nama variabel yang terdiri dari beberapa kata, gunakan garis bawah sebagai pemisah (konvensi *snake_case*). Contoh: `nama_pengguna`.

## Komentar

Komentar digunakan untuk memberikan catatan atau penjelasan dalam kode agar lebih mudah dipahami, tanpa memengaruhi jalannya program.

### Komentar Satu Baris

Digunakan untuk catatan singkat. Diawali dengan tanda hash (`#`).
```python
# Ini adalah komentar satu baris
```

### Komentar Multi-baris (Docstrings)

Ini sebenarnya adalah *string* multi-baris yang sering dipakai sebagai dokumentasi (*docstring*) untuk fungsi atau kelas, atau untuk menonaktifkan sementara bagian kode. Diapit oleh tiga tanda kutip ganda (`"""`) atau tiga tanda kutip tunggal (`'''`).
```python
"""
Ini adalah string multi-baris.
Berikut beberapa kode yang dikomentari di dalamnya.

name = 'John Doe'
age = 25
"""
```

### Fungsi `print()`

Untuk menampilkan data ke konsol (layar output), gunakan fungsi `print()`.

**Contoh:**
```python
print('Hello world!')  # Output: Hello world!
```

## Tipe Data Umum di Python

### Pendahuluan

Python adalah bahasa dengan *dynamic typing*, mirip dengan JavaScript. Ini berarti Anda tidak perlu secara eksplisit mendeklarasikan tipe variabel. Python secara otomatis akan mengenali tipe variabel berdasarkan nilai yang diberikan.

Berikut adalah beberapa tipe data umum di Python:

*   **Integer (int)**: Bilangan bulat tanpa desimal.
    ```python
    my_integer_var = 10
    print('Integer:', my_integer_var)  # Output: Integer: 10
    ```

*   **Float (float)**: Bilangan dengan desimal.
    ```python
    my_float_var = 4.50
    print('Float:', my_float_var)  # Output: Float: 4.5
    ```

*   **String (str)**: Urutan karakter yang diapit oleh tanda kutip tunggal (`'`) atau ganda (`"`).
    ```python
    my_string_var = 'hello'
    print('String:', my_string_var)  # Output: String: hello
    ```

*   **Boolean (bool)**: Nilai yang merepresentasikan `True` atau `False`.
    ```python
    my_boolean_var = True
    print('Boolean:', my_boolean_var)  # Output: Boolean: True
    ```

*   **Set (set)**: Koleksi elemen unik yang tidak terurut. Diapit oleh kurung kurawal.
    ```python
    my_set_var = {7, 5, 8}
    print('Set:', my_set_var)  # Output: Set: {8, 5, 7} (Urutan bisa berbeda karena tidak terurut)
    ```

*   **Dictionary (dict)**: Koleksi pasangan kunci-nilai (key-value pairs), diapit oleh kurung kurawal.
    ```python
    my_dictionary_var = {"name": "Alice", "age": 25}
    print('Dictionary:', my_dictionary_var)  # Output: Dictionary: {'name': 'Alice', 'age': 25}
    ```

*   **Tuple (tuple)**: Koleksi terurut yang *tidak dapat diubah* (immutable), diapit oleh tanda kurung.
    ```python
    my_tuple_var = (7, 5, 8)
    print('Tuple:', my_tuple_var)  # Output: Tuple: (7, 5, 8)
    ```

*   **Range (range)**: Urutan angka yang tidak dapat diubah, sering digunakan dalam perulangan (*loop*).
    ```python
    my_range_var = range(5)
    print(my_range_var)  # Output: range(0, 5)
    ```

*   **List (list)**: Koleksi terurut yang *dapat diubah* (mutable) dan dapat menampung berbagai tipe data. Diapit oleh kurung siku.
    ```python
    my_list = [22, 'Hello world', 3.14, True]
    print(my_list)  # Output: [22, 'Hello world', 3.14, True]
    ```

*   **None (NoneType)**: Nilai khusus yang menyatakan ketiadaan nilai (mirip dengan `null` di bahasa lain).
    ```python
    my_none_var = None
    print('None:', my_none_var)  # Output: None: None
    ```

## Tipe Immutable dan Mutable

*   **Tipe Immutable**: Tipe data yang tidak dapat diubah setelah dibuat. Meskipun variabelnya dapat diarahkan ke nilai baru (penugasan ulang), nilai objek aslinya tidak dapat dimodifikasi. Termasuk di dalamnya: `integer`, `float`, `complex`, `boolean`, `string`, `tuple`, `range`, dan `None`.

*   **Tipe Mutable**: Tipe data yang dapat diubah (dimodifikasi) setelah dibuat. Anda bisa menambah, menghapus, atau memperbarui elemen-elemen di dalamnya. Termasuk tipe koleksi: `list`, `set`, dan `dictionary`.

### Fungsi `type()`

Untuk melihat tipe dari suatu variabel, gunakan fungsi bawaan `type()`.
```python
greeting = 'Hello there!'
age = 21
print(type(greeting))  # Output: <class 'str'>
print(type(age))       # Output: <class 'int'>
```

### Fungsi `isinstance()`

Fungsi `isinstance()` digunakan untuk memeriksa apakah sebuah variabel (atau objek) adalah instance dari tipe data tertentu, mengembalikan `True` atau `False`.
```python
greeting = 'Hello world'
name = 'John Doe'
print(isinstance(greeting, str))  # Output: True
print(isinstance(name, int))      # Output: False
```

## Bekerja dengan String

### Definisi

Seperti yang mungkin Anda ingat dari JavaScript, string bersifat *immutable*, yang berarti setelah dibuat, isinya tidak dapat diubah. Di Python, Anda bisa menggunakan tanda kutip tunggal (`'`) maupun ganda (`"`). Disarankan untuk memilih satu gaya dan konsisten menggunakannya.

**Contoh:**
```python
developer = 'Jessica'
city = "Los Angeles"
```

### Mengakses Karakter dari String (Indexing)

Anda dapat mengakses karakter individu dalam string menggunakan notasi kurung siku (`[]`) dengan indeks. Indeks dimulai dari 0 untuk karakter pertama. Indeks negatif menghitung dari akhir string (`-1` adalah karakter terakhir).

```python
my_str = 'Hello world'
print(my_str[0])   # Output: H (Karakter pada indeks 0)
print(my_str[6])   # Output: w (Karakter pada indeks 6)
print(my_str[-1])  # Output: d (Karakter terakhir)
print(my_str[-2])  # Output: l (Karakter kedua dari belakang)
```

### Escaping String

Gunakan garis miring terbalik (`\`) untuk "melarikan diri" (escape) dari tanda kutip yang ingin menjadi bagian dari string, bukan sebagai penutup string.
```python
msg = 'It\'s a sunny day'        # Menggunakan \' untuk tanda kutip tunggal
quote = "She said, \"Hello!\""  # Menggunakan \" untuk tanda kutip ganda
print(msg)   # Output: It's a sunny day
print(quote) # Output: She said, "Hello!"
```

### Penggabungan String (Concatenation)

Anda dapat menggabungkan (menyambung) string menggunakan operator `+`.

**Contoh:**
```python
developer = 'Jessica'
print('My name is ' + developer + '.')  # Output: My name is Jessica.
```

Cara lain adalah dengan operator penugasan gabungan `+=`:
```python
greeting = 'My name is '
developer = 'Jessica.'
greeting += developer # Sama dengan greeting = greeting + developer
print(greeting)       # Output: My name is Jessica.
```

### f-strings (Formatted String Literals)

f-strings (singkatan dari *formatted string literals*) adalah cara yang ringkas dan efisien untuk menyisipkan ekspresi Python ke dalam string. Ini memungkinkan interpolasi dan penggabungan dengan sintaks yang sangat mudah dibaca.

**Contoh:**
```python
developer = 'Jessica'
greeting = f'My name is {developer}.' # String diawali 'f' atau 'F'
print(greeting)                     # Output: My name is Jessica.
```

### String Slicing

String slicing memungkinkan Anda mengekstrak bagian atau "irisan" dari sebuah string. Sintaks dasarnya adalah `str[start:stop:step]`.
*   `start`: Indeks awal (inklusif). Jika dihilangkan, dimulai dari awal string.
*   `stop`: Indeks akhir (eksklusif). Jika dihilangkan, hingga akhir string.
*   `step`: Interval langkah antar karakter. Jika dihilangkan, *default* adalah 1.

**Contoh:**
```python
message = 'Python is fun!'
print(message[0:6])   # Output: Python (dari indeks 0 sampai sebelum 6)
print(message[7:])    # Output: is fun! (dari indeks 7 sampai akhir)
print(message[::2])   # Output: Pto sfn (setiap karakter ke-2 dari awal sampai akhir)
```

### Mendapatkan Panjang String

Gunakan fungsi bawaan `len()` untuk mendapatkan jumlah karakter dalam string.

**Contoh:**
```python
developer = 'Jessica'
print(len(developer))  # Output: 7
```

### Bekerja dengan Operator `in`

Operator `in` mengembalikan nilai boolean (`True` atau `False`) yang menunjukkan apakah sebuah karakter atau substring ada dalam string.

**Contoh:**
```python
my_str = 'Hello world'
print('Hello' in my_str)  # Output: True
print('hey' in my_str)    # Output: False
print('hi' in my_str)     # Output: False
print('e' in my_str)      # Output: True
print('f' in my_str)      # Output: False
```

### Metode String yang Umum

Python menyediakan banyak metode bawaan untuk memanipulasi string. Metode string tidak mengubah string asli karena string bersifat immutable; mereka selalu mengembalikan string baru.

*   `str.upper()`: Mengembalikan salinan string dengan semua karakter diubah menjadi huruf besar.
    ```python
    developer = 'Jessica'
    print(developer.upper())  # Output: JESSICA
    ```

*   `str.lower()`: Mengembalikan salinan string dengan semua karakter diubah menjadi huruf kecil.
    ```python
    print(developer.lower())  # Output: jessica
    ```

*   `str.strip('chars')`: Mengembalikan salinan string dengan karakter tertentu yang ada di awal dan akhir string dihapus. Jika `chars` tidak diberikan, ia akan menghapus spasi putih (spasi, tab, newline).
    ```python
    greeting = '  hello world  '
    trimmed_my_str = greeting.strip()
    print(trimmed_my_str)  # Output: 'hello world'
    ```

*   `str.replace(old, new)`: Mengembalikan string baru dengan semua kemunculan substring `old` diganti dengan substring `new`.
    ```python
    greeting = 'hello world'
    replaced_my_str = greeting.replace('hello', 'hi')
    print(replaced_my_str)  # Output: 'hi world'
    ```

*   `str.split('delimiter')`: Memecah string menjadi daftar (*list*) substring berdasarkan pemisah (*delimiter*) yang ditentukan. Jika tanpa argumen, akan memecah berdasarkan spasi putih.
    ```python
    dashed_name = 'example-dashed-name'
    split_words = dashed_name.split('-')
    print(split_words)  # Output: ['example', 'dashed', 'name']
    ```

*   `'delimiter'.join(iterable)`: Menggabungkan elemen-elemen dari sebuah *iterable* (seperti list atau tuple) menjadi satu string, dipisahkan oleh string *delimiter* yang memanggil metode ini.
    ```python
    example_list = ['example', 'dashed', 'name']
    joined_str = ' '.join(example_list) # Menggabungkan dengan spasi
    print(joined_str)  # Output: example dashed name
    ```

*   `str.startswith(prefix)`: Mengembalikan `True` jika string dimulai dengan awalan (*prefix*) tertentu, `False` jika tidak.
    ```python
    developer = 'Naomi'
    result = developer.startswith('N')
    print(result)  # Output: True
    ```

*   `str.endswith(suffix)`: Mengembalikan `True` jika string diakhiri dengan akhiran (*suffix*) tertentu, `False` jika tidak.
    ```python
    result = developer.endswith('N')
    print(result)  # Output: False
    ```

*   `str.find(substring)`: Mengembalikan indeks kemunculan pertama dari *substring*. Jika substring tidak ditemukan, ia mengembalikan `-1`.
    ```python
    developer = 'Naomi'
    print(developer.find('N'))  # Output: 0
    city = 'Los Angeles'
    print(city.find('New'))     # Output: -1
    ```

*   `str.count(substring)`: Menghitung berapa kali suatu *substring* muncul dalam string.
    ```python
    city = 'Los Angeles'
    print(city.count('e'))  # Output: 2
    ```

*   `str.capitalize()`: Mengembalikan string baru dengan karakter pertama diubah menjadi huruf kapital, dan sisa karakter menjadi huruf kecil.
    ```python
    dessert = 'chocolate cake'
    print(dessert.capitalize())  # Output: Chocolate cake
    ```

*   `str.isupper()`: Mengembalikan `True` jika semua karakter huruf dalam string adalah huruf kapital, `False` jika tidak. Mengabaikan non-huruf.
    ```python
    print(dessert.isupper())  # Output: False
    ```

*   `str.islower()`: Mengembalikan `True` jika semua karakter huruf dalam string adalah huruf kecil, `False` jika tidak. Mengabaikan non-huruf.
    ```python
    print(dessert.islower())  # Output: True
    ```

*   `str.title()`: Mengembalikan string baru dengan huruf pertama setiap kata diubah menjadi huruf kapital.
    ```python
    city = 'los angeles'
    print(city.title())  # Output: Los Angeles
    ```

*   `str.maketrans()` dan `str.translate()`:
    `maketrans()` membuat tabel pemetaan karakter 1-ke-1. `translate()` menggunakan tabel tersebut untuk menerjemahkan karakter dalam string.
    ```python
    # Membuat tabel yang memetakan 'a' ke '1', 'b' ke '2', 'c' ke '3'
    trans_table = str.maketrans('abc', '123')
    print(trans_table)  # Output: {97: 49, 98: 50, 99: 51} (kode ASCII/Unicode)

    result = 'abcabc'.translate(trans_table)
    print(result)  # Output: 123123
    ```

## Operasi Umum pada Integer dan Float

### Operasi Matematika Dasar

Python mendukung operator standar untuk penjumlahan, pengurangan, perkalian, dan pembagian.

```python
int_1 = 56
int_2 = 12
float_1 = 5.4
float_2 = 12.0

print('Integer Addition:', int_1 + int_2)      # Output: 68
print('Float Addition:', float_1 + float_2)    # Output: 17.4
print('Int Subtraction:', int_1 - int_2)       # Output: 44
print('Float Subtraction:', float_2 - float_1) # Output: 6.6
print('Int Multiplication:', int_1 * int_2)    # Output: 672
print('Float Multiplication:', float_2 * float_1) # Output: 64.8 (mungkin sedikit perbedaan floating point)
print('Division (always float):', int_1 / int_2) # Output: 4.666666666666667
print('Float Division:', float_2 / float_1)    # Output: 2.222222222222222
```
**Catatan:** Penjumlahan antara integer dan float akan menghasilkan float.
```python
print(int_1 + float_1)  # Output: 61.4
```

### Operator Modulo (`%`)

Mengembalikan sisa dari operasi pembagian.
```python
print(int_1 % int_2)  # Output: 8 (56 dibagi 12 adalah 4 sisa 8)
```

### Floor Division (`//`)

Melakukan pembagian dan membulatkan hasilnya ke bawah menuju bilangan bulat terdekat (integer).
```python
print(int_1 // int_2)  # Output: 4 (56 dibagi 12 adalah 4.66, dibulatkan ke bawah menjadi 4)
```

### Eksponensiasi (`**`)

Digunakan untuk menghitung pangkat (misalnya, `x ** y` berarti x dipangkatkan y).
```python
int_1 = 4
int_2 = 2
print(int_1 ** int_2)  # Output: 16 (4 pangkat 2)
```

### Fungsi `float()`

Mengonversi nilai lain (integer, string numerik) menjadi `float`.
```python
num = 4
print(float(num))  # Output: 4.0
```

### Fungsi `int()`

Mengonversi nilai lain (float, string numerik, boolean) menjadi `integer`. Pemotongan (truncation) terjadi untuk float (bagian desimal dihilangkan).
```python
num = 4.0
print(int(num))  # Output: 4
```

### Fungsi `round()`

Membulatkan angka ke bilangan bulat terdekat.
```python
num_1 = 3.4
num_2 = 7.7
print(round(num_1))  # Output: 3
print(round(num_2))  # Output: 8
```

### Fungsi `abs()`

Mengembalikan nilai mutlak (absolut) dari sebuah angka.
```python
num = -13
print(abs(num))  # Output: 13
```

### Fungsi `pow(base, exp)`

Mengembalikan `base` dipangkatkan `exp`. Sama dengan operator `**`.
```python
result = pow(2, 3)
print(result)  # Output: 8 (2 pangkat 3)
```

## Penugasan Gabungan (Augmented Assignments)

Penugasan gabungan adalah cara singkat untuk menggabungkan operasi biner (seperti penjumlahan, pengurangan) dengan penugasan (`=`) dalam satu langkah.

```python
# Penjumlahan
my_var = 10
my_var += 5   # Sama dengan my_var = my_var + 5
print(my_var) # Output: 15

# Pengurangan
count = 14
count -= 3    # Sama dengan count = count - 3
print(count)  # Output: 11

# Perkalian
product = 65
product *= 7  # Sama dengan product = product * 7
print(product) # Output: 455

# Pembagian
price = 100
price /= 4    # Sama dengan price = price / 4 (hasilnya float)
print(price)  # Output: 25.0

# Floor division
total_pages = 23
total_pages //= 5 # Sama dengan total_pages = total_pages // 5
print(total_pages) # Output: 4

# Modulo
bits = 35
bits %= 2     # Sama dengan bits = bits % 2
print(bits)   # Output: 1

# Eksponensiasi
power = 2
power **= 3   # Sama dengan power = power ** 3
print(power)  # Output: 8
```
Ada juga operator penugasan gabungan untuk operasi bitwise, seperti `&=`, `|=`, `^=`, `>>=`, dan `<<=`.

## Bekerja dengan Fungsi

### Definisi

Fungsi adalah blok kode yang terorganisir dan dapat digunakan kembali yang dirancang untuk melakukan tugas tunggal, terkait. Fungsi dapat menerima masukan (disebut argumen atau parameter), melakukan serangkaian operasi, dan mengembalikan keluaran. Pemanggilan fungsi dilakukan dengan menulis nama fungsi diikuti tanda kurung `()`.

**Contoh:**
```python
def get_sum(num_1, num_2): # Mendefinisikan fungsi bernama get_sum
    return num_1 + num_2   # Mengembalikan hasil penjumlahan

result = get_sum(3, 4)     # Memanggil fungsi dengan argumen 3 dan 4
print(result)              # Output: 7
```

Jika sebuah fungsi tidak secara eksplisit mengembalikan nilai dengan pernyataan `return`, Python akan secara implisit mengembalikan `None`.
```python
def greet():
    print('hello')

result = greet()  # Output: hello
print(result)     # Output: None
```

Anda bisa memberikan nilai default pada parameter fungsi. Jika argumen untuk parameter tersebut tidak diberikan saat pemanggilan fungsi, nilai default akan digunakan.
```python
def get_sum(num_1, num_2=2): # num_2 memiliki nilai default 2
    return num_1 + num_2

result = get_sum(3)      # Memanggil hanya dengan satu argumen
print(result)            # Output: 5 (3 + 2)
result2 = get_sum(3, 5)  # Memanggil dengan dua argumen, menimpa default
print(result2)           # Output: 8 (3 + 5)
```

Memanggil fungsi tanpa jumlah argumen yang benar (misalnya, terlalu sedikit atau terlalu banyak) akan menghasilkan `TypeError`.
```python
def calculate_sum(a, b):
    print(a + b)

# calculate_sum()  # Ini akan menghasilkan TypeError karena kurang argumen
```

### Fungsi Bawaan yang Umum

*   `input(prompt)`: Meminta masukan dari pengguna melalui konsol. Masukan selalu dikembalikan sebagai string.
    ```python
    name = input('What is your name? ')  # Pengguna mengetik 'Kolade' dan menekan Enter
    print('Hello', name)                 # Output: Hello Kolade
    ```

*   `int(value)`: Mengonversi `value` (angka, boolean, atau string numerik) ke tipe `integer`. Mengalami `ValueError` jika string tidak valid.
    ```python
    print(int(3.14))   # Output: 3 (bagian desimal dipotong)
    print(int('42'))   # Output: 42
    print(int(True))   # Output: 1
    print(int(False))  # Output: 0
    ```

## Lingkup (Scope) di Python

Lingkup menentukan bagian mana dari kode tempat nama (variabel, fungsi, dll.) dapat diakses. Python menggunakan aturan LEGB (Local, Enclosing, Global, Built-in).

*   **Local Scope**: Variabel yang dideklarasikan di dalam sebuah fungsi atau kelas hanya dapat diakses di dalam fungsi/kelas tersebut.
    ```python
    def my_func():
        num = 10  # num adalah variabel lokal
        print(num)

    my_func() # Output: 10
    # print(num) # Ini akan menghasilkan NameError karena num tidak ada di luar my_func
    ```

*   **Enclosing Scope (Nonlocal)**: Fungsi bersarang (fungsi di dalam fungsi lain) dapat mengakses variabel dari fungsi induknya yang terdekat.
    ```python
    def outer_func():
        msg = 'Hello there!' # msg berada di enclosing scope untuk inner_func
        def inner_func():
            print(msg)       # inner_func bisa mengakses msg
        inner_func()

    outer_func() # Output: Hello there!
    ```

*   **Global Scope**: Variabel yang dideklarasikan di luar semua fungsi atau kelas, pada level *module*, dapat diakses di mana saja dalam modul tersebut.
    ```python
    tax = 0.70 # tax adalah variabel global

    def get_total(subtotal):
        # total adalah lokal, subtotal adalah lokal (parameter), tax adalah global
        total = subtotal + (subtotal * tax)
        return total

    print(get_total(100))  # Output: 170.0
    ```

*   **Built-in Scope**: Lingkup ini berisi semua nama bawaan Python (fungsi, modul, kata kunci, objek) yang selalu tersedia.
    ```python
    print(str(45))              # str adalah fungsi built-in
    print(type(3.14))           # type adalah fungsi built-in
    print(isinstance(3, str))   # isinstance adalah fungsi built-in
    ```

## Operator Perbandingan

Operator perbandingan digunakan untuk membandingkan dua nilai dan selalu mengembalikan nilai boolean (`True` atau `False`).

*   Sama dengan (`==`): Menguji apakah dua nilai sama.
    ```python
    print(3 == 4)  # Output: False
    ```

*   Tidak sama dengan (`!=`): Menguji apakah dua nilai tidak sama.
    ```python
    print(3 != 4)  # Output: True
    ```

*   Lebih besar dari (`>`): Menguji apakah nilai kiri lebih besar dari nilai kanan.
    ```python
    print(3 > 4)  # Output: False
    ```

*   Lebih kecil dari (`<`): Menguji apakah nilai kiri lebih kecil dari nilai kanan.
    ```python
    print(3 < 4)  # Output: True
    ```

*   Lebih besar atau sama dengan (`>=`): Menguji apakah nilai kiri lebih besar atau sama dengan nilai kanan.
    ```python
    print(3 >= 4)  # Output: False
    ```

*   Lebih kecil atau sama dengan (`<=`): Menguji apakah nilai kiri lebih kecil atau sama dengan nilai kanan.
    ```python
    print(3 <= 4)  # Output: True
    ```

## Percabangan: `if`, `elif`, dan `else`

Pernyataan kondisional memungkinkan eksekusi kode yang berbeda berdasarkan apakah suatu kondisi `True` atau `False`.

*   **`if`**: Blok kode di bawah `if` akan dijalankan jika kondisi yang mengikutinya adalah `True`.
    ```python
    age = 18
    if age >= 18:
        print('You are an adult')  # Output: You are an adult
    ```

*   **`elif` (else if)**: Diperiksa jika semua kondisi `if` atau `elif` sebelumnya adalah `False`. Anda bisa memiliki satu atau lebih `elif`.
    ```python
    age = 16
    if age >= 18:
        print('You are an adult')
    elif age >= 13: # Kondisi ini dicek karena if di atas False
        print('You are a teenager')  # Output: You are a teenager
    ```

*   **`else`**: Blok kode di bawah `else` akan dijalankan jika tidak ada kondisi `if` atau `elif` sebelumnya yang `True`. Hanya boleh ada satu `else` di akhir rantai kondisional.
    ```python
    age = 12
    if age >= 18:
        print('You are an adult')
    elif age >= 13:
        print('You are a teenager')
    else: # Kondisi ini dieksekusi karena semua di atas False
        print('You are a child')  # Output: You are a child
    ```

*   **Percabangan Bersarang**: Anda dapat menempatkan (menumpuk) pernyataan kondisional di dalam pernyataan kondisional lainnya.
    ```python
    is_citizen = True
    age = 25
    if is_citizen:
        if age >= 18: # Ini adalah if bersarang
            print('You are eligible to vote') # Output: You are eligible to vote
    else:
        print('You are not eligible to vote')
    ```

## Nilai Truthy dan Falsy

### Definisi
Di Python, setiap nilai memiliki nilai kebenaran bawaan (`True` atau `False`) saat dievaluasi dalam konteks Boolean (misalnya, dalam pernyataan `if` atau dengan operator `and`, `or`).
*   **Nilai Falsy**: Nilai-nilai yang secara konseptual dianggap "kosong" atau "tidak ada", dan akan dievaluasi sebagai `False` dalam konteks Boolean. Ini termasuk:
    *   `None`
    *   `False`
    *   Angka nol (`0`, `0.0`, `0j` untuk complex numbers)
    *   String kosong (`''`, `""`)
    *   Koleksi kosong (list kosong `[]`, tuple kosong `()`, dictionary kosong `{}`, set kosong `set()`)
*   **Nilai Truthy**: Semua nilai lain selain yang disebut di atas dianggap *truthy*, dan akan dievaluasi sebagai `True` dalam konteks Boolean.

### Fungsi `bool()`
Anda dapat menggunakan fungsi bawaan `bool()` untuk secara eksplisit memeriksa nilai kebenaran dari sebuah ekspresi atau variabel.

```python
print(bool(False))   # Output: False
print(bool(0))       # Output: False
print(bool(''))      # Output: False
print(bool([]))      # Output: False (list kosong)
print(bool(None))    # Output: False

print(bool(True))    # Output: True
print(bool(1))       # Output: True
print(bool('Hello')) # Output: True
print(bool([1, 2]))  # Output: True (list tidak kosong)
```

## Operator Boolean dan Short-circuiting

Operator Boolean digunakan untuk menggabungkan dua atau lebih ekspresi Boolean atau membalikkan nilai Boolean. Ada tiga operator utama: `and`, `or`, dan `not`.

*   **Operator `and`**:
    *   Mengembalikan `True` jika **kedua** operan adalah `True`.
    *   Jika operan pertama `False`, ia akan mengembalikan operan pertama dan tidak mengevaluasi operan kedua (*short-circuiting*).
    *   Jika operan pertama `True`, ia akan mengembalikan operan kedua.
    *   Secara umum, ia mengembalikan operan *falsy* pertama yang ditemui, atau operan terakhir jika semuanya *truthy*.

    ```python
    is_citizen = True
    age = 25
    print(is_citizen and age) # Output: 25 (age adalah operan kedua dan truthy)

    if is_citizen and age >= 18: # Kedua kondisi True
        print('You are eligible to vote') # Output: You are eligible to vote

    print(False and age) # Output: False (operan pertama falsy)
    print(0 and 'hello') # Output: 0 (operan pertama falsy)
    ```

*   **Operator `or`**:
    *   Mengembalikan `True` jika **salah satu dari** operan adalah `True`.
    *   Jika operan pertama `True`, ia akan mengembalikan operan pertama dan tidak mengevaluasi operan kedua (*short-circuiting*).
    *   Jika operan pertama `False`, ia akan mengembalikan operan kedua.
    *   Secara umum, ia mengembalikan operan *truthy* pertama yang ditemui, atau operan terakhir jika semuanya *falsy*.

    ```python
    age = 19
    is_employed = False
    print(age or is_employed) # Output: 19 (age adalah operan pertama dan truthy)

    is_student = True # Misal variabel ini ada
    if age < 18 or is_student: # age < 18 adalah False, tapi is_student adalah True
        print('You are eligible for a student discount') # Output: You are eligible for a student discount

    print(False or 0) # Output: 0 (operan terakhir karena keduanya falsy)
    print(False or age) # Output: 19 (age adalah operan kedua dan truthy)
    ```

*   **Short-circuiting**: Python mengevaluasi ekspresi Boolean dari kiri ke kanan. Ia berhenti begitu hasil akhir dapat ditentukan tanpa perlu mengevaluasi sisa ekspresi. Ini dapat mencegah kesalahan atau menghemat waktu eksekusi.

*   **Operator `not`**:
    *   Membalik nilai kebenaran dari sebuah operan. Jika operan *truthy*, `not` mengembalikan `False`. Jika operan *falsy*, `not` mengembalikan `True`.
    *   Selalu mengembalikan `True` atau `False`.

    ```python
    print(not '')      # Output: True (karena '' adalah falsy)
    print(not 'Hello') # Output: False (karena 'Hello' adalah truthy)
    print(not 0)       # Output: True (karena 0 adalah falsy)
    print(not 1)       # Output: False (karena 1 adalah truthy)
    print(not False)   # Output: True
    print(not True)    # Output: False
    ```

**Contoh `not` dalam percabangan:**
```python
is_admin = False
if not is_admin: # Kondisi ini True karena is_admin adalah False
    print('Access denied for non-administrators.') # Output: Access denied for non-administrators.
else:
    print('Welcome, Administrator!')