## Daftar Isi
1. [Apa Itu List dan Bagaimana Cara Kerjanya?](#apa-itu-list-dan-bagaimana-cara-kerjanya)
2. [Metode-Metode Umum pada List](#metode-metode-umum-pada-list)
3. [Apa Itu Tuple dan Bagaimana Cara Kerjanya?](#apa-itu-tuple-dan-bagaimana-cara-kerjanya)
4. [Metode-Metode Umum untuk Tuple](#metode-metode-umum-untuk-tuple)
5. [Bagaimana Cara Kerja Perulangan (Loop)?](#bagaimana-cara-kerja-perulangan-loop)
6. [Apa Itu Range dan Bagaimana Menggunakannya dalam Loop?](#apa-itu-range-dan-bagaimana-menggunakannya-dalam-loop)
7. [Fungsi `enumerate()` dan `zip()` serta Cara Kerjanya](#fungsi-enumerate-dan-zip-serta-cara-kerjanya)
8. [List Comprehension dan Fungsi-Fungsi Berguna untuk List](#list-comprehension-dan-fungsi-fungsi-berguna-untuk-list)
9. [Apa Itu Fungsi Lambda dan Bagaimana Cara Kerjanya?](#apa-itu-fungsi-lambda-dan-bagaimana-cara-kerjanya)
10. [Rangkuman: Perulangan dan Sequence](#rangkuman-perulangan-dan-sequence)

---

## Apa Itu List dan Bagaimana Cara Kerjanya?

Dalam beberapa pelajaran ke depan kita akan mempelajari **list**, **tuple**, dan **range**, yaitu tiga tipe data *sequence* dasar yang digunakan di Python.

Tipe data `list` adalah urutan elemen yang teratur yang dapat terdiri dari *string*, angka, atau bahkan *list* lain. *List* bersifat **mutable** (dapat diubah) dan menggunakan pengindeksan berbasis nol, artinya elemen pertama *list* berada pada indeks 0.

Berikut sintaks dasar untuk sebuah *list*:

```python
cities = ['Los Angeles', 'London', 'Tokyo']
```

Untuk mengakses elemen dari *list* `cities`, Anda bisa merujuk nomor indeksnya di dalam urutan. Contoh mengakses elemen pertama:

```python
cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[0]) # Output: 'Los Angeles'
```

Pengindeksan negatif digunakan untuk mengakses elemen dari akhir *list*, bukan dari awal (indeks 0). Untuk mengakses elemen terakhir *list*, gunakan `-1` seperti ini:

```python
cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[-1]) # Output: 'Tokyo'
```

Cara lain membuat *list* adalah dengan menggunakan **konstruktor** `list()`. Konstruktor `list()` digunakan untuk mengubah sebuah *iterable* menjadi *list*:

```python
developer = 'Jessica'
print(list(developer)) # Output: ['J', 'e', 's', 's', 'i', 'c', 'a']
```

> **Catatan Tambahan:** *Iterable* adalah jenis objek khusus yang dapat di-*loop* satu per satu. Anda akan belajar lebih lanjut tentang *loop* di Python nanti.

Untuk mendapatkan jumlah total elemen dalam *list*, gunakan fungsi `len()`:

```python
numbers = [1, 2, 3, 4, 5]
print(len(numbers)) # Output: 5
```

Jika Anda ingin memperbarui nilai pada indeks tertentu, lakukan seperti ini:

```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # Output: ['JavaScript', 'Java', 'C++', 'Rust']
```

Karena *list* bersifat *mutable*, Anda dapat memperbarui elemen mana pun di dalam *list* selama Anda memberikan nomor indeks yang valid. Jika Anda memberikan indeks (positif atau negatif) yang berada di luar jangkauan *list*, Anda akan mendapatkan `IndexError`:

```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']
# Mencoba mengakses indeks yang tidak ada
# programming_languages[10] = 'JavaScript'

"""
Output jika dijalankan:
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list assignment index out of range
"""
```

Untuk menghapus elemen dari *list*, gunakan kata kunci `del`:

```python
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # Output: ['Jane Doe', 'Python Developer']
```

Terkadang berguna untuk memeriksa apakah suatu elemen ada di dalam *list*. Gunakan kata kunci `in`:

```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']

print('Rust' in programming_languages)       # Output: True
print('JavaScript' in programming_languages) # Output: False
```

Tidak jarang kita memiliki *list* yang bersarang di dalam *list* lain:

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
```

Di sini ada satu *list* bersarang yang berisi tiga bahasa pemrograman populer. Untuk mengakses *list* bersarang tersebut, gunakan indeks 2 karena *list* berbasis indeks nol:

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2]) # Output: ['Python', 'Rust', 'C++']
```

Kemudian untuk mengakses bahasa kedua dari *list* bersarang itu, gunakan indeks 1 setelah mengakses *list* bersarangnya:

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2][1]) # Output: 'Rust'
```

Teknik umum lainnya yang digunakan dengan *list* adalah **unpacking** (membongkar) nilai.

*Unpacking* nilai dari *list* adalah teknik untuk menetapkan nilai-nilai dari *list* ke variabel-variabel baru. Contoh *unpacking list* `developer` ke dalam variabel `name`, `age`, dan `job`:

```python
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # Output: 'Alice'
print(age)  # Output: 34
print(job)  # Output: 'Rust Developer'
```

Di sini `name` bernilai `'Alice'`, `age` bernilai `34`, dan `job` bernilai `'Rust Developer'`.

Jika Anda perlu mengumpulkan elemen-elemen yang tersisa dari sebuah *list*, gunakan operator asterisk (`*`):

```python
developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name) # Output: 'Alice'
print(rest) # Output: [34, 'Rust Developer']
```

Pada contoh ini, `name` tetap bernilai `'Alice'`, dan `rest` adalah sebuah *list* berisi dua item: angka `34` dan *string* `'Rust Developer'`.

Apabila jumlah variabel di sisi kiri operator penugasan tidak cocok dengan jumlah total item di dalam *list*, Anda akan mendapatkan `ValueError`:

```python
developer = ['Alice', 34, 'Rust Developer']
# Mencoba melakukan unpacking dengan jumlah variabel yang salah
# name, age, job, city = developer

"""
Output jika dijalankan:
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
"""
```

Konsep terakhir yang akan kita lihat adalah operator *slice* (`:`). Seperti pada *string*, Anda dapat mengakses sebagian *list* menggunakan operator *slice*:

```python
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:4]) # Output: ['Cookies', 'Ice Cream', 'Pie']
```

Pada contoh di atas, indeks awal adalah 1 (menunjuk ke item kedua). Operator *slice* diikuti indeks akhir 4, yang berarti mengambil semua item mulai indeks 1 hingga sebelum indeks 4 (indeks 4 tidak ikut).

Hal lain yang bisa dilakukan dengan operator *slice* `:` adalah menentukan **step interval** (langkah) yang menentukan seberapa besar kenaikan antar indeks. Misalkan Anda memiliki *list* angka:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

Jika Anda ingin mengekstrak *list* berisi hanya bilangan genap, gunakan *slicing* seperti ini:

```python
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1::2]) # Output: [2, 4, 6]
```

Bilangan genap pertama ada di indeks 1, maka itu menjadi indeks awal. Karena kita ingin sampai akhir *list*, indeks akhir dihilangkan. Terakhir, kita tentukan `2` untuk *step interval* opsional, sehingga hanya melompat setiap 2 langkah (nilai *default*-nya 1).

*List* adalah struktur data yang berguna dan fleksibel yang akan sering Anda gunakan dalam program Python. Di pelajaran berikutnya, Anda akan mempelajari metode-metode umum yang dapat digunakan bersama *list*.

---

## Metode-Metode Umum pada List

Pada pelajaran sebelumnya, Anda telah diperkenalkan dengan tipe data *list* serta belajar mengakses elemen dan melakukan *slicing*. Di pelajaran ini kita lanjutkan dengan metode-metode umum seperti `append()`, `pop()`, dan `sort()`.

### `append()`
Metode `append()` digunakan untuk menambahkan item ke akhir *list*. Contoh menambahkan angka 6 ke *list* `numbers`:

```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # Output: [1, 2, 3, 4, 5, 6]
```

Anda juga bisa menambahkan satu *list* ke akhir *list* lain menggunakan `append()`:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # Output: [1, 2, 3, 4, 5, [6, 8, 10]]
```

Perhatikan bahwa seluruh *list* `even_numbers` menjadi bersarang di dalam `numbers`.

### `extend()`
Jika Anda ingin menambahkan semua elemen individual dari *list* `even_numbers` ke akhir `numbers`, gunakan metode `extend()`.

`extend()` mirip dengan `append()`, tetapi dengan `extend()` Anda dapat menambahkan banyak elemen dari satu *list* ke *list* lain. Contoh:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # Output: [1, 2, 3, 4, 5, 6, 8, 10]
```

Seperti terlihat, *list* bersarang hilang dan sekarang hanya berupa *list* angka.

### `insert()`
Untuk menyisipkan elemen pada indeks tertentu di *list*, gunakan `insert()`. Metode ini menerima dua argumen: indeks tempat Anda ingin menyisipkan item baru dan item yang akan disisipkan.

```python
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers) # Output: [1, 2, 2.5, 3, 4, 5]
```

Kode di atas menyisipkan angka `2.5` pada indeks 2.

### `remove()`
Untuk menghapus elemen dari *list* berdasarkan nilainya, gunakan `remove()`. Metode ini menerima nilai elemen yang akan dihapus:

```python
numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers) # Output: [10, 20, 30, 40, 50]
```

Penting diperhatikan bahwa metode ini hanya menghapus **kemunculan pertama** item, bukan semuanya:

```python
numbers = [10, 20, 30, 40, 50, 50, 50]
numbers.remove(50)

print(numbers) # Output: [10, 20, 30, 40, 50, 50]
```

### `pop()`
Untuk menghapus elemen pada indeks tertentu dan mengembalikannya, gunakan `pop()`:

```python
numbers = [1, 2, 3, 4, 5]
removed_item = numbers.pop(1)
print(removed_item) # Output: 2
print(numbers)      # Output: [1, 3, 4, 5]
```

Jika Anda tidak menyebutkan indeks, elemen terakhir yang akan dihapus:

```python
numbers = [1, 2, 3, 4, 5]
removed_item = numbers.pop()
print(removed_item) # Output: 5
print(numbers)      # Output: [1, 2, 3, 4]
```

### `clear()`
Untuk mengosongkan seluruh *list*, gunakan `clear()`:

```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()

print(numbers) # Output: []
```

### `sort()`
Metode `sort()` digunakan untuk mengurutkan elemen di tempat (*in-place*). Contoh mengurutkan *list* angka acak:

```python
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # Output: [1, 2, 19, 35, 41, 67]
```

Berbeda dengan `sort()`, fungsi bawaan `sorted()` bekerja pada semua *iterable* dan mengembalikan *list* baru yang sudah terurut, tanpa mengubah *list* asli.

```python
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers)       # Output: [19, 2, 35, 1, 67, 41] (list asli tidak berubah)
print(sorted_numbers) # Output: [1, 2, 19, 35, 41, 67] (list baru yang terurut)
```

Sebagai pengingat, *iterable* adalah objek yang dapat di-*loop*, sehingga Anda bisa mengakses setiap item satu per satu. Anda akan belajar lebih banyak tentang *loop* nanti.

Baik `sort()` maupun `sorted()` menerima parameter opsional `key` dan `reverse`. Detailnya akan dibahas di pelajaran mendatang bersama *tuple*.

### `reverse()`
Metode `reverse()` membalik urutan elemen *list* di tempat:

```python
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers) # Output: [1, 2, 3, 4, 5, 6]
```

### `index()`
Metode `index()` digunakan untuk mencari indeks pertama tempat suatu elemen ditemukan dalam *list*. Contoh mencari bahasa `'Java'`:

```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(programming_languages.index('Java')) # Output: 1
```

Jika elemen tidak ditemukan, Python akan melemparkan `ValueError`:

```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']
# Mencoba mencari item yang tidak ada
# programming_languages.index('JavaScript')

