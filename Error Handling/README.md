## 1. Pesan Error Umum dalam Python

Saat menulis kode Python, sangat wajar jika menemui *error*. Memahami pesan-pesan *error* ini adalah kunci untuk melakukan *debugging* dengan cepat dan efisien. Pesan *error* memberitahu Anda secara persis apa yang salah, asalkan Anda tahu cara membacanya.

Beberapa *error* Python yang umum meliputi `SyntaxError`, `NameError`, `TypeError`, `IndexError`, dan `AttributeError`. *Error-error* ini muncul ketika Python tidak memahami kode Anda, atau ketika logika program tidak cocok dengan data yang sedang diproses.

### `SyntaxError`
`SyntaxError` terjadi saat kode Anda tidak mengikuti aturan sintaks Python.

```python
print("Hello, world!"
# Output:
#   File "<stdin>", line 1
#     print("Hello, world!"
#                         ^
# SyntaxError: unexpected EOF while parsing
```
Baris di atas kehilangan tanda kurung tutup. Python melemparkan `SyntaxError` karena kode tidak mengikuti aturan sintaks yang benar.

### `NameError`
Python melemparkan `NameError` saat Anda mencoba mengakses variabel atau fungsi yang belum didefinisikan.

```python
print(name)
```
```
# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'name' is not defined
```
Di sini, Anda mencoba mencetak variabel `name` yang belum pernah dibuat atau diinisialisasi sebelumnya.

### `TypeError`
`TypeError` terjadi ketika Anda melakukan operasi pada tipe data yang tidak kompatibel.

```python
5 + "5"
```
```
# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
Anda tidak bisa menjumlahkan *integer* dengan *string* secara langsung. Python memberikan `TypeError`.

### `IndexError`
`IndexError` dilempar saat Anda mengakses indeks yang tidak ada di dalam *sequence* (seperti *list*, *tuple*, atau *string*).

```python
my_list = [1, 2, 3]
print(my_list[5])
```
```
# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
```
*List* `my_list` hanya memiliki indeks 0, 1, dan 2. Indeks 5 berada di luar jangkauan yang valid.

### `AttributeError`
`AttributeError` muncul ketika Anda mencoba menggunakan metode atau properti yang tidak dimiliki oleh objek dengan tipe tertentu.

```python
num = 42
num.append(5)
```
```
# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'int' object has no attribute 'append'
```
Objek *integer* (`int`) tidak memiliki metode `append()`. Python memberikan `AttributeError`.

Mengenali pesan *error* Python yang umum akan membantu Anda memperbaiki masalah lebih cepat. Daripada menebak-nebak, bacalah pesan *error* dengan saksama. Pesan itu sering kali memberi tahu dengan tepat apa yang salah dan di mana Anda harus memeriksanya.

---

## 2. Teknik Debugging yang Baik dalam Python

*Debugging* adalah keterampilan esensial bagi setiap pengembang Python. Memahami teknik-teknik dasarnya dapat membantu Anda mengidentifikasi dan memperbaiki masalah secara efisien.

*Debugging* adalah proses mengidentifikasi dan menyelesaikan *error* atau *bug* dalam kode. Proses ini melibatkan pemeriksaan kode, pemahaman alur program, dan penggunaan alat bantu untuk menemukan sumber masalah.

### Menggunakan Fungsi `print()` dan f-string
Memanfaatkan fungsi `print()` dan f-string di berbagai titik dalam kode dapat membantu Anda memahami alur program dan keadaan variabel.

```python
def add(a, b):
    result = a + b
    print(f'Adding {a} and {b} gives {result}') # Pernyataan debug
    return result

add(5, 3)
# Output: Adding 5 and 3 gives 8
```
Dengan mencetak nilai `a`, `b`, dan `result`, Anda dapat memverifikasi bahwa fungsi berperilaku seperti yang diharapkan.

### Debugging Interaktif dengan Modul `pdb`
Python menyediakan modul bawaan `pdb` untuk *debugging* interaktif.

```python
import pdb

