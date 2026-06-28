# Daftar Isi

- [1. Apa Itu Python dan Penggunaan Umumnya di Industri?](#1-apa-itu-python-dan-penggunaan-umumnya-di-industri)
- [2. Cara Mendeklarasikan Variabel dan Konvensi Penamaan](#2-cara-mendeklarasikan-variabel-dan-konvensi-penamaan)
  - [Aturan Penamaan Variabel](#aturan-penamaan-variabel)
  - [Konvensi Penamaan yang Umum](#konvensi-penamaan-yang-umum)
  - [Komentar di Python](#komentar-di-python)
- [3. Bagaimana Fungsi print() Bekerja](#3-bagaimana-fungsi-print-bekerja)
- [4. Tipe Data Umum di Python](#4-tipe-data-umum-di-python)
  - [Daftar Tipe Data yang Paling Umum di Python](#daftar-tipe-data-yang-paling-umum-di-python)
- [5. Fungsi type() dan isinstance()](#5-fungsi-type-dan-isinstance)
  - [Fungsi isinstance()](#fungsi-isinstance)
- [6. String dan Immutabilitas String](#6-string-dan-immutabilitas-string)
  - [Menangani Tanda Kutip di Dalam String](#menangani-tanda-kutip-di-dalam-string)
  - [Operator in untuk String](#operator-in-untuk-string)
  - [Panjang String dan Indeks](#panjang-string-dan-indeks)
  - [Tipe Data Immutable dan Mutable](#tipe-data-immutable-dan-mutable)
- [7. Penggabungan String (*Concatenation*) dan Interpolasi String](#7-penggabungan-string-concatenation-dan-interpolasi-string)
  - [Penggabungan String dengan +](#penggabungan-string-dengan)
  - [Operator Penugasan Gabungan +=](#operator-penugasan-gabungan)
  - [Interpolasi String dengan f-string](#interpolasi-string-dengan-f-string)
- [8. *String Slicing* (Mengiris String)](#8-string-slicing-mengiris-string)
  - [Parameter step (Langkah)](#parameter-step-langkah)
- [9. Metode-Metode String yang Umum](#9-metode-metode-string-yang-umum)
- [10. Bekerja dengan Integer dan Floating Point Numbers](#10-bekerja-dengan-integer-dan-floating-point-numbers)
  - [Operasi Aritmetika Dasar](#operasi-aritmetika-dasar)
  - [Operator Aritmetika Lanjutan](#operator-aritmetika-lanjutan)
  - [Mengapa 0.1 + 0.2 Tidak Tepat 0.3?](#mengapa-01--02-tidak-tepat-03)
  - [Konversi Tipe: int() dan float()](#konversi-tipe-int-dan-float)
  - [Fungsi Numerik Bawaan Lainnya](#fungsi-numerik-bawaan-lainnya)
- [11. *Augmented Assignments* (Penugasan Gabungan)](#11-augmented-assignments-penugasan-gabungan)
  - [Operator *Augmented Assignment*](#operator-augmented-assignment)
  - [*Augmented Assignment* pada String](#augmented-assignment-pada-string)
- [12. Pernyataan Kondisional dan Operator Logika](#12-pernyataan-kondisional-dan-operator-logika)
  - [Operator Perbandingan](#operator-perbandingan)
  - [Pernyataan if](#pernyataan-if)
  - [else dan elif](#else-dan-elif)
  - [if Bersarang (*nested if*)](#if-bersarang-nested-if)
- [13. Nilai *Truthy* dan *Falsy*, Operator Boolean, dan *Short-Circuiting*](#13-nilai-truthy-dan-falsy-operator-boolean-dan-short-circuiting)
  - [Nilai *Truthy* dan *Falsy*](#nilai-truthy-dan-falsy)
  - [Operator Boolean (Logika)](#operator-boolean-logika)
  - [*Short-Circuiting*](#short-circuiting)
- [14. Fungsi di Python](#14-fungsi-di-python)
  - [Fungsi Bawaan yang Berguna](#fungsi-bawaan-yang-berguna)
  - [Mendefinisikan Fungsi Sendiri](#mendefinisikan-fungsi-sendiri)
  - [return](#return)
- [15. Scope (Ruang Lingkup) di Python – Aturan LEGB](#15-scope-ruang-lingkup-di-python--aturan-legb)
  - [Local Scope](#local-scope)
  - [Enclosing Scope](#enclosing-scope)
  - [Global Scope](#global-scope)
  - [Built-in Scope](#built-in-scope)
- [Ringkasan Dasar-Dasar Python](#ringkasan-dasar-dasar-python)
  - [Apa itu Python?](#apa-itu-python)
  - [Variabel](#variabel)
  - [Komentar](#komentar)
  - [Fungsi print()](#fungsi-print)
  - [Tipe Data Umum](#tipe-data-umum)
  - [type() dan isinstance()](#type-dan-isinstance)
  - [String](#string)
    - [Metode String Umum](#metode-string-umum)
    - [Penggabungan dan f-string](#penggabungan-dan-f-string)
    - [String Slicing](#string-slicing)
  - [Integer dan Float](#integer-dan-float)
  - [*Augmented Assignments* (Penugasan Gabungan)](#augmented-assignments-penugasan-gabungan)
  - [Operator Perbandingan](#operator-perbandingan)
  - [Pernyataan Kondisional](#pernyataan-kondisional)
  - [*Truthy*/*Falsy* dan Operator Boolean](#truthyfalsy-dan-operator-boolean)
  - [Fungsi](#fungsi)
  - [Scope (Ruang Lingkup) – Aturan LEGB](#scope-ruang-lingkup--aturan-legb)

---

## 1. Apa Itu Python dan Penggunaan Umumnya di Industri?
Python adalah bahasa pemrograman serbaguna (*general-purpose*) yang dikenal karena kesederhanaan dan kemudahan penggunaannya. Karakteristik ini menjadikannya salah satu bahasa pemrograman paling populer saat ini.

Python banyak digunakan di berbagai bidang, antara lain:
- **Data Science dan Machine Learning**: Python adalah bahasa utama di kalangan *data scientist* dan *machine learning engineer*. Pustaka seperti **Pandas** dan **NumPy** memudahkan analisis data, sementara pustaka seperti **TensorFlow** dan **Scikit-learn** menyederhanakan pengembangan model pembelajaran mesin dan kerja dengan AI.
- **Pengembangan Web**: *Framework* Python seperti **Django**, **FastAPI**, dan **Flask** memungkinkan pengembang membangun sistem *backend* yang skalabel dan aman dengan upaya minimal. Banyak platform media sosial terkenal seperti **Instagram** dan **Pinterest** menggunakan Python di sisi *backend* mereka.
- **Keamanan Siber**: Para profesional keamanan siber dan *ethical hacker* memanfaatkan Python untuk mendeteksi kerentanan terhadap *malware* dan virus, membangun pemindaian keamanan otomatis, dan menganalisis ancaman.
- **Sistem Tertanam dan IoT (Internet of Things)**: Python dapat berjalan dengan baik pada mikrokomputer seperti **Raspberry Pi** dan papan yang kompatibel dengan **MicroPython**. Ini memungkinkan pembuatan berbagai proyek IoT, seperti perangkat rumah pintar, stasiun pemantau cuaca, dan lain-lain.
- **DevOps**: Python sering digunakan untuk menulis skrip CI/CD (Continuous Integration/Continuous Deployment) dan mengelola infrastruktur di seluruh jalur pengembangan. Bahasa ini juga dipakai untuk membangun layanan *backend* dan API internal.
- **Pengujian Perangkat Lunak**: Alat Python seperti **pytest** digunakan untuk membuat rangkaian pengujian yang andal dan otomatis.
- **Administrasi Sistem**: Administrator sistem mengandalkan Python untuk pemantauan server, manajemen log, dan tugas-tugas tingkat sistem lainnya.
- **Otomatisasi**: Salah satu kekuatan terbesar Python adalah kemampuannya dalam otomatisasi. Anda dapat menulis skrip sederhana untuk membantu tugas-tugas berulang, seperti mengekstrak data dari *spreadsheet*, mengirim email, dan bekerja dengan berkas di mesin lokal Anda. Pustaka seperti **Selenium** dan **BeautifulSoup** memudahkan interaksi dengan situs web, sehingga Anda dapat melakukan *web scraping* data publik, mengotomatiskan tugas melalui antarmuka web, bahkan mengelola *deployment* *cloud* untuk proyek Anda.

Seperti yang terlihat, Python adalah bahasa yang sangat kuat, namun mudah dipelajari. Dari skrip otomatisasi sederhana hingga aplikasi skala industri berskala besar, Anda dapat menggunakan Python untuk hampir semua hal. Python adalah pilihan yang tepat bagi siapa pun yang ingin belajar pemrograman, terlepas dari spesialisasi yang akan mereka pilih nanti.

---

## 2. Cara Mendeklarasikan Variabel dan Konvensi Penamaan
Di Python, variabel dapat diibaratkan sebagai kotak berlabel yang digunakan untuk menyimpan dan merujuk data dari berbagai tipe. Untuk mendeklarasikan variabel, Anda cukup menetapkan (*assign*) sebuah nilai ke sebuah pengenal (*identifier*) menggunakan operator penugasan (`=`). Anda **tidak membutuhkan** kata kunci khusus seperti `let` atau `const` di JavaScript, atau `char` di C#.

Di Python, Anda cukup menulis nama variabel di sebelah kiri operator penugasan, diikuti operator penugasan (`=`), dan nilai yang ingin diberikan di sebelah kanan.

**Contoh deklarasi variabel:**
```python
name = 'John Doe'
age = 25
```

Dalam contoh di atas, variabel `name` menyimpan nilai `'John Doe'`. Nilai ini merupakan sebuah **string**, yaitu rangkaian karakter yang digunakan untuk merepresentasikan teks. String ditulis dengan tanda kutip tunggal (`'...')` atau ganda (`"..."`), misalnya `'Hello'` atau `"Hello"`. (Anda akan mempelajari lebih lanjut tentang string di pelajaran mendatang.)

### Aturan Penamaan Variabel
Saat menamai variabel di Python, ada beberapa aturan penting yang harus diingat:
- Nama variabel hanya boleh dimulai dengan huruf (a-z, A-Z) atau garis bawah (`_`). **Tidak boleh** dimulai dengan angka.
- Nama variabel hanya boleh berisi karakter alfanumerik (a-z, A-Z, 0-9) dan garis bawah (`_`).
- Nama variabel **bersifat *case-sensitive*** — `age`, `Age`, dan `AGE` dianggap sebagai tiga variabel yang berbeda.
- Nama variabel **tidak boleh** merupakan kata kunci (*reserved keywords*) Python seperti `if`, `class`, atau `def`.

Jika Anda melanggar salah satu aturan tersebut, Python akan melemparkan `SyntaxError`.
```python
5variable_name = 5
# Outputs:
#      ^
# SyntaxError: invalid syntax
```

### Konvensi Penamaan yang Umum
Berikut adalah konvensi penamaan variabel yang lazim di Python:
1.  **Gunakan *snake_case***: Nama variabel ditulis dengan huruf kecil semua, dan kata-kata dipisahkan oleh garis bawah (`_`).
    ```python
    my_variable_name = 'freeCodeCamp'
    ```
2.  **Gunakan nama yang deskriptif**: Misalnya, jika Anda ingin menyimpan usia pengguna, `user_age` lebih baik daripada hanya `age` atau singkatan seperti `ua`.
    ```python
    user_age = 30
    ```
    Dengan cara ini, Anda dapat dengan mudah mengomunikasikan tujuan variabel kepada anggota tim lain (atau diri Anda di masa depan) dalam basis kode yang besar.
3.  **Hindari nama variabel satu huruf**: Meskipun sering terlihat, hal ini tidak disarankan karena nama satu huruf tidak mengomunikasikan tujuan atau makna data yang disimpan.
    ```python
    x = 56  # Apa maksud dari x?
    ```

### Komentar di Python
Tanda pagar (`#`) dan teks setelahnya disebut **komentar**. Python akan mengabaikan semua teks yang berada setelah simbol `#` pada baris tersebut saat program dijalankan.

```python
# Ini adalah komentar satu baris
```

Komentar banyak baris (multiline comments) dapat dibuat dengan beberapa komentar satu baris yang berurutan:

```python
# Ini adalah
# komentar
# banyak baris
```
Anda juga bisa menggunakan *docstring* untuk komentar banyak baris, terutama untuk mendokumentasikan fungsi atau kelas, dengan tanda kutip tiga (`"""..."""` atau `'''...'''`).

Komentar sangat berguna untuk menjelaskan kode, meninggalkan pengingat untuk diri sendiri, atau mengklarifikasi mengapa suatu baris kode ada. Komentar sangat membantu saat Anda sedang belajar atau bekerja dalam tim.

Namun, Anda **tidak boleh** menggunakan komentar untuk menjelaskan arti nama variabel yang seharusnya sudah jelas. Sebaliknya, nama yang Anda pilih untuk variabel harus deskriptif dan mengomunikasikan kegunaannya, serta mengikuti aturan penamaan yang disebutkan sebelumnya untuk mencegah kesalahan sintaks.

---

## 3. Bagaimana Fungsi `print()` Bekerja
Setiap bahasa pemrograman memiliki cara untuk mengeluarkan data ke terminal atau konsol. Di Python, Anda menggunakan fungsi bawaan (`built-in function`) `print()` untuk mencetak data.

Salah satu hal pertama yang dilakukan saat belajar bahasa pemrograman adalah menulis program "Hello world!". Di Python, Anda dapat melakukannya dengan sangat mudah menggunakan fungsi `print()`:

```python
print('Hello world!')
# Output: Hello world!
```

String `'Hello world!'` adalah **argumen** yang diteruskan ke fungsi `print()`. Anda juga dapat menggunakan `print()` untuk menampilkan beberapa nilai (argumen) sekaligus dengan memisahkannya menggunakan koma:

```python
print('Warna favorit saya adalah', 'biru', 'hijau', 'merah')
# Output: Warna favorit saya adalah biru hijau merah
```

Python secara otomatis menambahkan spasi di antara setiap item saat Anda memisahkannya dengan koma. Fitur ini sangat membantu ketika Anda ingin mencetak beberapa informasi sekaligus.

---

## 4. Tipe Data Umum di Python
Sebelum bekerja dengan variabel, penting untuk memahami **tipe data**. Tipe data menjelaskan jenis nilai yang dapat disimpan oleh suatu variabel, misalnya angka, teks, atau kumpulan item. Bahasa pemrograman menggunakan tipe data agar tahu cara menyimpan dan bekerja dengan berbagai jenis informasi secara efektif.

Python adalah bahasa **bertipe dinamis** (*dynamically-typed*) seperti JavaScript, artinya Anda tidak perlu mendeklarasikan tipe variabel secara eksplisit. Bahasa ini mengetahui tipe data suatu variabel berdasarkan nilai yang Anda berikan padanya.

**Contoh:**
```python
name = 'John Doe'   # Python secara otomatis mengidentifikasi ini sebagai string
age = 25            # Python secara otomatis mengidentifikasi ini sebagai integer
```

Ini berbeda dengan bahasa bertipe statis (*statically-typed*) seperti C#, Java, dan C++, di mana Anda harus mendeklarasikan tipe data bersamaan dengan nama variabel:
```csharp
string name = "John Doe";
int age = 25;
```

Sifat tipe dinamis di Python membuat pengkodean menjadi cepat dan lebih fleksibel, tetapi perlu diingat bahwa hal ini kadang dapat menyebabkan *bug* tak terduga. Kesalahan tipe data baru terdeteksi saat program berjalan (*runtime*), bukan saat dikompilasi atau ditulis.

> **Catatan Tambahan:**
> Dalam bahasa yang dikompilasi (misalnya C++), pemeriksaan tipe data dilakukan sebelum program dijalankan, sehingga kesalahan tipe dapat diketahui lebih awal. Di Python, kesalahan tipe baru muncul ketika baris kode yang bermasalah dieksekusi selama *runtime*. Ini berarti Anda mungkin baru mengetahui adanya kesalahan tipe setelah program berjalan mencapai bagian tertentu yang mengandung kesalahan tersebut.

### Daftar Tipe Data yang Paling Umum di Python
| Tipe Data | Deskripsi Singkat | Contoh |
|:----------|:-------------------------------------------|:---------------------------|
| `int` | Bilangan bulat (tanpa desimal) | `10`, `-5`, `0` |
| `float` | Bilangan dengan titik desimal | `4.41`, `-0.4`, `3.14` |
| `str` | Rangkaian karakter (teks) dalam tanda kutip | `'Hello world!'`, `"Python"` |
| `bool` | Tipe *boolean* (`True` atau `False`) | `True`, `False` |
| `set` | Koleksi elemen unik yang tidak berurutan | `{0.5, 4, 'apple'}` |
| `dict` | Koleksi pasangan kunci-nilai (*key-value pairs*) dalam kurung kurawal | `{'name': 'John Doe', 'age': 28}` |
| `tuple` | Koleksi terurut yang **immutable** (tidak dapat diubah setelah dibuat), dalam tanda kurung | `('apple', 4.5, 7)` |
| `range` | Urutan bilangan yang tidak dapat diubah, sering dipakai dalam perulangan | `range(5)` (merepresentasikan 0, 1, 2, 3, 4) |
| `list` | Koleksi terurut yang **mutable** (dapat diubah setelah dibuat) dan mendukung berbagai tipe data, dalam kurung siku | `[22, 'Hello world', 3.14, True]` |
| `NoneType` | Nilai khusus yang mewakili ketiadaan nilai | `None` |

**Contoh kode untuk setiap tipe data:**

```python
my_integer_var = 10
print('Integer:', my_integer_var) # Output: Integer: 10

my_float_var = 4.50
print('Float:', my_float_var)     # Output: Float: 4.5

my_string_var = 'hello'
print('String:', my_string_var)   # Output: String: hello

my_boolean_var = True
print('Boolean:', my_boolean_var) # Output: Boolean: True

my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var)         # Output: Set: {8.5, 7, 'hello'} (urutan bisa berbeda)

my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var) # Output: Dictionary: {'name': 'Alice', 'age': 25}

my_tuple_var = (7, 'hello', 8.5)
print('Tuple:', my_tuple_var)     # Output: Tuple: (7, 'hello', 8.5)

my_range_var = range(5)
print('Range:', my_range_var)     # Output: Range: range(0, 5)

my_list = [22, 'Hello world', 3.14, True]
print('List:', my_list)           # Output: List: [22, 'Hello world', 3.14, True]

my_none_var = None
print('NoneType:', my_none_var)   # Output: NoneType: None
```

---

## 5. Fungsi `type()` dan `isinstance()`
Untuk melihat tipe data dari suatu variabel atau nilai, Anda dapat menggunakan fungsi bawaan `type()`.

```python
developer = 'Devin'
print(type(developer)) # Output: <class 'str'>
```
Output `<class 'str'>` berarti variabel `developer` bertipe `string`.

Jika Anda tidak memberikan argumen apa pun ke `type()`, akan muncul `TypeError`:
```python
# type() # Akan menghasilkan TypeError: type() takes 1 or 3 arguments
```

Berikut contoh pemakaian `type()` untuk semua tipe data yang telah dipelajari:

```python
print(type(10))                               # Output: <class 'int'>
print(type(4.50))                             # Output: <class 'float'>
print(type('hello'))                          # Output: <class 'str'>
print(type(True))                             # Output: <class 'bool'>
print(type({7, 'hello', 8.5}))                # Output: <class 'set'>
print(type({'name': 'Alice', 'age': 25}))     # Output: <class 'dict'>
print(type((7, 'hello', 8.5)))                # Output: <class 'tuple'>
print(type(range(5)))                         # Output: <class 'range'>
print(type([22, 'Hello world', 3.14, True]))  # Output: <class 'list'>
print(type(None))                             # Output: <class 'NoneType'>
```

### Fungsi `isinstance()`
Sering kali Anda perlu memeriksa apakah suatu variabel memiliki tipe tertentu sebelum melakukan operasi padanya. Di sinilah fungsi `isinstance()` berguna.

Fungsi ini menerima dua argumen: sebuah objek (variabel) dan tipe (atau tuple tipe) yang ingin diperiksa. Kemudian, ia akan mengembalikan nilai boolean (`True` atau `False`).

```python
account_balance = '12'
print(isinstance(account_balance, int)) # Output: False
```
Karena `account_balance` adalah string, hasil dari `isinstance(account_balance, int)` adalah `False`.

Jika Anda mencoba melakukan operasi matematika pada string, Python akan memberikan `TypeError`:
```python
account_balance = '12'
# account_balance / 2 # Akan menghasilkan TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

`isinstance()` juga bisa memeriksa beberapa tipe sekaligus dengan memberikan tuple tipe sebagai argumen kedua:
```python
account_balance = 12
print(isinstance(account_balance, (int, float))) # Output: True
```
Pada contoh di atas, `account_balance` adalah integer, sehingga `isinstance()` mengembalikan `True`. Jika nilainya `12.0`, hasilnya tetap `True` karena kita memeriksa apakah itu integer **atau** float.

> **Tips:**
> - Gunakan `type()` ketika Anda hanya ingin mengetahui tipe pasti dari suatu objek.
> - Gunakan `isinstance()` ketika Anda perlu memvalidasi apakah suatu objek sesuai dengan tipe tertentu (atau beberapa tipe) sebelum melanjutkan pemrosesannya, ini lebih fleksibel dan seringkali lebih "Pythonic".

---

## 6. String dan Immutabilitas String
**String** adalah rangkaian karakter yang diapit oleh tanda kutip tunggal (`'...'`) atau ganda (`"..."`). Di Python, keduanya diperlakukan sama, jadi Anda bebas memilih salah satu.

```python
my_str_1 = 'Hello'
my_str_2 = "World"
```

Untuk string multi-baris, Anda dapat menggunakan tiga tanda kutip ganda (`"""..."""`) atau tanda kutip tunggal (`'''...'''`):
```python
my_str_3 = """Multiline
string"""
print(my_str_3)
# Output:
# Multiline
# string

my_str_4 = '''Another
multiline
string'''
print(my_str_4)
# Output:
# Another
# multiline
# string
```

### Menangani Tanda Kutip di Dalam String
Jika string Anda mengandung tanda kutip yang sama dengan pembungkus string (misalnya, string dengan tanda kutip tunggal di dalamnya dibungkus oleh tanda kutip tunggal juga), ada dua opsi untuk menghindarinya:
1.  **Gunakan jenis kutip yang berlawanan**:
    ```python
    msg = "It's a sunny day"         # String dibungkus ganda, kutip tunggal di dalam aman
    quote = 'She said, "Hello World!"' # String dibungkus tunggal, kutip ganda di dalam aman
    print(msg)   # Output: It's a sunny day
    print(quote) # Output: She said, "Hello World!"
    ```
2.  *Escape* tanda kutip dengan garis miring terbalik (`\`):
    ```python
    msg = 'It\'s a sunny day'           # Menghindari bentrok kutip tunggal
    quote = "She said, \"Hello!\""    # Menghindari bentrok kutip ganda
    print(msg)   # Output: It's a sunny day
    print(quote) # Output: She said, "Hello!"
    ```

### Operator `in` untuk String
Operator `in` mengembalikan nilai boolean (`True` atau `False`) yang menunjukkan apakah suatu karakter atau *substring* (bagian dari string) ada di dalam string.

```python
my_str = 'Hello world'
print('Hello' in my_str)   # Output: True (Substring 'Hello' ada)
print('hey' in my_str)     # Output: False (Substring 'hey' tidak ada)
print('hi' in my_str)      # Output: False (Substring 'hi' tidak ada)
print('e' in my_str)       # Output: True (Karakter 'e' ada)
print('f' in my_str)       # Output: False (Karakter 'f' tidak ada)
```

### Panjang String dan Indeks
Gunakan fungsi bawaan `len()` untuk mendapatkan panjang (jumlah karakter) dari sebuah string:
```python
my_str = 'Hello world'
print(len(my_str))   # Output: 11 (termasuk spasi)
```

Setiap karakter dalam string memiliki posisi yang disebut **indeks**. Indeks dimulai dari `0` untuk karakter pertama. Untuk mengakses karakter berdasarkan indeks, gunakan tanda kurung siku (`[]`):

```python
my_str = "Hello world"
print(my_str[0])    # Output: H (Karakter pada indeks 0)
print(my_str[6])    # Output: w (Karakter pada indeks 6)
```

**Indeks negatif** juga diperbolehkan di Python. Indeks `-1` merujuk pada karakter terakhir, `-2` pada karakter kedua terakhir, dan seterusnya:
```python
print(my_str[-1])   # Output: d (Karakter terakhir)
print(my_str[-2])   # Output: l (Karakter kedua terakhir)
```

### Tipe Data Immutable dan Mutable
Di Python, semua data diperlakukan sebagai objek. Objek-objek ini memiliki sifat **immutable** (tidak dapat diubah) atau **mutable** (dapat diubah).

-   Objek **immutable** tidak dapat dimodifikasi setelah dibuat. Anda hanya bisa mengarahkan variabel ke nilai baru (*reassignment*), tetapi tidak bisa mengubah elemen di dalamnya secara individual.
-   Objek **mutable** dapat dimodifikasi setelah dibuat.

**String adalah tipe data immutable**. Artinya, Anda dapat menugaskan ulang string yang berbeda ke variabel (mengubah variabel untuk merujuk ke objek string yang baru):
```python
greeting = 'hi'
print(greeting) # Output: hi
greeting = 'hello' # Variabel 'greeting' sekarang merujuk ke objek string baru 'hello'
print(greeting) # Output: hello
```
Tetapi Anda **tidak bisa** mengubah karakter secara langsung di dalam string yang sudah ada:
```python
greeting = 'hi'
# greeting[0] = 'H' # Memicu TypeError: 'str' object does not support item assignment
```

Contoh tipe immutable lainnya termasuk: integer, float, boolean, tuple, dan `None`. Sedangkan tipe mutable antara lain: list, set, dan dictionary.

---

## 7. Penggabungan String (*Concatenation*) dan Interpolasi String
### Penggabungan String dengan `+`
Anda dapat menggabungkan beberapa string menggunakan operator plus (`+`). Proses ini disebut **string concatenation**.

```python
my_str_1 = 'Hello'
my_str_2 = "World"
str_plus_str = my_str_1 + ' ' + my_str_2 # Menambahkan spasi di antara dua string
print(str_plus_str) # Output: Hello World
```

Operasi ini **hanya bekerja untuk string**. Jika Anda mencoba menggabungkan string dengan tipe data lain seperti angka secara langsung, akan muncul `TypeError`:

```python
name = 'John Doe'
age = 26
# name_and_age = name + age # Memicu TypeError: can only concatenate str (not "int") to str
```
Untuk mengatasinya, Anda harus secara eksplisit mengonversi angka menjadi string menggunakan fungsi `str()`:
```python
name_and_age = name + str(age)
print(name_and_age) # Output: John Doe26
```
Perhatikan bahwa output di atas menggabungkan nama dan usia tanpa spasi karena `str(age)` hanya mengonversi angka menjadi string tanpa menambahkan spasi.

### Operator Penugasan Gabungan `+=`
Operator `+=` adalah bentuk singkat dari `variabel = variabel + nilai`. Ini melakukan penggabungan string dan penugasan dalam satu langkah sekaligus.

```python
name_and_age = name # name_and_age = 'John Doe'
name_and_age += str(age) # name_and_age = 'John Doe' + '26'
print(name_and_age) # Output: John Doe26
```

### Interpolasi String dengan f-string
**f-string** (kependekan dari *formatted string literals*) adalah cara yang sangat direkomendasikan untuk melakukan interpolasi string di Python. Metode ini memungkinkan Anda menyematkan ekspresi Python atau nilai variabel ke dalam string dengan sintaks yang ringkas dan mudah dibaca.

Untuk menggunakan f-string, awali string dengan huruf `f` atau `F` (misalnya `f"..."` atau `F'...'`), lalu tempatkan variabel atau ekspresi di dalam kurung kurawal `{}`.

```python
name = 'John Doe'
age = 26
name_and_age = f'Nama saya {name} dan saya berumur {age} tahun.'
print(name_and_age) # Output: Nama saya John Doe dan saya berumur 26 tahun.

num1 = 5
num2 = 10
print(f'Jumlah {num1} dan {num2} adalah {num1 + num2}.') # Output: Jumlah 5 dan 10 adalah 15.
```

Perhatikan bahwa Anda **tidak perlu** mengonversi tipe data non-string (seperti integer `age` atau hasil `num1 + num2`) secara manual dengan `str()` di dalam f-string. Konversi tipe akan dilakukan secara otomatis oleh Python di balik layar. f-string adalah metode yang sangat kuat dan sering digunakan dalam pengembangan Python modern.

---

## 8. *String Slicing* (Mengiris String)
*String slicing* adalah cara untuk mengekstrak sebagian (*sub-sequence*) dari sebuah string. Ini dilakukan menggunakan sintaks:

```
string[start:stop]
```
-   `start`: Indeks posisi awal irisan (inklusif). Jika dihilangkan, defaultnya adalah `0` (awal string).
-   `stop`: Indeks posisi akhir irisan (eksklusif, karakter pada indeks ini tidak termasuk). Jika dihilangkan, defaultnya adalah panjang string (akhir string).

**Contoh dasar:**
```python
my_str = 'Hello world'
print(my_str[1:4])    # Output: ell (Karakter dari indeks 1 sampai sebelum indeks 4)
```

**Ketika `start` dihilangkan:** Ini akan memotong string dari awal (indeks 0) hingga indeks `stop` yang ditentukan.
```python
print(my_str[:7])     # Output: Hello w (Karakter dari indeks 0 hingga sebelum indeks 7)
```

**Ketika `stop` dihilangkan:** Ini akan memotong string dari indeks `start` yang ditentukan hingga akhir string.
```python
print(my_str[8:])     # Output: rld (Karakter dari indeks 8 sampai akhir string)
```

Penting untuk diingat bahwa mengiris string **tidak** akan mengubah string aslinya. String adalah objek *immutable*. Slicing selalu menghasilkan string baru.
```python
print(my_str[8:]) # Output: rld
print(my_str)     # Output: Hello world (String asli tidak berubah)
```

Menghilangkan kedua parameter `start` dan `stop` akan menghasilkan salinan lengkap dari seluruh string:
```python
print(my_str[:])  # Output: Hello world (Salinan dari string asli)
```

### Parameter `step` (Langkah)
Sintaks lengkap untuk *string slicing* adalah:

```
string[start:stop:step]
```
`step` menentukan kenaikan indeks setiap langkah saat irisan dibuat. Defaultnya adalah `1`.

```python
print(my_str[0:11:2]) # Output: Hlowrd (Mengambil setiap karakter kedua dari indeks 0 hingga 10)
```
Dalam contoh ini:
- `H` (indeks 0)
- `l` (indeks 2)
- `o` (indeks 4)
- `w` (indeks 6)
- `r` (indeks 8)
- `d` (indeks 10)

**Trik membalik string**: Jika Anda menggunakan `step = -1` tanpa menentukan `start` dan `stop`, Python akan membalik seluruh string.
```python
print(my_str[::-1]) # Output: dlrow olleH
```

---

## 9. Metode-Metode String yang Umum
Python menyediakan banyak metode bawaan yang memungkinkan Anda untuk memanipulasi dan menganalisis string dengan mudah. Metode-metode ini dipanggil pada objek string menggunakan sintaks `string.method_name()`.

Berikut adalah beberapa metode string yang paling sering digunakan:

| Metode                | Deskripsi                                                               | Contoh & Output                                                     |
|:----------------------|:------------------------------------------------------------------------|:--------------------------------------------------------------------|
| `upper()`             | Mengembalikan string baru dengan semua karakter huruf besar.            | `'hello world'.upper()` → `'HELLO WORLD'`                           |
| `lower()`             | Mengembalikan string baru dengan semua karakter huruf kecil.            | `'Hello World'.lower()` → `'hello world'`                           |
| `strip([chars])`      | Menghapus karakter spasi putih (default) atau karakter tertentu dari awal dan akhir string. | `'  hello world  '.strip()` → `'hello world'`<br>`'---hello---'.strip('-')` → `'hello'` |
| `replace(old, new)`   | Mengganti semua kemunculan `old` substring dengan `new` substring dan mengembalikan string baru. | `'hello world'.replace('hello', 'hi')` → `'hi world'`              |
| `split([separator])`  | Memisahkan string menjadi sebuah *list* berdasarkan `separator` yang diberikan (default: spasi putih) dan mengembalikan list string. | `'hello world'.split()` → `['hello', 'world']`<br>`'a,b,c'.split(',')` → `['a', 'b', 'c']` |
| `join(iterable)`      | Menggabungkan elemen-elemen dari sebuah *iterable* (misalnya list string) menjadi satu string, menggunakan string tempat metode ini dipanggil sebagai pemisah. | `' '.join(['hello', 'world'])` → `'hello world'`<br>`', '.join(['apple', 'banana', 'cherry'])` → `'apple, banana, cherry'` |
| `startswith(prefix)`  | Mengembalikan `True` jika string dimulai dengan `prefix` yang ditentukan. | `'hello world'.startswith('hello')` → `True`                       |
| `endswith(suffix)`    | Mengembalikan `True` jika string diakhiri dengan `suffix` yang ditentukan. | `'hello world'.endswith('world')` → `True`                         |
| `find(substring)`     | Mengembalikan indeks pertama dari `substring` yang ditemukan. Mengembalikan `-1` jika substring tidak ditemukan. | `'hello world'.find('world')` → `6`<br>`'hello world'.find('xyz')` → `-1` |
| `count(substring)`    | Menghitung berapa kali `substring` muncul dalam string.                 | `'hello world'.count('o')` → `2`<br>`'banana'.count('a')` → `3`    |
| `capitalize()`        | Mengembalikan string dengan huruf pertama dikapitalisasi dan sisanya huruf kecil. | `'hello world'.capitalize()` → `'Hello world'`                     |
| `isupper()`           | Mengembalikan `True` jika semua karakter dalam string adalah huruf besar (dan setidaknya ada satu karakter huruf). | `'HELLO'.isupper()` → `True`<br>`'Hello'.isupper()` → `False` |
| `islower()`           | Mengembalikan `True` jika semua karakter dalam string adalah huruf kecil (dan setidaknya ada satu karakter huruf). | `'hello'.islower()` → `True`<br>`'Hello'.islower()` → `False` |
| `title()`             | Mengembalikan string dalam format judul, di mana huruf pertama setiap kata dikapitalisasi. | `'hello world'.title()` → `'Hello World'`                          |

> **Catatan tambahan:**
> Python juga memiliki metode `maketrans()` dan `translate()` untuk pemetaan karakter 1-ke-1 yang lebih kompleks. `str.maketrans()` digunakan untuk membuat tabel translasi, dan `str.translate()` menggunakan tabel tersebut untuk mengganti karakter dalam string.
> ```python
> # Contoh maketrans dan translate
> translate_table = str.maketrans("aeiou", "12345") # Membuat tabel: a->1, e->2, dst.
> text = "hello python"
> translated_text = text.translate(translate_table)
> print(translated_text) # Output: h2ll4 pyth4n
> ```
> Metode-metode ini tidak mengubah string asli karena string di Python adalah *immutable*. Mereka selalu mengembalikan string baru yang telah dimodifikasi.

---

## 10. Bekerja dengan Integer dan Floating Point Numbers
Di Python, angka dibagi menjadi beberapa tipe data utama, dua yang paling umum adalah **Integer** dan **Float**.

-   **Integer** (`int`): Merepresentasikan bilangan bulat tanpa komponen desimal, baik positif, negatif, atau nol.
    ```python
    my_int_1 = 56
    my_int_2 = -4
    print(type(my_int_1)) # Output: <class 'int'>
    ```

-   **Float** (`float`): Merepresentasikan bilangan riil dengan komponen desimal.
    ```python
    my_float_1 = -12.0
    my_float_2 = 4.9
    print(type(my_float_1)) # Output: <class 'float'>
    ```

### Operasi Aritmetika Dasar
Python mendukung semua operasi aritmetika dasar:
```python
# Penjumlahan (+)
print("Penjumlahan Integer:", 56 + 12)    # Output: Penjumlahan Integer: 68
print("Penjumlahan Float:", 5.4 + 12.0)   # Output: Penjumlahan Float: 17.4

# Pengurangan (-)
print("Pengurangan Integer:", 56 - 12)    # Output: Pengurangan Integer: 44
print("Pengurangan Float:", 12.0 - 5.4)   # Output: Pengurangan Float: 6.6

# Perkalian (*)
print("Perkalian Integer:", 12 * 4)       # Output: Perkalian Integer: 48
print("Perkalian Float:", 12.0 * 5.4)     # Output: Perkalian Float: 64.80000000000001 (Lihat catatan presisi float di bawah)

# Pembagian (/)
# Pembagian di Python 3 selalu menghasilkan float, meskipun hasilnya adalah bilangan bulat
print("Pembagian Integer:", 56 / 12)      # Output: Pembagian Integer: 4.666666666666667
print("Pembagian Float:", 12.0 / 5.4)     # Output: Pembagian Float: 2.2222222222222223
```

Jika Anda mencampur integer dan float dalam operasi aritmetika, hasilnya secara otomatis akan dikonversi menjadi `float` untuk menjaga presisi:
```python
print("Hasil campuran int dan float:", 56 + 5.4)       # Output: Hasil campuran int dan float: 61.4
print("Tipe hasil campuran:", type(56 + 5.4))          # Output: Tipe hasil campuran: <class 'float'>
```

### Operator Aritmetika Lanjutan
-   **Modulo (`%`)** : Mengembalikan sisa dari operasi pembagian.
    ```python
    print("Modulo (int):", 56 % 12)       # Output: Modulo (int): 8 (56 = 4 * 12 + 8)
    print("Modulo (float):", 12.0 % 5.4)  # Output: Modulo (float): 1.1999999999999993
    ```
-   **Pembagian bulat (`//`)** : Mengembalikan hasil pembagian yang dibulatkan ke bawah (*floor division*) ke bilangan bulat terdekat.
    ```python
    print("Floor Division (int):", 56 // 12)      # Output: Floor Division (int): 4
    print("Floor Division (float):", 12.0 // 5.4) # Output: Floor Division (float): 2.0
    ```
-   **Eksponensiasi (`**`)** : Menghitung pangkat (misal: `base` dipangkatkan `exponent`).
    ```python
    print("Eksponensiasi (int):", 56 ** 2)          # Output: Eksponensiasi (int): 3136 (56 kuadrat)
    print("Eksponensiasi (float):", 5.4 ** 3.0)     # Output: Eksponensiasi (float): 157.46399999999998
    ```

### Mengapa `0.1 + 0.2` Tidak Tepat `0.3`?
Terkadang, hasil operasi dengan angka *float* memiliki digit desimal lebih banyak dari yang diharapkan, misalnya `0.1 + 0.2` bisa menghasilkan `0.30000000000000004` (ini tidak selalu terjadi di semua sistem atau versi Python, tetapi adalah fenomena umum).

Ini terjadi karena komputer menyimpan bilangan dalam format biner. Beberapa pecahan desimal (seperti 0.1 atau 0.2) tidak dapat direpresentasikan secara tepat dalam biner, mirip dengan bagaimana 1/3 tidak dapat ditulis tepat sebagai desimal (0.3333...). Akibatnya, timbul kesalahan pembulatan kecil (*floating-point precision error*) dalam perhitungan. Untuk perhitungan yang membutuhkan presisi tinggi (misalnya keuangan), disarankan menggunakan modul `decimal`.

### Konversi Tipe: `int()` dan `float()`
Anda dapat mengonversi antara tipe data `int` dan `float` menggunakan fungsi bawaan `int()` dan `float()`.
-   `int()`: Mengonversi nilai ke integer. Jika dari float, akan memotong bagian desimal (membulatkan ke bawah, *truncation*).
    ```python
    my_float = 12.92563
    my_int = int(my_float)
    print(my_int) # Output: 12 (bagian desimal dipotong)
    ```
-   `float()`: Mengonversi nilai ke float.
    ```python
    my_int_1 = 56
    my_float_1 = float(my_int_1)
    print(my_float_1) # Output: 56.0
    ```

Konversi dari string juga dimungkinkan, asalkan string tersebut merepresentasikan angka yang valid:
```python
converted_int = int('45')
converted_float = float('7.8')
print(converted_int, type(converted_int))     # Output: 45 <class 'int'>
print(converted_float, type(converted_float)) # Output: 7.8 <class 'float'>
```
Jika string bukan representasi angka yang valid, akan muncul `ValueError`.

### Fungsi Numerik Bawaan Lainnya
-   **`round(number, [ndigits])`** : Membulatkan angka ke sejumlah desimal tertentu. Jika `ndigits` dihilangkan, dibulatkan ke integer terdekat. Pembulatan ke genap terdekat jika angka di tengah (e.g., `.5`).
    ```python
    print(round(4.798))     # Output: 5
    print(round(4.253, 1))  # Output: 4.3
    print(round(2.5))       # Output: 2 (default to nearest even)
    print(round(3.5))       # Output: 4 (default to nearest even)
    ```
-   **`abs(number)`** : Mengembalikan nilai absolut (nilai non-negatif) dari angka.
    ```python
    print(abs(-15))         # Output: 15
    print(abs(15))          # Output: 15
    ```
-   **`pow(base, exp, [mod])`** : Menghitung `base` dipangkatkan `exp`. Jika `mod` diberikan, mengembalikan hasilnya modulo `mod`.
    ```python
    print(pow(2, 3))        # Output: 8 (sama dengan 2**3)
    print(pow(2, 3, 5))     # Output: 3 (sama dengan (2**3) % 5 -> 8 % 5 = 3)
    ```

---

## 11. *Augmented Assignments* (Penugasan Gabungan)
*Augmented assignment* atau penugasan gabungan adalah cara ringkas untuk menulis operasi di mana hasil dari operasi biner ditetapkan kembali ke variabel yang sama. Ini adalah singkatan untuk `variabel = variabel <operator> nilai`.

Sintaks umum adalah:
```python
variabel <operator>= nilai
```

### Operator *Augmented Assignment*
-   **Penambahan `+=`**:
    ```python
    my_var = 10
    my_var += 5        # Ini setara dengan: my_var = my_var + 5
    print(my_var)      # Output: 15
    ```
-   **Pengurangan `-=`**:
    ```python
    count = 14
    count -= 3         # Ini setara dengan: count = count - 3
    print(count)       # Output: 11
    ```
-   **Perkalian `*=`**:
    ```python
    product = 65
    product *= 7       # Ini setara dengan: product = product * 7
    print(product)     # Output: 455
    ```
-   **Pembagian `/=`**:
    ```python
    price = 100
    price /= 4         # Ini setara dengan: price = price / 4
    print(price)       # Output: 25.0 (Pembagian selalu menghasilkan float)
    ```
-   **Pembagian Bulat `//=`**:
    ```python
    total_pages = 23
    total_pages //= 5  # Ini setara dengan: total_pages = total_pages // 5
    print(total_pages) # Output: 4
    ```
-   **Modulo `%=`**:
    ```python
    bits = 35
    bits %= 2          # Ini setara dengan: bits = bits % 2
    print(bits)        # Output: 1
    ```
-   **Eksponensiasi `**=`**:
    ```python
    power = 2
    power **= 3        # Ini setara dengan: power = power ** 3
    print(power)       # Output: 8
    ```

### *Augmented Assignment* pada String
-   Operator `+=` juga dapat digunakan untuk menggabungkan string:
    ```python
    greet = 'Hello'
    greet += ' World'
    print(greet)       # Output: Hello World
    ```
-   Operator `*=` dapat digunakan untuk mengulang string:
    ```python
    greet = 'Hello'
    greet *= 3
    print(greet)       # Output: HelloHelloHello
    ```
-   Operator *augmented assignment* lainnya (`-=`, `/=`, `//=`, `%=`, `**=`) akan memunculkan `TypeError` jika digunakan pada tipe data string karena operasi tersebut tidak terdefinisi untuk string.

> **Catatan Penting:**
> Python **tidak** memiliki operator *increment* atau *decrement* seperti `++` atau `--` yang ada di beberapa bahasa pemrograman lain (misalnya C++ atau JavaScript). Untuk menambah atau mengurangi nilai variabel sebesar satu, Anda harus menggunakan `x += 1` atau `x -= 1` yang lebih eksplisit dan mudah dibaca.

---

## 12. Pernyataan Kondisional dan Operator Logika
Pernyataan kondisional memungkinkan program untuk membuat keputusan dan menjalankan blok kode yang berbeda berdasarkan apakah suatu kondisi `True` atau `False`.

### Operator Perbandingan
Operator perbandingan membandingkan dua nilai dan mengembalikan nilai boolean (`True` atau `False`).

| Operator | Nama                   | Deskripsi                                 |
|:---------|:-----------------------|:------------------------------------------|
| `==`     | Sama dengan            | Memeriksa apakah dua nilai sama.          |
| `!=`     | Tidak sama dengan      | Memeriksa apakah dua nilai tidak sama.    |
| `>`      | Lebih besar dari       | Memeriksa apakah nilai kiri lebih besar dari nilai kanan. |
| `<`      | Kurang dari            | Memeriksa apakah nilai kiri kurang dari nilai kanan. |
| `>=`     | Lebih besar atau sama dengan | Memeriksa apakah nilai kiri lebih besar atau sama dengan nilai kanan. |
| `<=`     | Kurang dari atau sama dengan | Memeriksa apakah nilai kiri kurang dari atau sama dengan nilai kanan. |

**Contoh penggunaan operator perbandingan:**
```python
print(3 > 4)   # Output: False
print(3 < 4)   # Output: True
print(3 == 4)  # Output: False
print(4 == 4)  # Output: True
print(3 != 4)  # Output: True
print(3 >= 4)  # Output: False
print(3 <= 4)  # Output: True

name = 'Alice'
print(name == 'Alice') # Output: True
print(name != 'Bob')   # Output: True
```

### Pernyataan `if`
Pernyataan `if` adalah blok kode dasar untuk kondisional. Blok kode di dalamnya akan dieksekusi hanya jika kondisi yang diberikan bernilai `True`.

```python
if kondisi:
    # blok kode ini akan dieksekusi jika 'kondisi' adalah True
```
Blok kode di bawah `if` ditentukan oleh **indentasi**. Di Python, indentasi adalah bagian integral dari sintaksis. Disarankan standar 4 spasi per level indentasi. Jika indentasi tidak konsisten atau tidak ada, Python akan melemparkan `IndentationError`.

```python
age = 18
if age >= 18:
    print('Anda sudah dewasa.') # Output: Anda sudah dewasa.
```

### `else` dan `elif`
-   **`else`**: Blok `else` akan dieksekusi jika kondisi `if` (dan `elif` sebelumnya, jika ada) bernilai `False`.
-   **`elif` (else if)**: Memungkinkan Anda untuk memeriksa kondisi tambahan jika kondisi `if` sebelumnya bernilai `False`. Anda dapat memiliki banyak blok `elif`.

Struktur lengkapnya adalah:
```python
if kondisi1:
    # blok kode jika kondisi1 True
elif kondisi2:
    # blok kode jika kondisi1 False DAN kondisi2 True
else:
    # blok kode jika semua kondisi sebelumnya (kondisi1, kondisi2, dll.) False
```

**Contoh penggunaan `if`, `elif`, dan `else`:**
```python
age = 12
if age >= 18:
    print('Anda sudah dewasa.')
elif age >= 13:
    print('Anda remaja.')
else:
    print('Anda anak-anak.') # Output: Anda anak-anak.
```

> **Penting:** Tidak boleh ada pernyataan atau baris kode lain di antara blok `if` dan `else` (atau `elif`) pada level indentasi yang sama. Hal tersebut akan menyebabkan `SyntaxError`.

### `if` Bersarang (*nested if*)
Anda dapat menempatkan (menumpuk) pernyataan `if` di dalam pernyataan `if` lainnya. Ini memungkinkan Anda untuk mengecek kondisi yang lebih kompleks.

```python
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('Anda memenuhi syarat untuk memilih.') # Output: Anda memenuhi syarat untuk memilih.
    else:
        print('Anda warga negara tapi belum cukup umur untuk memilih.')
else:
    print('Anda tidak memenuhi syarat karena bukan warga negara.')
```
Meskipun *nested if* memungkinkan pengecekan beragam kondisi, terlalu banyak bersarang dapat membuat kode sulit dibaca dan dipelihara. Seringkali, operator logika (`and`, `or`, `not`) dapat membantu menyederhanakan kondisi bersarang menjadi satu ekspresi.

---

## 13. Nilai *Truthy* dan *Falsy*, Operator Boolean, dan *Short-Circuiting*
### Nilai *Truthy* dan *Falsy*
Di Python, setiap nilai memiliki nilai boolean inheren ketika dievaluasi dalam konteks logika (misalnya dalam pernyataan `if`).
-   **Falsy**: Nilai-nilai yang dianggap `False` dalam konteks boolean. Ini termasuk:
    -   `None`
    -   `False`
    -   Angka nol (`0`, `0.0`, `0j` untuk *complex numbers*)
    -   String kosong `''` atau `""`
    -   `list` kosong `[]`
    -   `tuple` kosong `()`
    -   `dict` kosong `{}`
    -   `set` kosong `set()`
-   **Truthy**: Semua nilai selain yang disebut sebagai *falsy* dianggap `True` dalam konteks boolean. Contoh:
    -   `True`
    -   Angka bukan nol (misalnya `1`, `-5`, `3.14`)
    -   String tidak kosong (misalnya `'Hello'`, `' '`)
    -   `list` tidak kosong (misalnya `[1, 2]`)
    -   Objek lainnya

Anda dapat menggunakan fungsi `bool()` untuk secara eksplisit memeriksa nilai boolean dari suatu objek:
```python
print(bool(False))   # Output: False
print(bool(0))       # Output: False
print(bool(''))      # Output: False
print(bool([]))      # Output: False

print(bool(True))    # Output: True
print(bool(1))       # Output: True
print(bool('Hello')) # Output: True
print(bool([1, 2]))  # Output: True
```

### Operator Boolean (Logika)
Python memiliki tiga operator boolean: `and`, `or`, dan `not`. Operator ini digunakan untuk menggabungkan atau memanipulasi ekspresi boolean.

-   **`and`**:
    -   Mengembalikan operand kiri jika operand kiri adalah *falsy*.
    -   Jika operand kiri adalah *truthy*, mengembalikan operand kanan.
    -   Kedua operand harus *truthy* agar hasil ekspresi secara keseluruhan dianggap *truthy*.
    ```python
    print(True and 25)  # Output: 25 (True adalah truthy, jadi mengembalikan 25)
    print(False and 25) # Output: False (False adalah falsy, jadi mengembalikan False)
    print(0 and 'hello') # Output: 0 (0 adalah falsy, jadi mengembalikan 0)
    print('hi' and 10)  # Output: 10 ('hi' adalah truthy, jadi mengembalikan 10)
    ```

-   **`or`**:
    -   Mengembalikan operand kiri jika operand kiri adalah *truthy*.
    -   Jika operand kiri adalah *falsy*, mengembalikan operand kanan.
    -   Setidaknya satu operand harus *truthy* agar hasil ekspresi secara keseluruhan dianggap *truthy*.
    ```python
    print(19 or False)  # Output: 19 (19 adalah truthy, jadi mengembalikan 19)
    print(False or 19)  # Output: 19 (False adalah falsy, jadi mengembalikan 19)
    print(0 or '')      # Output: '' (0 adalah falsy, '' adalah falsy, mengembalikan '' sebagai operand kedua)
    print(1 or 2)       # Output: 1 (1 adalah truthy, jadi mengembalikan 1)
    ```

-   **`not`**:
    -   Membalikkan nilai boolean dari operandnya.
    -   Selalu mengembalikan `True` atau `False`.
    ```python
    print(not '')      # Output: True (Karena '' adalah falsy, not '' menjadi True)
    print(not 'Hello') # Output: False (Karena 'Hello' adalah truthy, not 'Hello' menjadi False)
    print(not True)    # Output: False
    print(not False)   # Output: True
    ```

### *Short-Circuiting*
Operator `and` dan `or` bersifat **short-circuit** (evaluasi pintas). Ini berarti Python akan mengevaluasi ekspresi dari kiri ke kanan dan berhenti segera setelah hasil akhir ekspresi dapat ditentukan, tanpa perlu mengevaluasi operand yang tersisa.

-   Untuk `and`: Jika operand pertama adalah *falsy*, Python tahu bahwa seluruh ekspresi `and` akan `False`, jadi tidak perlu mengevaluasi operand kedua.
-   Untuk `or`: Jika operand pertama adalah *truthy*, Python tahu bahwa seluruh ekspresi `or` akan `True`, jadi tidak perlu mengevaluasi operand kedua.

**Contoh `and` dalam kondisional:**
```python
is_citizen = True
age = 25
if is_citizen and age >= 18: # 'is_citizen' (True) dievaluasi, kemudian 'age >= 18' (True) dievaluasi.
    print('Anda memenuhi syarat memilih.') # Output: Anda memenuhi syarat memilih.
```
Jika `is_citizen` adalah `False`, `age >= 18` tidak akan dievaluasi.

**Contoh `or` dalam kondisional:**
```python
age = 19
is_student = True
if age < 18 or is_student: # 'age < 18' (False) dievaluasi, kemudian 'is_student' (True) dievaluasi.
    print('Anda memenuhi syarat diskon pelajar.') # Output: Anda memenuhi syarat diskon pelajar.
```
Jika `age < 18` adalah `True`, `is_student` tidak akan dievaluasi.

**Contoh `not`:**
```python
is_admin = False
if not is_admin: # 'not is_admin' menjadi 'True'
    print('Akses ditolak untuk non-administrator.') # Output: Akses ditolak untuk non-administrator.
```

Memahami *truthy*, *falsy*, operator boolean, dan *short-circuiting* sangat penting untuk menulis kode Python yang efisien dan logis.

---

## 14. Fungsi di Python
Fungsi adalah blok kode yang terorganisir, dapat digunakan kembali, dan dirancang untuk melakukan tugas tertentu. Python memiliki banyak fungsi bawaan (`built-in functions`) seperti `print()`, `input()`, dan `int()`. Selain itu, Anda dapat membuat fungsi kustom Anda sendiri menggunakan kata kunci `def`.

### Fungsi Bawaan yang Berguna
```python
# input(): Meminta input dari pengguna melalui konsol
name = input('Siapa nama Anda? ')   # Misal pengguna mengetik "Kolade"
print('Halo', name)                 # Output: Halo Kolade

# int(): Mengonversi nilai ke integer
print(int(3.14))      # Output: 3 (memotong bagian desimal)
print(int('42'))      # Output: 42 (mengonversi string '42' menjadi integer 42)
print(int(True))      # Output: 1 (Boolean True dianggap 1 dalam konteks integer)
```

### Mendefinisikan Fungsi Sendiri
Anda dapat mendefinisikan fungsi Anda sendiri menggunakan kata kunci `def`, diikuti dengan nama fungsi, tanda kurung `()`, dan titik dua `:`. Badan fungsi harus diindentasi.

```python
def hello():
    print('Hello World')

hello() # Memanggil fungsi hello(). Output: Hello World
```

Fungsi dapat memiliki **parameter** (placeholder yang menerima nilai saat fungsi dipanggil) dan menerima **argumen** (nilai aktual yang diteruskan ke parameter fungsi) saat dipanggil:
```python
def calculate_sum(a, b): # 'a' dan 'b' adalah parameter
    print(a + b)

calculate_sum(3, 1)   # Output: 4 (3 dan 1 adalah argumen yang diberikan ke 'a' dan 'b')
calculate_sum(10, 20) # Output: 30
```

Jika jumlah argumen yang diteruskan tidak sesuai dengan jumlah parameter yang diharapkan oleh fungsi, Python akan melemparkan `TypeError`:
```python
# calculate_sum() # Memicu TypeError: calculate_sum() missing 2 required positional arguments
```

### `return`
Gunakan pernyataan `return` untuk mengembalikan nilai dari fungsi. Ketika `return` dieksekusi, fungsi akan segera berhenti, dan nilai yang diikuti `return` akan menjadi hasil dari pemanggilan fungsi tersebut.

Jika sebuah fungsi tidak memiliki pernyataan `return` eksplisit, atau memiliki `return` tanpa nilai, fungsi tersebut secara implisit akan mengembalikan `None`.

```python
def calculate_sum(a, b):
    return a + b # Fungsi ini mengembalikan hasil penjumlahan

my_sum = calculate_sum(3, 1) # Nilai yang dikembalikan (4) disimpan di my_sum
print(my_sum)   # Output: 4

def greet_user(name):
    print(f"Halo, {name}!")

result = greet_user("Budi") # Fungsi ini hanya mencetak, tidak mengembalikan nilai eksplisit
print(result)              # Output: Halo, Budi!
                           #         None (karena tidak ada 'return', fungsi mengembalikan None)
```

---

## 15. Scope (Ruang Lingkup) di Python – Aturan LEGB
**Scope** (ruang lingkup) adalah wilayah di dalam program di mana suatu variabel atau nama dapat diakses. Python memiliki aturan yang jelas untuk menentukan *scope* variabel, yang sering disebut aturan **LEGB**:

-   **L** (Local): Variabel yang didefinisikan di dalam sebuah fungsi atau metode. Variabel ini hanya dapat diakses dari dalam fungsi tersebut.
-   **E** (Enclosing Function Local): Variabel yang didefinisikan di dalam fungsi luar (fungsi yang membungkus fungsi lain). Variabel ini dapat diakses oleh fungsi dalam (fungsi bersarang).
-   **G** (Global): Variabel yang didefinisikan di tingkat teratas sebuah modul (file Python). Variabel ini dapat diakses dari mana saja di dalam modul tersebut.
-   **B** (Built-in): Nama-nama bawaan Python yang sudah tersedia secara *default*, seperti `print`, `len`, `True`, `False`, `None`. Ini adalah *scope* terluar.

Python akan mencari variabel dari *scope* terdalam (Local) ke *scope* terluar (Built-in).

### Local Scope
Variabel yang didefinisikan di dalam sebuah fungsi memiliki *local scope*. Mereka tidak dapat diakses di luar fungsi tersebut.
```python
def my_func():
    my_var = 10 # my_var adalah variabel lokal
    print(my_var)

my_func()         # Output: 10 (dari dalam fungsi)
# print(my_var)   # Memicu NameError: name 'my_var' is not defined (diakses dari luar fungsi)
```

### Enclosing Scope
Ketika ada fungsi bersarang (fungsi di dalam fungsi), fungsi dalam dapat mengakses variabel dari fungsi luar (*enclosing function*). Variabel dari fungsi luar ini berada dalam *enclosing scope* bagi fungsi dalam.
```python
def outer_func():
    msg = 'Hello there!' # msg berada di enclosing scope untuk inner_func
    def inner_func():
        print(msg) # inner_func dapat mengakses msg
    inner_func()

outer_func()   # Output: Hello there!
```
Secara default, fungsi dalam hanya dapat membaca variabel dari *enclosing scope*. Untuk memodifikasi variabel di *enclosing scope* dari dalam fungsi dalam, Anda harus menggunakan kata kunci `nonlocal`.
```python
def outer_func():
    msg = 'Hello there!'
    res = ""
    def inner_func():
        nonlocal res      # Deklarasikan res sebagai variabel non-lokal (dari enclosing scope)
        res = 'How are you?'
        print(msg)        # Masih bisa membaca msg
    inner_func()
    print(res)            # Output: How are you? (variabel res di outer_func telah diubah)

outer_func()
```

### Global Scope
Variabel yang didefinisikan di tingkat teratas file Python (bukan di dalam fungsi manapun) memiliki *global scope*. Variabel ini dapat diakses (dibaca) dari mana saja di dalam file tersebut.
```python
my_var_global = 10 # my_var_global berada di global scope

def read_global_var():
    print(my_var_global) # Fungsi dapat membaca variabel global

read_global_var() # Output: 10
print(my_var_global) # Output: 10 (bisa diakses di tingkat global)
```
Untuk memodifikasi variabel global dari dalam fungsi, Anda harus secara eksplisit menggunakan kata kunci `global`. Jika tidak, Python akan membuat variabel lokal baru dengan nama yang sama di dalam fungsi tersebut.
```python
my_var_global = 10

def change_global_var():
    global my_var_global # Deklarasikan my_var_global sebagai variabel global yang akan dimodifikasi
    my_var_global = 20   # Mengubah variabel global

change_global_var()
print(my_var_global) # Output: 20 (variabel global telah diubah)

# Contoh tanpa global, membuat variabel lokal baru:
another_global_var = 50
def change_without_global():
    another_global_var = 100 # Ini membuat VARIABEL LOKAL baru bernama another_global_var

change_without_global()
print(another_global_var) # Output: 50 (variabel global tidak berubah)
```

### Built-in Scope
Nama-nama di *built-in scope* adalah nama-nama yang sudah disediakan oleh Python secara bawaan dan selalu tersedia.
```python
print(str(45))       # Output: '45' (str adalah built-in)
print(type(3.14))    # Output: <class 'float'> (type adalah built-in)
print(isinstance(3, str)) # Output: False (isinstance adalah built-in)
```
Anda tidak boleh mendefinisikan ulang nama-nama *built-in*, karena ini akan menimpa fungsionalitas aslinya.

Memahami aturan LEGB sangat penting untuk menghindari kesalahan `NameError` dan untuk menulis kode yang jelas dan mudah diprediksi terkait aksesibilitas variabel.

---

# Ringkasan Dasar-Dasar Python
Bagian ini merangkum semua materi yang telah dibahas sebelumnya, memberikan gambaran singkat untuk referensi cepat.

## Apa itu Python?
-   Bahasa pemrograman serbaguna yang sederhana dan mudah digunakan.
-   Luas digunakan di *data science*, *machine learning*, *web development*, *cybersecurity*, IoT, otomatisasi, dan banyak lagi.

## Variabel
-   **Deklarasi**: `nama_variabel = nilai`. Python bertipe dinamis.
-   **Aturan Penamaan**:
    -   Dimulai dengan huruf atau `_`, bukan angka.
    -   Hanya berisi huruf, angka, dan `_`.
    -   Bersifat *case-sensitive* (`name` dan `Name` berbeda).
    -   Tidak boleh menggunakan kata kunci Python (misalnya `if`, `for`).
-   **Konvensi**: Gunakan `snake_case` (misalnya `nama_lengkap`), nama yang deskriptif, dan hindari nama variabel satu huruf.

## Komentar
-   **Satu baris**: Dimulai dengan `#`. Python mengabaikan sisanya pada baris tersebut.
-   **Banyak baris**: Bisa menggunakan beberapa `#` atau *docstrings* (string multi-baris diapit `"""..."""` atau `'''...'''`).

## Fungsi `print()`
-   `print('Hello world!')`: Untuk mencetak output ke konsol.
-   Dapat menerima beberapa argumen yang dipisahkan koma; Python akan otomatis menambahkan spasi di antara mereka. Contoh: `print('Nama:', 'Budi')` → `Nama: Budi`.

## Tipe Data Umum
| Tipe Bahasa | Contoh                     | Keterangan                                       |
|:------------|:---------------------------|:-------------------------------------------------|
| `int`       | `10`, `-5`                 | Bilangan bulat.                                  |
| `float`     | `4.50`, `3.14`             | Bilangan dengan titik desimal.                   |
| `str`       | `'hello'`, `"world"`       | Rangkaian karakter (teks). **Immutable**.        |
| `bool`      | `True`, `False`            | Nilai boolean (benar/salah).                     |
| `set`       | `{7, 5, 8}`, `set()`       | Koleksi elemen unik, tidak berurutan. **Mutable**. |
| `dict`      | `{'name': 'Alice', 'age': 25}` | Koleksi pasangan kunci-nilai. **Mutable**.       |
| `tuple`     | `(7, 5, 8)`, `()`          | Koleksi terurut, **immutable**.                  |
| `range`     | `range(5)`                 | Urutan bilangan (misalnya `0, 1, 2, 3, 4`). **Immutable**. |
| `list`      | `[22, 'Hello', 3.14, True]` | Koleksi terurut, dapat berisi berbagai tipe data. **Mutable**. |
| `NoneType`  | `None`                     | Nilai khusus yang merepresentasikan ketiadaan nilai. **Immutable**. |

-   **Tipe Immutable**: int, float, bool, str, tuple, range, None. Nilainya tidak dapat diubah setelah dibuat.
-   **Tipe Mutable**: list, set, dict. Nilainya dapat diubah setelah dibuat.

## `type()` dan `isinstance()`
-   `type(variabel)`: Mengembalikan jenis (kelas) dari suatu objek.
    -   Contoh: `type(10)` → `<class 'int'>`.
-   `isinstance(obj, tipe)`: Mengembalikan `True` jika `obj` adalah instance dari `tipe` yang diberikan, `False` jika tidak. Lebih baik untuk pemeriksaan tipe yang fleksibel.
    -   Dapat memeriksa beberapa tipe sekaligus: `isinstance(x, (int, float))`.

## String
-   Dapat diapit `'...'` atau `"..."`. Untuk multi-baris: `"""..."""` atau `'''...'''`.
-   Karakter khusus dapat di-escape dengan `\` (misalnya `\'`, `\"`).
-   Akses karakter menggunakan indeks: `my_str[0]` (karakter pertama), `my_str[-1]` (karakter terakhir).
-   **Immutable**: Tidak bisa mengubah karakter individu (misalnya `my_str[0] = 'H'` akan eror).
-   **Operator `in`**: `'Hello' in my_str` mengembalikan `True` atau `False` untuk mengecek keberadaan substring.

### Metode String Umum
-   `upper()`, `lower()`: Mengubah kasus huruf.
-   `strip()`: Menghapus spasi putih dari awal/akhir.
-   `replace(old, new)`: Mengganti substring.
-   `split([separator])`: Memisahkan string ke dalam list.
-   `join(iterable)`: Menggabungkan elemen iterable menjadi string.
-   `startswith(prefix)`, `endswith(suffix)`: Mengecek awal/akhir string.
-   `find(substring)`: Mencari indeks pertama substring (`-1` jika tidak ada).
-   `count(substring)`: Menghitung kemunculan substring.
-   `capitalize()`, `title()`: Untuk kapitalisasi spesifik.
-   `isupper()`, `islower()`: Mengecek apakah semua huruf besar/kecil.
-   **`str.maketrans()` dan `str.translate()`**: Untuk pemetaan karakter yang kompleks.
    ```python
    trans_table = str.maketrans('abc', '123')
    'abcabc'.translate(trans_table) # Output: '123123'
    ```

### Penggabungan dan f-string
-   `+` dan `+=`: Untuk menggabungkan string. Pastikan semua operand adalah string (gunakan `str()` untuk konversi).
-   **f-string**: Cara modern dan direkomendasikan untuk interpolasi string. `f'Nama saya {nama} dan umur {umur} tahun.'`

### String Slicing
-   `string[start:stop:step]`: Mengekstrak porsi string.
    -   `start` (inklusi, default 0), `stop` (eksklusi, default akhir string), `step` (loncatan, default 1).
    -   Dapat menggunakan indeks negatif.
    -   `my_str[::-1]` untuk membalik string.

## Integer dan Float
-   **Operasi Aritmetika**: `+`, `-`, `*`, `/`, `%` (modulo), `//` (floor division), `**` (eksponensiasi).
-   Mencampur tipe `int` dan `float` dalam operasi akan menghasilkan `float`.
-   **Konversi Tipe**: `int(nilai)`, `float(nilai)`, juga dapat mengonversi dari string representasi angka.
-   **Fungsi Numerik Bawaan**: `round()`, `abs()`, `pow()`.

## *Augmented Assignments* (Penugasan Gabungan)
-   Sintaks `variabel <operator>= nilai` (misalnya `x += 5`, `y *= 2`). Ini adalah singkatan untuk `variabel = variabel <operator> nilai`.
-   Tidak ada operator `++` atau `--` di Python; gunakan `x += 1` atau `x -= 1`.

## Operator Perbandingan
-   `==` (sama dengan), `!=` (tidak sama dengan), `>` (lebih besar dari), `<` (kurang dari), `>=` (lebih besar atau sama dengan), `<=` (kurang dari atau sama dengan).
-   Mengembalikan nilai boolean (`True` atau `False`).

## Pernyataan Kondisional
-   **`if`**: Mengeksekusi blok kode jika kondisi `True`.
-   **`elif`**: Mengeksekusi blok jika kondisi `if` sebelumnya `False` dan kondisi `elif` ini `True`.
-   **`else`**: Mengeksekusi blok jika semua kondisi `if`/`elif` sebelumnya `False`.
-   Struktur blok kode ditentukan oleh **indentasi** (disarankan 4 spasi).
-   Bisa ada `if` bersarang (*nested if*), tapi sebaiknya dihindari jika bisa disederhanakan dengan operator logika.

## *Truthy*/*Falsy* dan Operator Boolean
-   **Falsy**: Nilai yang dianggap `False` dalam konteks boolean (misalnya `None`, `False`, `0`, `''`, `[]`, `{}`, `set()`).
-   **Truthy**: Semua nilai lainnya yang dianggap `True`.
-   Fungsi `bool()` untuk memeriksa nilai boolean eksplisit.
-   **Operator Logika**:
    -   `and`: Mengembalikan operand pertama jika *falsy*, jika tidak mengembalikan operand kedua. Kedua operand harus *truthy* untuk hasil *truthy*.
    -   `or`: Mengembalikan operand pertama jika *truthy*, jika tidak mengembalikan operand kedua. Minimal satu operand *truthy* untuk hasil *truthy*.
    -   `not`: Membalikkan nilai boolean; selalu mengembalikan `True` atau `False`.
-   ***Short-Circuiting***: `and` dan `or` mengevaluasi dari kiri ke kanan dan berhenti segera setelah hasil akhir dapat ditentukan, tanpa mengevaluasi operand yang tersisa.

## Fungsi
-   Didefinisikan dengan `def nama_fungsi(parameter): ...`.
-   Dapat menerima **parameter** dan mengembalikan nilai dengan `return ekspresi`. Jika tidak ada `return` atau `return` kosong, fungsi mengembalikan `None`.
-   Dapat memiliki parameter bawaan (bersama dan default).
-   Contoh fungsi bawaan: `input()`, `int()`, `float()`, `len()`.

## Scope (Ruang Lingkup) – Aturan LEGB
-   **L (Local)**: Variabel di dalam fungsi.
-   **E (Enclosing Function Local)**: Variabel di fungsi luar (untuk fungsi bersarang). Gunakan `nonlocal` untuk memodifikasinya.
-   **G (Global)**: Variabel di tingkat modul (file). Gunakan `global` untuk memodifikasinya dari dalam fungsi.
-   **B (Built-in)**: Nama-nama bawaan Python (misalnya `print`, `True`).

---

Dengan memahami semua konsep di atas, Anda telah memiliki fondasi yang kuat dalam dasar-dasar Python. Selanjutnya, Anda dapat mendalami materi seperti struktur data lanjutan (misalnya list, dictionary lebih dalam), penanganan *exception*, modul dan paket, penanganan file, dan paradigma pemrograman berorientasi objek atau fungsional.