"""
Output jika dijalankan:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'JavaScript' is not in list
"""
```

Masih ada beberapa metode lain untuk *list* Python, tetapi metode-metode di atas sudah cukup sebagai permulaan.

---

## Apa Itu Tuple dan Bagaimana Cara Kerjanya?

**Tuple** adalah tipe data Python yang digunakan untuk membuat urutan nilai yang teratur. *Tuple* dapat berisi campuran tipe data:

```python
developer = ('Alice', 34, 'Rust Developer')
```

*Tuple* mirip dengan *list*, tetapi sementara *list* bersifat *mutable* (dapat diubah), *tuple* bersifat **immutable** (tidak dapat diubah). Artinya elemen dalam *tuple* tidak bisa diubah setelah *tuple* dibuat.

Jika Anda mencoba memperbarui salah satu item dalam *tuple*, Anda akan mendapatkan `TypeError`:

```python
programming_languages = ('Python', 'Java', 'C++', 'Rust')
# Mencoba mengubah elemen tuple
# programming_languages[0] = 'JavaScript'

"""
Output jika dijalankan:
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment
"""
```

Untuk mengakses elemen dari *tuple*, gunakan notasi kurung siku dan nomor indeks:

```python
developer = ('Alice', 34, 'Rust Developer')
print(developer[1]) # Output: 34
```

Gunakan pengindeksan negatif untuk mengakses dari akhir *tuple*. Contoh mengambil elemen kedua dari belakang:

```python
numbers = (1, 2, 3, 4, 5)
print(numbers[-2]) # Output: 4
```

Jika Anda memberikan indeks yang melebihi atau sama dengan panjang *tuple*, akan muncul `IndexError`:

```python
numbers = (1, 2, 3, 4, 5)
# Mencoba mengakses indeks di luar jangkauan
# numbers[7]