def divide(a, b):
    pdb.set_trace() # Menyetel breakpoint
    return a / b

print(divide(10, 2))
```
Dengan memasang *trace* menggunakan fungsi `set_trace()`, Anda dapat mengeksekusi kode baris per baris, memeriksa variabel, dan memahami perilaku program.

Jika Anda menjalankan kode di atas, akan muncul *output* yang menunjukkan lokasi *file*, baris tempat `set_trace()` dipanggil, kode setelahnya, dan *prompt* interaktif `pdb`:

```
> /Users/fcc/Desktop/debugging.py(5)divide()
-> return a / b
(Pdb)
```
Masukkan `help` ke dalam *prompt* untuk melihat daftar perintah yang dapat digunakan:

```
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb
```
Kemudian Anda dapat menggunakan perintah-perintah tersebut untuk melakukan *debug* kode. Contoh, untuk melihat tipe dari suatu elemen pada saat itu, gunakan perintah `whatis`:

```
(Pdb) whatis a
<class 'int'>
(Pdb) whatis divide
Function divide
```
Terlihat bahwa saat `set_trace()` dijalankan, parameter `a` bertipe *integer*, dan `divide` adalah sebuah fungsi.

Untuk melanjutkan eksekusi kode, gunakan perintah `continue` (atau aliasnya `cont` atau `c`):

```
(Pdb) continue
5.0
```

### Alat Debugging di IDE
Banyak *Integrated Development Environment* (IDE) menawarkan alat *debugging* canggih, seperti *breakpoints*, eksekusi langkah per langkah, dan inspeksi variabel.

**Menggunakan Debugger VS Code**

Jika Anda menggunakan VS Code, Anda dapat menetapkan *breakpoints* dan menjalankan *debugger* untuk menghentikan eksekusi di titik tersebut. Berikut langkah-langkah melakukan *debug* fungsi `divide` yang sama:

1.  **Siapkan kode**
    Buat *file* `main.py` dengan konten berikut:

    ```python
    def divide(a, b):
        result = a / b
        return result

    print(divide(10, 2))
    print(divide(15, 3))
    ```

2.  **Tetapkan breakpoint**
    *   Klik pada *gutter* (margin kiri) di samping baris 2 (`result = a / b`) untuk menetapkan *breakpoint*.
    *   Sebuah titik merah akan muncul, menandakan *breakpoint* aktif.

3.  **Mulai debugging**
    *   Tekan `F5` atau pilih **Run > Start Debugging**.
    *   Pilih **Python File** saat diminta.
    *   *Debugger* akan menghentikan eksekusi tepat di *breakpoint*.

4.  **Periksa variabel**
    *   Arahkan kursor ke variabel untuk melihat nilainya saat ini.
    *   Gunakan panel **Variables** di sebelah kiri untuk melihat semua variabel lokal.
    *   Gunakan **Debug Console** di bagian bawah untuk mengevaluasi ekspresi.

5.  **Melangkah melalui kode**
    Gunakan *debug toolbar* untuk:
    *   **Continue (F5)**: melanjutkan eksekusi hingga *breakpoint* berikutnya.
    *   **Step Over (F10)**: mengeksekusi baris saat ini dan pindah ke baris berikutnya.
    *   **Step Into (F11)**: masuk ke dalam pemanggilan fungsi.
    *   **Step Out (Shift+F11)**: keluar dari fungsi yang sedang dijalankan.

Alat *debugging* di IDE menyediakan antarmuka visual untuk memeriksa keadaan program, sehingga lebih mudah mengidentifikasi dan memperbaiki masalah dibandingkan hanya menggunakan pernyataan `print()`.

Dengan menguasai teknik-teknik dasar *debugging* ini (pernyataan `print()`, modul `pdb`, dan alat IDE), Anda dapat mengidentifikasi dan menyelesaikan masalah dalam kode Python secara efektif. Setiap teknik memiliki tempatnya: `print()` untuk pengecekan cepat, `pdb` untuk eksplorasi interaktif, dan *debugger* IDE untuk inspeksi visual.

---

## 3. Bagaimana Exception Handling Bekerja?

*Exception handling* adalah bagian inti dari penulisan program yang tangguh dan tahan terhadap kesalahan. Ia memungkinkan Anda untuk mengantisipasi, menangkap, dan merespons *error* secara terstruktur.

*Exception handling* adalah proses menangkap dan mengelola *error* yang terjadi selama eksekusi program, sehingga kode Anda tidak berhenti tiba-tiba (*crash*).

Python menyediakan blok `try`, `except`, `else`, dan `finally` untuk menangani *error* dengan anggun.

**Contoh dasar:**

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
# Output: You can't divide by zero!
```
*   `try`: Blok kode tempat Anda mengantisipasi kemungkinan terjadinya *error*.
*   `except`: Blok ini dijalankan jika *error* dengan tipe yang ditentukan terjadi di dalam blok `try`.