"""
Output jika dijalankan:
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: tuple index out of range
"""
```

Cara lain membuat *tuple* adalah dengan konstruktor `tuple()`. Anda bisa memasukkan berbagai *iterable* seperti *string*, *list*, bahkan *tuple* lain:

```python
developer = 'Jessica'
print(tuple(developer)) # Output: ('J', 'e', 's', 's', 'i', 'c', 'a')
```

Untuk memeriksa apakah suatu item ada dalam *tuple*, gunakan kata kunci `in`:

```python
programming_languages = ('Python', 'Java', 'C++', 'Rust')

print('Rust' in programming_languages)       # Output: True
print('JavaScript' in programming_languages) # Output: False
```

Anda juga bisa melakukan *unpacking* item dari *tuple* seperti pada *list*:

```python
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # Output: 'Alice'
print(age)  # Output: 34
print(job)  # Output: 'Rust Developer'
```

Untuk mengumpulkan elemen-elemen yang tersisa, gunakan operator `*`:

```python
developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(name) # Output: 'Alice'
print(rest) # Output: [34, 'Rust Developer']
```

Di sini `name` bernilai `'Alice'`, dan `rest` adalah *list* berisi angka 34 dan *string* `'Rust Developer'`.

Sama seperti *list*, Anda bisa menggunakan operator *slice* pada *tuple* untuk mengekstrak sebagian darinya. Contoh mengekstrak `'pie'` dan `'cookies'`:

```python
desserts = ('cake', 'pie', 'cookies', 'ice cream')
print(desserts[1:3]) # Output: ('pie', 'cookies')
```

Ingat, angka pertama adalah indeks awal, angka kedua adalah indeks akhir (item pada indeks akhir tidak ikut disertakan).

Menghapus item dari *tuple* tidak dimungkinkan karena *tuple* adalah *immutable*. Contoh ini akan menghasilkan error:

```python
developer = ('Jane Doe', 23, 'Python Developer')
# Mencoba menghapus elemen tuple
# del developer[1]

"""
Output jika dijalankan:
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'tuple' object doesn't support item deletion
"""
```

**Kapan menggunakan *tuple* dibanding *list*?**
Jika Anda memerlukan kumpulan elemen dinamis yang dapat ditambah, dihapus, dan diubah, gunakan *list*. Jika Anda bekerja dengan data yang tetap dan tidak berubah, gunakan *tuple*.

Di pelajaran selanjutnya, kita akan melihat beberapa metode umum untuk *tuple*.

---

## Metode-Metode Umum untuk Tuple

### `count()`
Metode `count()` digunakan untuk menghitung berapa kali suatu item muncul dalam *tuple*.

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.count('Rust')) # Output: 2
```

Jika item tidak ada, hasilnya `0`:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.count('JavaScript')) # Output: 0
```

Jika tidak ada argumen yang diberikan ke `count()`, Python akan menampilkan `TypeError`:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
# Mencoba memanggil count() tanpa argumen
# programming_languages.count()
# TypeError: tuple.count() takes exactly one argument (0 given)
```

### `index()`
Metode `index()` mencari indeks pertama tempat item ditemukan.

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.index('Java')) # Output: 1
```

Jika item tidak ditemukan, Python melemparkan `ValueError`:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
# Mencoba mencari item yang tidak ada
# programming_languages.index('JavaScript')
# ValueError: tuple.index(x): x not in tuple
```

Anda bisa memberikan argumen opsional `start` dan `stop` untuk membatasi pencarian.
Argumen `start` adalah indeks awal pencarian (inklusi), sedangkan `stop` adalah indeks akhir pencarian (eksklusi).

Contoh dengan *start index*:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python', 3)) # Output: 5
```

Di sini pencarian dimulai dari indeks 3, sehingga `'Python'` yang ditemukan adalah pada indeks 5 (bukan indeks 2).

Contoh dengan *start* dan *stop index*:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(programming_languages.index('Python', 2, 5)) # Output: 2
```

Pencarian dimulai dari indeks 2 hingga sebelum indeks 5 (yaitu indeks 2, 3, 4), dan hasilnya indeks 2.

### `sorted()`
Fungsi `sorted()` dapat digunakan pada *iterable* apa pun, termasuk *tuple*. Ia mengembalikan *list* baru yang sudah terurut.

```python
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
print(sorted(numbers)) # Output: [2, 3, 7, 13, 18, 45, 67, 78]
```

Berbeda dengan metode `sort()` pada *list* yang mengurutkan di tempat, `sorted()` selalu membuat *list* baru.

Anda dapat menyesuaikan pengurutan dengan parameter opsional `key` dan `reverse`. Contoh mengurutkan berdasarkan panjang *string*:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, key=len))
# Output: ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']
```

Untuk urutan terbalik, gunakan `reverse=True`:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, reverse=True))
# Output: ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']
```

*Tuple* adalah tipe data yang umum di Python. Memahami cara menggunakannya beserta metode dan fungsi terkait akan membantu Anda menulis kode yang lebih efisien.

---

## Bagaimana Cara Kerja Perulangan (Loop)?

Seperti yang telah Anda pelajari, *loop* digunakan untuk mengulang blok kode sejumlah tertentu. Di pelajaran ini Anda akan mempelajari berbagai jenis *loop* di Python.

### `for` loop
`for` loop digunakan untuk mengiterasi sebuah *sequence* (seperti *list*, *tuple*, atau *string*) dan menjalankan blok kode untuk setiap item.

```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)
```

Hasilnya:

```
Rust
Java
Python
C++
```

Perhatikan bahwa `print(language)` harus menjorok ke dalam (*indentasi*). Tanpa *indentasi* Anda akan mendapatkan `IndentationError`.

Anda juga bisa menggunakan `for` loop pada *string*:

```python
for char in 'code':
    print(char)
```

Hasilnya:

```
c
o
d
e
```

Anda dapat menyarangkan `for` loop (*nested loop*):

```python
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)
```

Hasilnya:

```
Fruit Apple
Fruit Carrot
Fruit Banana
Vegetable Apple
Vegetable Carrot
Vegetable Banana
```

### `while` loop
`while` loop akan terus mengulang selama kondisi bernilai `True`.

Contoh permainan tebak angka:

```python
import random

secret_number = random.randint(1, 5) # Memilih angka acak antara 1 dan 5
guess = 0 # Inisialisasi tebakan

print("Tebak angka rahasia antara 1 sampai 5!")

while guess != secret_number:
    try:
        guess = int(input('Tebak angka: '))
        if guess < 1 or guess > 5:
            print('Angka harus antara 1 dan 5. Coba lagi.')
        elif guess != secret_number:
            print('Salah! Coba lagi.')
    except ValueError:
        print('Input tidak valid. Harap masukkan angka.')

print(f'Anda benar! Angka rahasianya adalah {secret_number}.')
```

Jika pengguna menebak `secret_number`, *loop* berhenti dan pesan `Anda benar!` ditampilkan. Berikut contoh jalannya program:

```
Tebak angka rahasia antara 1 sampai 5!
Tebak angka: 2
Salah! Coba lagi.
Tebak angka: 1
Salah! Coba lagi.
Tebak angka: 3
Anda benar! Angka rahasianya adalah 3.
```

### `break` dan `continue`
Python mendukung pernyataan `break` dan `continue`.

- `break` menghentikan eksekusi *loop* sepenuhnya.
- `continue` melewati iterasi saat ini dan melanjutkan ke iterasi berikutnya.

Contoh `break`:

```python
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        print(f"Menemukan '{developer}', menghentikan loop.")
        break
    print(f"Bekerja dengan {developer}.")
```

Hasilnya:

```
Bekerja dengan Jess.
Menemukan 'Naomi', menghentikan loop.
```
Hanya `Jess` yang ditampilkan sebelum *loop* dihentikan.

Contoh `continue`:

```python
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        print(f"Melewatkan '{developer}'.")
        continue
    print(f"Bekerja dengan {developer}.")
```

Hasilnya:

```
Bekerja dengan Jess.
Melewatkan 'Naomi'.
Bekerja dengan Tom.
```
Sekarang `Jess` dan `Tom` yang tercetak, karena iterasi saat `developer == 'Naomi'` dilewati.

### `else` pada loop
Baik `for` maupun `while` dapat dipasangkan dengan klausul `else`. Blok `else` akan dijalankan hanya jika *loop* tidak dihentikan oleh `break`.

Contoh mencari vokal dalam kata:

```python
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    has_vowel = False # Flag untuk menandai apakah vokal ditemukan
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' mengandung vokal '{letter}'")
            has_vowel = True
            break # Hentikan loop huruf setelah vokal pertama ditemukan
    else: # Blok else ini akan dijalankan jika loop for letter selesai tanpa break
        print(f"'{word}' tidak memiliki vokal")
```

Hasilnya:

```
'sky' tidak memiliki vokal
'apple' mengandung vokal 'a'
'rhythm' tidak memiliki vokal
'fly' tidak memiliki vokal
'orange' mengandung vokal 'o'
```

*Loop* sangat umum di Python, jadi penting untuk merasa nyaman dengannya. Di pelajaran berikutnya Anda akan mempelajari fungsi `enumerate()` dan `range()` di dalam *loop*.

---

## Apa Itu Range dan Bagaimana Menggunakannya dalam Loop?

Fungsi `range()` digunakan untuk menghasilkan urutan bilangan bulat (*integer*). Sintaks dasarnya:

```python
range(start, stop, step)
```

Argumen wajib `stop` adalah bilangan bulat yang mewakili titik akhir (tidak termasuk). Contoh:

```python
print("Contoh range(3):")
for num in range(3):
    print(num)
# Output:
# 0
# 1
# 2
```

Kode di atas menghasilkan bilangan 0, 1, dan 2. Angka `stop` (3) tidak disertakan.

Jika argumen `start` tidak ditentukan, *default*-nya adalah 0. Anda bisa menggunakan `start` untuk memulai dari angka lain:

```python
print("\nContoh range(1, 5):")
for num in range(1, 5):
    print(num)
# Output:
# 1
# 2
# 3
# 4
```

Menghasilkan 1, 2, 3, 4.

Secara *default*, urutan bilangan bertambah 1. Gunakan `step` untuk mengubah kenaikan:

```python
print("\nContoh range(2, 11, 2):")
for num in range(2, 11, 2):
    print(num)
# Output:
# 2
# 4
# 6
# 8
# 10
```

Menghasilkan bilangan genap 2, 4, 6, 8, 10.

Jika `range()` dipanggil tanpa argumen, Anda akan mendapatkan `TypeError`:

```python
# range() tanpa argumen
# range()
# TypeError: range expected at least 1 argument, got 0
```

`range()` hanya menerima *integer*, bukan *float*. Jika *float* digunakan atau hasil perhitungan akan float, akan muncul `TypeError`:

```python
# range() dengan float
# range(1.5, 5.5)
# TypeError: 'float' object cannot be interpreted as an integer
```

Untuk menghasilkan urutan menurun, gunakan *step* negatif:

```python
print("\nContoh range(40, 0, -10):")
for num in range(40, 0, -10):
    print(num)
# Output:
# 40
# 30
# 20
# 10
```

Akan mencetak 40, 30, 20, 10.

Anda juga bisa membuat *list* dari *range* dengan konstruktor `list()`:

```python
numbers = list(range(2, 11, 2))
print(numbers) # Output: [2, 4, 6, 8, 10]
```