Dalam contoh ini, pembagian dengan nol menghasilkan `ZeroDivisionError`, yang kemudian ditangkap dan ditangani.

**Contoh dengan `else` dan `finally`:**

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('Division successful:', x)
finally:
    print('This block always runs.')
# Output:
# Division successful: 5.0
# This block always runs.
```
*   `else`: Dijalankan jika **tidak ada *exception*** yang terjadi dalam blok `try`.
*   `finally`: **Selalu dijalankan**, terlepas dari apakah *exception* terjadi atau tidak. Biasa digunakan untuk tugas pembersihan seperti menutup *file* atau melepaskan sumber daya.

**Menangkap beberapa exception**
Anda dapat menangkap beberapa jenis *exception* dengan blok `except` terpisah:

```python
try:
    number = int('abc') # Ini akan memicu ValueError
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")
# Output: That was not a valid number.
```
Dengan klausa `except` yang terpisah, respons terhadap *error* bisa lebih spesifik dan berguna.

**Menggunakan objek *exception***
Anda dapat mengakses objek *exception* itu sendiri, biasanya dengan alias menggunakan kata kunci `as`.

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f'Error occurred: {e}')
# Output: Error occurred: division by zero
```
Menggunakan `e` memungkinkan Anda mengakses pesan *error* asli atau objek *error* untuk pencatatan (**logging**) atau *debugging*.

**Menangkap beberapa *exception* dalam satu blok `except`**
Caranya dengan menuliskan tipe *exception* sebagai *tuple*:

```python
try:
    user_input = input('Enter a number: ')
    number = int(user_input)
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')

# Contoh input: 'abc'
# Output: Error occurred: invalid literal for int() with base 10: 'abc'

# Contoh input: '0'
# Output: Error occurred: division by zero
```
Dengan *exception handling*, program Anda dapat pulih dari *error* secara terkendali. Menggunakan `try`, `except`, `else`, dan `finally` memungkinkan Anda mengantisipasi potensi masalah dan membangun aplikasi yang lebih tangguh.

---

## 4. Pernyataan `raise` dan Cara Kerjanya

Di Python, pernyataan `raise` adalah alat yang kuat untuk memicu *exception* secara manual dalam kode Anda. Ini memberi kendali atas kapan dan bagaimana *error* dihasilkan, memungkinkan Anda membuat kondisi *error* kustom dan menegakkan perilaku program tertentu.

Pernyataan `raise` digunakan untuk secara eksplisit melemparkan *exception* di titik mana pun dalam program, menandakan bahwa kondisi *error* telah terjadi atau persyaratan tertentu belum terpenuhi.

### Penggunaan Dasar
```python
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}')
# Output: Error: Age cannot be negative
```
Kata kunci `raise` memicu *exception* `ValueError` dengan pesan kustom saat usia negatif diberikan.

### Melemparkan Ulang Exception Saat Ini
`raise` tanpa argumen akan melemparkan ulang *exception* yang sedang ditangani. Ini berguna dalam *exception handling*:

```python
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Melemparkan ulang ValueError yang sama

try:
    process_data('abc') # Ini akan memicu ValueError
except ValueError:
    print('Handled at higher level')
# Output:
# Logging: Invalid data received
# Handled at higher level
```
Pola ini memungkinkan Anda mencatat *log* atau melakukan pembersihan sambil tetap menyebarkan *error* ke level yang lebih tinggi.

### Membuat Exception Kustom
Anda bisa membuat kelas *exception* sendiri dengan mewarisi dari `Exception` (atau subkelasnya).

```python
class InsufficientFundsError(Exception):
    """Exception khusus untuk dana tidak mencukupi."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')
# Output: Transaction failed: Insufficient funds: $100 available, $150 requested
```
Kelas *exception* kustom memungkinkan Anda menyertakan logika tambahan dan atribut sendiri.

### Merantai Exception dengan `from`
Pernyataan `raise` bisa dikombinasikan dengan kata kunci `from` untuk merantai *exception*, menunjukkan hubungan antara *error* yang berbeda.

*   `raise ... from None` menyembunyikan konteks *exception* asli, hanya menampilkan *exception* baru.
*   `raise ... from e` merantai *exception* baru ke *exception* asli, mempertahankan jejak *error*.

```python
def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        # Menyembunyikan FileNotFoundError, hanya menampilkan ValueError baru
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        # Merantai ValueError baru dengan e (original ValueError)
        raise ValueError('Invalid configuration format') from e

# Contoh penggunaan dan outputnya:
# 1. config.txt tidak ada
# try:
#     config = parse_config('non_existent.txt')
# except ValueError as e:
#     print(e)
# Output: Configuration file is missing

# 2. config.txt ada tapi isinya tidak valid (misal: 'abc')
try:
    # Buat file config.txt dengan isi 'abc' untuk pengujian
    with open('config.txt', 'w') as f:
        f.write('abc')
    config = parse_config('config.txt')
except ValueError as e:
    print(e)
# Output: Invalid configuration format
```
**Traceback untuk `from None`** (hanya menampilkan *error* baru):
```
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    config = parse_config('config.txt')
  File "main.py", line 7, in parse_config
    raise ValueError('Configuration file is missing') from None
ValueError: Configuration file is missing
```

**Traceback untuk `from e`** (mempertahankan rantai error):
```
Traceback (most recent call last):
  File "main.py", line 5, in parse_config
    return int(data)
ValueError: invalid literal for int() with base 10: ''

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "main.py", line 12, in <module>
    config = parse_config('config.txt')
  File "main.py", line 9, in parse_config
    raise ValueError('Invalid configuration format') from e
ValueError: Invalid configuration format
```

### Menggunakan `assert`
Pernyataan `assert` adalah singkatan untuk melemparkan `AssertionError` jika suatu kondisi tidak terpenuhi.

```python
def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f'Assertion failed: {e}')
# Output: Assertion failed: Cannot calculate square root of negative number
```
`assert` sangat berguna untuk menegakkan aturan bisnis, validasi *input*, atau kondisi yang harus selalu benar selama pengembangan.

Pernyataan `raise` penting untuk membuat aplikasi yang tangguh. Dengan menggunakannya secara strategis, Anda dapat menegakkan aturan bisnis, memvalidasi *input*, dan memberikan pesan *error* yang bermakna, sehingga kode menjadi lebih mudah diprediksi dan di-*debug*, serta memberikan umpan balik yang jelas kepada pengguna.

---

## 5. Review: Penanganan Error, Debugging, dan Exception

### Kesalahan Umum dalam Python
| Error           | Deskripsi                                        | Contoh                                                              |
| :-------------- | :----------------------------------------------- | :------------------------------------------------------------------ |
| `SyntaxError`   | *Error* saat kode melanggar aturan sintaks.      | `print("Hello there"` → `SyntaxError: '(' was never closed`         |
| `NameError`     | Mengakses variabel/fungsi yang belum didefinisikan. | `print(username)` (tanpa definisi) → `NameError: name 'username' is not defined` |
| `TypeError`     | Operasi pada tipe data yang tidak kompatibel.    | `5 + "5"` → `TypeError: can only concatenate str (not "int") to str` |
| `IndexError`    | Mengakses indeks di luar jangkauan *sequence*.   | `greet = "hello world"; print(greet[12])` → `IndexError: string index out of range` |
| `AttributeError`| Memanggil metode/properti yang tidak ada pada objek. | `"hello".append("!")` → `AttributeError: 'str' object has no attribute 'append'` |