Fungsi `range()` sangat praktis untuk menghasilkan urutan *integer*. Setelah terbiasa, Anda akan sering menggunakannya dalam program Python.

---

## Fungsi `enumerate()` dan `zip()` serta Cara Kerjanya

### `enumerate()`
Dalam `for` loop biasa kita mencetak elemen tanpa indeks. Untuk melacak indeks, kita bisa membuat variabel indeks manual. Namun cara yang lebih mudah adalah menggunakan `enumerate()`.

`enumerate()` mengembalikan objek *enumerate* yang berisi pasangan (*indeks*, *nilai*). Jika kita ubah ke *list*:

```python
languages = ['Spanish', 'English', 'Russian', 'Chinese']
print(list(enumerate(languages)))
# Output: [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]
```

Dengan *unpacking* di dalam *loop*:

```python
print("\nMenggunakan enumerate() dalam loop:")
for index, language in enumerate(languages):
    print(f'Index {index} dan bahasa {language}')
```

Hasil:

```
Menggunakan enumerate() dalam loop:
Index 0 dan bahasa Spanish
Index 1 dan bahasa English
Index 2 dan bahasa Russian
Index 3 dan bahasa Chinese
```

`enumerate()` juga menerima argumen opsional `start` untuk menentukan nilai awal hitungan (*default*: 0). Contoh dengan `start=1`:

```python
print("\nMenggunakan enumerate() dengan start=1:")
for index, language in enumerate(languages, 1):
    print(f'Index {index} dan bahasa {language}')
```

Hasil:

```
Menggunakan enumerate() dengan start=1:
Index 1 dan bahasa Spanish
Index 2 dan bahasa English
Index 3 dan bahasa Russian
Index 4 dan bahasa Chinese
```

### `zip()`
`zip()` digunakan untuk menggabungkan beberapa *iterable* secara paralel, menghasilkan *iterator of tuple* yang berisi elemen-elemen dari masing-masing *iterable*.

```python
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))
# Output: [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]
```

Dalam `for` loop:

```python
print("\nMenggunakan zip() dalam loop:")
for name, id in zip(developers, ids):
    print(f'Nama: {name}')
    print(f'ID: {id}')
```

Hasil:

```
Menggunakan zip() dalam loop:
Nama: Naomi
ID: 1
Nama: Dario
ID: 2
Nama: Jessica
ID: 3
Nama: Tom
ID: 4
```

Jika *iterable* memiliki panjang yang berbeda, `zip()` akan berhenti saat *iterable* terpendek habis.

Fungsi `enumerate()` dan `zip()` sangat kuat, dan bila dikombinasikan dengan *loop*, dapat membuat kode jauh lebih ringkas.

---

## List Comprehension dan Fungsi-Fungsi Berguna untuk List

Anda sudah terbiasa menggunakan *loop* seperti ini:

```python
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers) # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

Cara yang lebih ringkas adalah dengan **list comprehension**, yang memungkinkan Anda membuat *list* baru dalam satu baris dengan menggabungkan *loop* dan kondisi di dalam kurung siku.

*Refactor* dengan *list comprehension*:

```python
even_numbers_lc = [num for num in range(21) if num % 2 == 0]
print(even_numbers_lc) # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

*List comprehension* melakukan *loop* dari 0 hingga 20 (rentang 21 angka, 0-20) dan hanya menyertakan bilangan yang habis dibagi 2. Pendekatan ini lebih kompak dan menghilangkan kebutuhan akan blok *loop* dan kondisi terpisah yang lebih panjang.

Contoh lain untuk menghasilkan *tuple* (angka, status ganjil/genap) menggunakan kondisi *ternary* di dalam *list comprehension*:

```python
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)
```

Hasil:

```
[(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]
```

### `filter()`
`filter()` digunakan untuk memilih elemen dari *iterable* yang memenuhi kondisi tertentu. Ia menerima sebuah fungsi dan sebuah *iterable*. Fungsi tersebut harus mengembalikan nilai Boolean (`True` atau `False`).

Contoh: membuat *list* kata yang panjangnya lebih dari 4:

```python
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words_iterator = filter(is_long_word, words)
print(list(long_words_iterator)) # Output: ['mountain', 'river', 'cloud']
```
Perhatikan bahwa `filter()` mengembalikan sebuah *iterator*, sehingga perlu dikonversi ke *list* (atau tipe data lain) untuk dicetak.

### `map()`
`map()` menerapkan sebuah fungsi ke setiap elemen *iterable* dan mengembalikan *iterable* baru dengan hasilnya.

Contoh: mengonversi suhu Celsius ke Fahrenheit:

```python
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit_iterator = map(to_fahrenheit, celsius)
print(list(fahrenheit_iterator)) # Output: [32.0, 50.0, 68.0, 86.0, 104.0]
```
Sama seperti `filter()`, `map()` juga mengembalikan *iterator*.

### `sum()`
`sum()` menjumlahkan semua elemen dalam *iterable* (misalnya *list*, *tuple*, dll).

```python
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Output: 50
```

Anda bisa memberikan argumen opsional `start` sebagai nilai awal penjumlahan. Argumen ini akan ditambahkan ke jumlah total elemen *iterable*.

Contoh dengan argumen posisional:

```python
total_with_start_pos = sum(numbers, 10)
print(total_with_start_pos) # Output: 60 (50 + 10)
```

Atau dengan *keyword argument* agar lebih eksplisit:

```python
total_with_start_kw = sum(numbers, start=10)
print(total_with_start_kw) # Output: 60 (50 + 10)
```

*List comprehension* beserta fungsi seperti `map()`, `filter()`, dan `sum()` mungkin terasa agak membingungkan pada awalnya. Namun dengan latihan yang cukup, Anda akan semakin nyaman menggunakannya.

---

## Apa Itu Fungsi Lambda dan Bagaimana Cara Kerjanya?

Selama ini Anda mendefinisikan fungsi dengan kata kunci `def`:

```python
def square(num):
    return num ** 2

print(square(4)) # Output: 16
```

Untuk fungsi-fungsi *higher-order* seperti `map()` dan `filter()`, Anda bisa menggunakan fungsi anonim satu baris yang disebut **fungsi lambda**.

Contoh fungsi `square` diubah menjadi *lambda*:

```python
# Sintaksia dasar fungsi lambda
# lambda arg1, arg2, ... : ekspresi

square_lambda = lambda num: num ** 2
print(square_lambda(4)) # Output: 16
```
Fungsi *lambda* tidak memiliki nama (anonim). Cocok digunakan saat kita hanya butuh ekspresi singkat, misalnya dalam `filter()`:

```python
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
```

### Praktik Terbaik Lambda
1.  **Jangan menugaskan *lambda* ke variabel**, karena itu menghilangkan tujuan anonimnya dan tidak memberikan keuntungan dibandingkan fungsi `def` biasa. Lebih baik gunakan fungsi biasa `def` untuk fungsi bernama:

    ```python
    # TIDAK DISARANKAN
    # square = lambda x: x ** 2
    # print(square(5))

    # DISARANKAN
    def square(num):
        return num ** 2
    print(square(5)) # Output: 25
    ```

2.  **Hindari *lambda* yang rumit dan sulit dibaca**, seperti yang melibatkan banyak logika kondisional atau operasi kompleks:

    ```python
    # TIDAK DISARANKAN (lambda yang terlalu kompleks untuk dibaca)
    # result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)
    # print(result)  # Output: 14
    ```

    Akan lebih baik ditulis dengan fungsi `def` yang jelas:

    ```python
    # DISARANKAN (jelas dan mudah dibaca)
    def calculate_expression(x):
        if x > 0:
            return x**2 + 2*x - 1
        else:
            return x**3 - x + 4

    print(calculate_expression(3))  # Output: 14
    ```

Baik fungsi reguler maupun *lambda* memiliki tempatnya masing-masing. Gunakan *lambda* untuk ekspresi *inline* singkat dan sederhana, terutama saat dilewatkan sebagai argumen ke fungsi *higher-order*. Untuk logika yang lebih kompleks dan dapat digunakan kembali, gunakan fungsi biasa dengan `def`.

---

## Rangkuman: Perulangan dan Sequence

### Python Lists
-   **Definisi**: *List* adalah urutan elemen terurut yang dapat berisi *string*, angka, atau *list* lain. *List* bersifat **mutable** dan berbasis indeks nol.
-   **Membuat List**:
    ```python
    cities = ['Los Angeles', 'London', 'Tokyo']
    ```
-   **Mengakses Elemen**:
    ```python
    cities[0]   # 'Los Angeles'
    cities[-1]  # 'Tokyo'
    ```
-   **Menggunakan Konstruktor `list()`**:
    ```python
    developer = 'Jessica'
    list(developer)  # ['J','e','s','s','i','c','a']
    ```
-   **Panjang List (`len()`)**:
    ```python
    len([1,2,3,4,5])  # 5
    ```
-   **Mutabilitas**: Elemen dapat diubah dengan indeks valid.
    ```python
    programming_languages = ['Python', 'Java']
    programming_languages[0] = 'JavaScript' # ['JavaScript', 'Java']
    ```
-   **`IndexError`**: Muncul jika indeks di luar jangkauan.
-   **Menghapus Elemen**: `del list[index]`.
-   **Keanggotaan**: `'Rust' in programming_languages` (mengembalikan `True` atau `False`).
-   **List Bersarang**: Mengakses elemennya seperti `developer[2][1]`.
-   **Unpacking**: `name, age, job = list`.
    -   Mengumpulkan sisa dengan `*`: `name, *rest = list`.
    -   `ValueError` jika jumlah variabel tidak cocok dengan jumlah elemen.
-   **Slicing**: Mengambil sebagian *list*.
    -   `desserts[1:4]`
    -   `numbers[1::2]` (dengan *step interval*).