### Teknik Debugging yang Baik
*   **Fungsi `print`**: Menyisipkan pernyataan `print()` di berbagai titik untuk melihat nilai variabel dan alur program.
*   **Debugger bawaan (`pdb`)**: Modul `pdb` dari pustaka standar memungkinkan Anda menyetel *trace* dengan `set_trace()` dan berinteraksi secara langsung.
*   **Alat *debugging* IDE**: IDE seperti PyCharm dan VS Code menyediakan fitur *breakpoint*, eksekusi langkah demi langkah, inspeksi variabel, dan lainnya.

### Exception Handling
**`try...except`**
Blok `try` menjalankan kode yang mungkin memunculkan *exception*, `except` menangani tipe *exception* tertentu.
```python
try:
    print(22 / 0)
except ZeroDivisionError:
    print('You can\'t divide by zero!')
# Output: You can't divide by zero!
```
Anda dapat merantai beberapa blok `except`:
```python
try:
    number = int(input('Enter a number: '))
    print(22 / number)
except ZeroDivisionError:
    print('You cannot divide by zero!')
except ValueError:
    print('Please enter a valid number!')

# Contoh input: '0'
# Output: You cannot divide by zero!

# Contoh input: 'abc'
# Output: Please enter a valid number!
```

**`else` dan `finally`**
`else` berjalan jika tidak ada *exception*, `finally` selalu berjalan.
```python
try:
    result = 100 / 4
except ZeroDivisionError:
    print('You cannot divide by zero!')
else:
    print(f'Result is {result}') # Result is 25.0
finally:
    print('Execution complete!') # Execution complete!

# Output:
# Result is 25.0
# Execution complete!
```

**Objek Exception**
Gunakan `as` untuk mengakses *exception*:
```python
try:
    value = int('This will raise an error')
except ValueError as e:
    print(f'Caught an error: {e}')
    # Output: Caught an error: invalid literal for int() with base 10: 'This will raise an error'
```

### Pernyataan `raise`
`raise` memicu *exception* secara manual:
```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('You cannot divide by zero')
    return a / b

try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print(f"Error: {e}")
# Output: Error: You cannot divide by zero
```

### Memberi Sinyal Exception dengan Custom Exception
Membuat *exception* kustom memungkinkan pesan *error* yang lebih spesifik.

```python
class InvalidCredentialsError(Exception):
    """Exception khusus untuk kredensial tidak valid."""
    def __init__(self, message="Invalid username or password"):
        self.message = message
        super().__init__(self.message)

def login(username, password):
    stored_username = "admin"
    stored_password = "password123"

    if username != stored_username or password != stored_password:
        raise InvalidCredentialsError()

    return f"Welcome, {username}!"
```

Contoh pemakaian:
```python
# Percobaan login gagal
try:
    message = login("user", "wrongpassword")
except InvalidCredentialsError as e:
    print(f"Login failed: {e}")
else:
    print(message)
# Output: Login failed: Invalid username or password

# Percobaan login berhasil
try:
    message = login("admin", "password123")
except InvalidCredentialsError as e:
    print(f"Login failed: {e}")
else:
    print(message)
# Output: Welcome, admin!
```
Pada *login* yang gagal, blok `except` menangkap `InvalidCredentialsError` dan mencetak pesan kegagalan. Pada *login* yang berhasil, blok `else` dijalankan karena tidak ada *exception*.

**Rantai Exception dengan `from`**
`raise ... from None` menyembunyikan konteks asli, sementara `raise ... from e` mempertahankan rantai *error*, seperti telah dicontohkan di bagian sebelumnya.