### Metode-Metode Umum pada List
-   `append(item)`: Menambah item ke akhir *list*.
-   `extend(iterable)`: Menambah semua elemen *iterable* ke akhir *list*.
-   `insert(index, item)`: Menyisipkan item pada indeks tertentu.
-   `remove(value)`: Menghapus kemunculan pertama dari nilai.
-   `pop(index)`: Menghapus dan mengembalikan elemen pada indeks (default: indeks terakhir).
-   `clear()`: Mengosongkan seluruh *list*.
-   `sort()`: Mengurutkan *list* di tempat (*in-place*).
-   `sorted(iterable)`: Mengembalikan *list* baru yang terurut dari *iterable* apapun, tanpa mengubah yang asli.
-   `reverse()`: Membalik urutan elemen *list* di tempat.
-   `index(value)`: Mengembalikan indeks pertama dari nilai yang ditemukan, atau `ValueError` jika tidak ada.

### Tuples di Python
-   **Definisi**: *Tuple* adalah urutan elemen terurut yang **immutable** (tidak dapat diubah setelah dibuat).
-   **Contoh**: `developer = ('Alice', 34, 'Rust Developer')`.
-   **`TypeError`**: Terjadi saat mencoba mengubah elemen *tuple*.
-   **Akses**: Sama seperti *list*, menggunakan indeks `developer[1]` atau `numbers[-2]`.
-   **`IndexError`**: Terjadi jika indeks di luar jangkauan.
-   **Konstruktor `tuple()`**: `tuple('Jessica')`.
-   **Keanggotaan**: `'Rust' in programming_languages`.
-   **Unpacking & `*`**: Sama seperti *list*.
-   **Slicing**: Sama seperti *list*, contoh `desserts[1:3]`.
-   **Penghapusan**: Tidak dimungkinkan, akan menghasilkan `TypeError` karena *immutable*.
-   **Kapan menggunakan *tuple*?**: Saat data tetap dan tidak perlu diubah.

### Metode-Metode Umum untuk Tuple
-   `count(item)`: Menghitung berapa kali suatu item muncul.
-   `index(item, start, stop)`: Mencari indeks pertama item; mendukung batasan *start* dan *stop*.
-   `sorted(iterable, key, reverse)`: Mengembalikan *list* baru yang terurut dari *iterable* manapun.

### Perulangan (Loops) di Python
-   **`for` loop**: Digunakan untuk mengiterasi pada *sequence* (list, tuple, string) atau *iterable* lainnya.
    -   **Indentasi** blok kode adalah wajib.
    -   Dapat bersarang (*nested loops*).
-   **`while` loop**: Terus mengulang selama kondisi bernilai `True`.
-   **`break`**: Menghentikan eksekusi *loop* sepenuhnya.
-   **`continue`**: Melewati iterasi saat ini dan melanjutkan ke iterasi berikutnya dalam *loop*.
-   **`else` pada loop**: Blok `else` akan dijalankan jika *loop* selesai secara normal (tidak dihentikan oleh `break`).

### `range()`
-   **`range(start, stop, step)`**: Menghasilkan urutan bilangan bulat.
    -   `stop` adalah wajib dan bersifat eksklusif (tidak termasuk).
    -   `start` bersifat opsional (default 0).
    -   `step` bersifat opsional (default 1).
-   Hanya menerima *integer*; akan menimbulkan `TypeError` jika digunakan dengan *float* atau tanpa argumen `stop`.
-   *Step* negatif digunakan untuk urutan menurun.
-   Dapat dikombinasikan dengan `list()` untuk membuat *list integer*: `list(range(2, 11, 2))`.

### Fungsi `enumerate()` dan `zip()`
-   `enumerate(iterable, start=0)`: Mengembalikan objek *enumerate* yang menghasilkan pasangan (*indeks*, *nilai*) dari *iterable*.
-   `zip(*iterables)`: Menggabungkan elemen-elemen dari satu atau lebih *iterable* secara paralel menjadi *iterator of tuples*. Akan berhenti ketika *iterable* terpendek habis.

### List Comprehension
-   Sintaks ringkas untuk membuat *list* baru berdasarkan *iterable* yang sudah ada.
-   Format dasar: `[ekspresi for item in iterable if kondisi]`.
-   Contoh: `even_numbers = [num for num in range(21) if num % 2 == 0]`.

### Fungsi-Fungsi Berguna untuk List (dan Iterable Umum)
-   `filter(fungsi, iterable)`: Membangun *iterator* dari elemen *iterable* yang menghasilkan `True` ketika fungsi dipanggil.
-   `map(fungsi, iterable)`: Membangun *iterator* dari hasil penerapan fungsi pada setiap elemen *iterable*.
-   `sum(iterable, start=0)`: Menjumlahkan semua item dalam *iterable*, dengan nilai `start` opsional yang ditambahkan ke total.

### Fungsi Lambda
-   Fungsi anonim satu baris.
-   Sintaks: `lambda argumen: ekspresi`.
-   Berguna untuk ekspresi yang singkat dan sederhana, sering dilewatkan sebagai argumen ke fungsi *higher-order* seperti `map()` dan `filter()`.
-   Sebaiknya tidak ditugaskan ke variabel; gunakan `def` untuk fungsi bernama dan logika yang lebih kompleks.

---
Dengan memahami seluruh materi di atas, Anda telah memiliki dasar yang kuat tentang *list*, *tuple*, *range*, *loop*, serta berbagai fungsi pendukung di Python. Latihan secara konsisten akan membuat Anda semakin mahir.