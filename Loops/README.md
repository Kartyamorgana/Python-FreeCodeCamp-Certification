# Ulasan `Loops` dan `Sequences` di Python

## List di Python

**Pendahuluan**
Di Python, tipe data `list` adalah urutan elemen terurut yang *mutable* (dapat diubah) dan diindeks mulai dari nol. Elemen-elemennya bisa terdiri dari *string*, angka, atau bahkan `list` lain.

```python
cities = ['Los Angeles', 'London', 'Tokyo']
```

**Mengakses Elemen**
Elemen dalam `list` diakses menggunakan nomor indeksnya.

```python
cities[0]  # Output: 'Los Angeles'
```

**Mengakses Elemen dengan Indeks Negatif**
Indeks negatif memungkinkan akses dari akhir `list`. Indeks `-1`  mengakses elemen terakhir.

```python
cities[-1]  # Output: 'Tokyo'
```

**Membuat List dengan Konstruktor `list()`**
Konstruktor `list()` dapat mengubah *iterable* (seperti *string* atau *tuple*) menjadi sebuah `list`.

```python
developer = 'Jessica'
print(list(developer))  # Output: ['J', 'e', 's', 's', 'i', 'c', 'a']
```

**Mendapatkan Panjang List**
Fungsi `len()` digunakan untuk mendapatkan jumlah elemen dalam `list`.

```python
numbers = [1, 2, 3, 4, 5]
len(numbers)  # Output: 5
```

**Mutability List**
Karena `list` bersifat *mutable*, elemennya dapat diubah menggunakan indeks yang valid.

```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages)  # Output: ['JavaScript', 'Java', 'C++', 'Rust']
```

**`Index Out of Range Error`**
Mengakses indeks di luar jangkauan `list` (baik positif maupun negatif) akan menimbulkan `IndexError`.

```python
# programming_languages[10] = 'JavaScript'  # Ini akan menghasilkan IndexError
```

**Menghapus Elemen dari List**
Kata kunci `del` digunakan untuk menghapus elemen pada indeks tertentu.

```python
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer)  # Output: ['Jane Doe', 'Python Developer']
```

**Memeriksa Keberadaan Elemen**
Kata kunci `in` digunakan untuk memeriksa apakah suatu elemen ada dalam `list`.

```python
'Rust' in programming_languages       # Output: True
'JavaScript' in programming_languages # Output: False
```

**List Bersarang (*Nested List*)**
`List` dapat berisi `list` lain sebagai elemennya.

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2]       # Output: ['Python', 'Rust', 'C++']
developer[2][1]    # Output: 'Rust'
```

**Unpacking Nilai dari List**
Elemen dalam `list` dapat di-*unpack* ke variabel-variabel terpisah. Jumlah variabel harus sama dengan jumlah elemen `list`.

```python
developer_info = ['Alice', 34, 'Rust Developer']
name, age, job = developer_info
print(f"Name: {name}, Age: {age}, Job: {job}")
# Output: Name: Alice, Age: 34, Job: Rust Developer
```
Jika jumlah variabel tidak cocok dengan jumlah elemen `list`, akan muncul `ValueError`.

**Mengumpulkan Elemen Sisa**
Operator asterisk `*` dapat digunakan untuk mengumpulkan sisa elemen `list` ke dalam satu variabel baru (berupa `list`).

```python
name, *rest = developer_info
print(f"Name: {name}, Rest: {rest}")
# Output: Name: Alice, Rest: [34, 'Rust Developer']
```

***Slicing* List**
`Slicing` digunakan untuk mendapatkan potongan (`sub-list`) dari `list` menggunakan operator `:` ([`start:stop:step`]). Elemen pada indeks `stop` tidak akan disertakan.

```python
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie']
desserts[1:3]  # Output: ['Cookies', 'Ice Cream']
```

***Step Intervals***
Interval langkah (*step*) dalam `slicing` menentukan seberapa banyak indeks dilewati.

```python
numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2]  # Output: [2, 4, 6] (dimulai dari indeks 1, setiap 2 langkah)
```

### Metode List

*   **`append(element)`**: Menambahkan satu elemen ke akhir `list`.
    ```python
    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)
    print(numbers) # Output: [1, 2, 3, 4, 5, 6]

    # append akan menambahkan list sebagai satu elemen, bukan menggabungkan isinya
    even_numbers = [8, 10]
    numbers.append(even_numbers)
    print(numbers) # Output: [1, 2, 3, 4, 5, 6, [8, 10]]
    ```

*   **`extend(iterable)`**: Menambahkan semua elemen dari *iterable* lain ke akhir `list`, secara efektif menggabungkan *list*.
    ```python
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = [8, 10]
    numbers.extend(even_numbers)
    print(numbers) # Output: [1, 2, 3, 4, 5, 6, 8, 10]
    ```

*   **`insert(index, element)`**: Menyisipkan elemen pada indeks tertentu.
    ```python
    numbers = [1, 2, 3, 4, 5]
    numbers.insert(2, 2.5) # Sisipkan 2.5 pada indeks 2
    print(numbers) # Output: [1, 2, 2.5, 3, 4, 5]
    ```

*   **`remove(value)`**: Menghapus kemunculan pertama dari nilai tertentu. Jika nilai tidak ditemukan, akan terjadi `ValueError`.
    ```python
    numbers = [1, 5, 2, 5, 3]
    numbers.remove(5) # Menghapus angka 5 yang pertama ditemukan
    print(numbers) # Output: [1, 2, 5, 3]
    ```

*   **`pop(index=-1)`**: Menghapus dan mengembalikan elemen pada indeks tertentu. Jika `index` tidak ditentukan, elemen terakhir akan dihapus dan dikembalikan.
    ```python
    numbers = [1, 2, 3, 4, 5]
    popped_element_at_index_1 = numbers.pop(1)
    print(f"List setelah pop indeks 1: {numbers}, Elemen yang dihapus: {popped_element_at_index_1}")
    # Output: List setelah pop indeks 1: [1, 3, 4, 5], Elemen yang dihapus: 2

    popped_last_element = numbers.pop()
    print(f"List setelah pop terakhir: {numbers}, Elemen yang dihapus: {popped_last_element}")
    # Output: List setelah pop terakhir: [1, 3, 4], Elemen yang dihapus: 5
    ```

*   **`clear()`**: Mengosongkan seluruh `list`.
    ```python
    numbers = [1, 2, 3]
    numbers.clear()
    print(numbers) # Output: []
    ```

*   **`sort(key=None, reverse=False)`**: Mengurutkan `list` secara *in-place* (mengubah `list` asli).
    ```python
    numbers = [35, 1, 67, 19, 41, 2]
    numbers.sort()
    print(numbers) # Output: [1, 2, 19, 35, 41, 67]
    ```

*   **`sorted(iterable, key=None, reverse=False)`**: Mengembalikan `list` baru yang terurut dari *iterable* yang diberikan, tanpa mengubah *iterable* aslinya.
    ```python
    original_numbers = [35, 1, 67, 19, 41, 2]
    sorted_numbers = sorted(original_numbers)
    print(f"Original: {original_numbers}, Sorted: {sorted_numbers}")
    # Output: Original: [35, 1, 67, 19, 41, 2], Sorted: [1, 2, 19, 35, 41, 67]
    ```

*   **`reverse()`**: Membalik urutan elemen dalam `list` secara *in-place*.
    ```python
    numbers = [1, 2, 3, 4, 5, 6]
    numbers.reverse()
    print(numbers) # Output: [6, 5, 4, 3, 2, 1]
    ```

*   **`index(value, start=0, end=None)`**: Mencari indeks kemunculan pertama dari suatu nilai. Jika nilai tidak ditemukan, akan menghasilkan `ValueError`.
    ```python
    programming_languages = ['Python', 'Java', 'C++', 'Rust', 'Java']
    print(programming_languages.index('Java')) # Output: 1 (indeks pertama 'Java')
    ```

## Tuple di Python

**Definisi**
`Tuple` adalah urutan nilai terurut yang *immutable* (tidak dapat diubah). Mirip dengan `list`, `tuple` juga dapat berisi tipe data campuran.

```python
developer = ('Alice', 34, 'Rust Developer')
```
Mencoba mengubah elemen `tuple` akan menghasilkan `TypeError`.

**Mengakses Elemen**
Elemen `tuple` diakses menggunakan notasi kurung siku dengan indeks, sama seperti `list`.

```python
developer[1]   # Output: 34
numbers = (1, 2, 3, 4, 5)
numbers[-2]    # Output: 4
```
Indeks di luar jangkauan akan menghasilkan `IndexError`.

**Membuat Tuple dengan Konstruktor `tuple()`**
Konstruktor `tuple()` dapat mengubah *iterable* menjadi sebuah `tuple`.

```python
print(tuple('Jessica'))  # Output: ('J', 'e', 's', 's', 'i', 'c', 'a')
```

**Memeriksa Keberadaan Elemen**
Kata kunci `in` digunakan untuk memeriksa apakah suatu elemen ada dalam `tuple`.

```python
programming_languages_tuple = ('Python', 'Java', 'Rust')
'Rust' in programming_languages_tuple  # Output: True
```

**Unpacking dan Mengumpulkan Sisa**
Mekanisme *unpacking* dan penggunaan operator `*` untuk mengumpulkan sisa elemen bekerja sama persis seperti pada `list`.

```python
name, age, job = developer # Unpacking
print(f"Name: {name}, Age: {age}, Job: {job}")
# Output: Name: Alice, Age: 34, Job: Rust Developer

name, *rest = developer    # Mengumpulkan sisa
print(f"Name: {name}, Rest: {rest}")
# Output: Name: Alice, Rest: [34, 'Rust Developer']
```

***Slicing* Tuple**
`Slicing` pada `tuple` juga berfungsi sama seperti pada `list`, menghasilkan `tuple` baru.

```python
desserts_tuple = ('Cake', 'Cookies', 'Ice Cream', 'Pie')
desserts_tuple[1:3]  # Output: ('Cookies', 'Ice Cream')
```

**Menghapus Elemen**
Karena `tuple` bersifat *immutable*, elemen individual tidak dapat dihapus. Mencoba melakukannya akan menyebabkan `TypeError`. Namun, `tuple` secara keseluruhan dapat dihapus menggunakan `del`.

**Kapan Menggunakan Tuple vs List?**
*   **Gunakan `list`** jika koleksi elemen Anda perlu diubah-ubah (ditambah, dihapus, atau dimodifikasi).
*   **Gunakan `tuple`** jika data bersifat tetap, tidak boleh diubah setelah dibuat, dan untuk koleksi yang lebih kecil atau untuk mengelompokkan data terkait (misalnya, koordinat `(x, y)`). `Tuple` umumnya sedikit lebih cepat dan menggunakan memori lebih sedikit daripada `list`.

### Metode Tuple yang Umum

*   **`count(value)`**: Menghitung berapa kali suatu nilai muncul dalam `tuple`. Mengembalikan 0 jika nilai tidak ditemukan.
    ```python
    programming_languages_tuple = ('Python', 'Java', 'Rust', 'Python')
    programming_languages_tuple.count('Python')  # Output: 2
    programming_languages_tuple.count('Go')      # Output: 0
    ```

*   **`index(value, start=0, end=None)`**: Mencari indeks kemunculan pertama dari suatu nilai. `start` dan `end` dapat digunakan untuk membatasi pencarian. Jika nilai tidak ditemukan, akan menghasilkan `ValueError`.
    ```python
    programming_languages_tuple = ('Python', 'Java', 'C++', 'Python', 'Rust')
    print(programming_languages_tuple.index('Java'))           # Output: 1
    print(programming_languages_tuple.index('Python', 2))      # Output: 3 (mencari dari indeks 2)
    # print(programming_languages_tuple.index('Go'))           # Ini akan menghasilkan ValueError
    ```

*   **`sorted(iterable, key=None, reverse=False)`**: Mengembalikan `list` baru yang terurut dari elemen `tuple`, tanpa mengubah `tuple` asli.
    ```python
    numbers_tuple = (3, 1, 4, 1, 5, 9)
    print(sorted(numbers_tuple)) # Output: [1, 1, 3, 4, 5, 9]

    words = ('apple', 'banana', 'cat')
    print(sorted(words, key=len))             # Urut berdasarkan panjang kata: ['cat', 'apple', 'banana']
    print(sorted(words, reverse=True))        # Urut menurun: ['cat', 'banana', 'apple']
    ```

## Loop di Python

**Definisi**
*Loop* adalah konstruksi pemrograman yang memungkinkan blok kode dieksekusi secara berulang dalam jumlah tertentu atau selama kondisi tertentu terpenuhi.

### `for` Loop

`for` loop digunakan untuk mengiterasi melalui *sequence* atau *iterable* lainnya (seperti `list`, `tuple`, `string`, `dictionary`, atau objek lain yang dapat diiterasi).

```python
programming_languages_list = ['Python', 'Java', 'C++', 'Rust']
for language in programming_languages_list:
    print(language)
# Output:
# Python
# Java
# C++
# Rust
```
`for` loop juga dapat mengiterasi karakter dalam sebuah *string*.

```python
for char in 'code':
    print(char)
# Output:
# c
# o
# d
# e
```

**`Nested for loops` (*Loop* Bersarang)**
`for` loop dapat bersarang (satu `for` loop di dalam `for` loop lainnya) untuk iterasi multi-dimensi.

```python
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']
for category in categories:
    for food in foods:
        print(f"{category}: {food}")
# Output:
# Fruit: Apple
# Fruit: Carrot
# Fruit: Banana
# Vegetable: Apple
# Vegetable: Carrot
# Vegetable: Banana
```

### `while` Loop

`while` loop akan terus mengulang blok kode selama kondisi yang diberikan bernilai `True`. Loop akan berhenti ketika kondisi menjadi `False`.

```python
secret_number = 3
guess = 0
while guess != secret_number:
    try:
        guess = int(input('Guess the number (1-5): '))
        if guess != secret_number:
            print('Wrong! Try again.')
    except ValueError:
        print("Invalid input. Please enter a number.")
print('You got it!')
```

### Pernyataan `break` dan `continue`

*   **`break`**: Segera menghentikan eksekusi *loop* dan melanjutkan eksekusi kode setelah *loop*.
*   **`continue`**: Melompati sisa kode dalam iterasi saat ini dan langsung melanjutkan ke iterasi berikutnya dari *loop*.

```python
for num in range(1, 10):
    if num % 2 == 0:
        continue # Lewati angka genap
    if num == 7:
        break    # Hentikan loop jika angka 7 tercapai
    print(num)
# Output:
# 1
# 3
# 5
```

### `else` Clause pada Loop

Kedua jenis *loop* (`for` dan `while`) dapat memiliki klausa `else` (opsional). Blok kode di dalam `else` ini akan dieksekusi jika *loop* selesai secara normal (yaitu, tidak diinterupsi oleh pernyataan `break`).

```python
words = ["hello", "world", "rhythm", "sky"]

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break # Jika menemukan vokal, hentikan loop dalam untuk kata ini
    else: # Ini akan dijalankan jika loop dalam selesai tanpa 'break'
        print(f"'{word}' has no vowels")

# Output:
# 'hello' contains the vowel 'e'
# 'world' contains the vowel 'o'
# 'rhythm' has no vowels
# 'sky' has no vowels
```

## Ranges dan Penggunaannya dalam Loop

**Fungsi `range()`**
Fungsi `range()` digunakan untuk menghasilkan urutan bilangan bulat. Ini sering digunakan dalam `for` loop.

Sintaksnya adalah `range(start, stop, step)`:
*   `start` (opsional): Bilangan bulat awal (inklusif). Defaultnya 0.
*   `stop` (wajib): Bilangan bulat akhir (eksklusif). Urutan berhenti sebelum mencapai nilai ini.
*   `step` (opsional): Selisih antar angka (inkremental atau dekremental). Defaultnya 1.

Contoh penggunaan `range()`:
```python
# range(stop): Mulai dari 0 hingga stop-1
for num in range(3):
    print(num)    # Output: 0, 1, 2

# range(start, stop): Mulai dari start hingga stop-1
for num in range(2, 11, 2):
    print(num)    # Output: 2, 4, 6, 8, 10

# range(start, stop, step): Mundur dengan step negatif
for num in range(40, 0, -10):
    print(num)    # Output: 40, 30, 20, 10
```
Argument untuk `range()` harus berupa bilangan bulat; menggunakan *float* atau tipe data non-integer lainnya akan menyebabkan `TypeError`.

**Menggunakan `range()` dengan `list()`**
`range()` dapat digabungkan dengan `list()` untuk membuat `list` bilangan bulat.
```python
print(list(range(2, 11, 2)))  # Output: [2, 4, 6, 8, 10]
```

## Fungsi `enumerate()` dan `zip()`

### `enumerate()`

Fungsi `enumerate()` menambahkan penghitung ke sebuah *iterable* dan mengembalikannya sebagai objek `enumerate`. Objek `enumerate` ini dapat langsung digunakan dalam `for` loop untuk mengakses indeks dan nilai secara bersamaan.

```python
languages = ['Spanish', 'English', 'French']
for index, language in enumerate(languages):
    print(f'Index {index}: {language}')

# Output:
# Index 0: Spanish
# Index 1: English
# Index 2: French
```
`enumerate()` juga dapat digunakan di luar `for` loop untuk melihat outputnya:
```python
print(list(enumerate(languages)))
# Output: [(0, 'Spanish'), (1, 'English'), (2, 'French')]
```
Argumen opsional `start` dapat diberikan untuk memulai hitungan dari angka tertentu selain 0.
```python
for index, language in enumerate(languages, start=1):
    print(f'ID {index}: {language}')
# Output:
# ID 1: Spanish
# ID 2: English
# ID 3: French
```

### `zip()`

Fungsi `zip()` menggabungkan elemen dari beberapa *iterable* menjadi satu objek *iterator* `zip`. Setiap elemen dari objek `zip` adalah sebuah `tuple` yang berisi elemen yang sesuai dari *iterable* yang digabungkan.

```python
developers = ['Alice', 'Bob', 'Charlie']
ids = [101, 102, 103]

for name, dev_id in zip(developers, ids):
    print(f'Name: {name}, ID: {dev_id}')
# Output:
# Name: Alice, ID: 101
# Name: Bob, ID: 102
# Name: Charlie, ID: 103
```
`zip()` akan berhenti ketika *iterable* terpendek habis.

## List Comprehensions di Python

**Definisi**
*List comprehension* adalah cara ringkas dan ekspresif untuk membuat `list` baru di Python. Ini menyediakan sintaksis yang lebih pendek daripada `for` loop untuk membuat `list` berdasarkan `list` atau *iterable* lain.

Sintaks dasarnya adalah `[ekspresi for item in iterable if kondisi]`.

```python
# Membuat list bilangan genap dari 0 hingga 20
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## Metode Iterable

### `filter(function, iterable)`

Fungsi `filter()` menyaring elemen dari sebuah *iterable* berdasarkan kondisi yang ditentukan oleh sebuah fungsi. Fungsi ini mengembalikan sebuah *iterator* yang hanya berisi elemen-elemen yang membuat fungsi kondisi mengembalikan `True`.

```python
words = ['apple', 'banana', 'cat', 'dogfood', 'elephant']

def is_long_word(word):
    return len(word) > 4

long_words_iterator = filter(is_long_word, words)
long_words = list(long_words_iterator) # Konversi iterator ke list
print(long_words)
# Output: ['apple', 'banana', 'dogfood', 'elephant']
```

### `map(function, iterable, ...)`

Fungsi `map()` menerapkan fungsi yang diberikan ke setiap item dalam *iterable* dan mengembalikan *iterator* dari hasil tersebut.

```python
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp_c):
    return (temp_c * 9/5) + 32

fahrenheit_iterator = map(to_fahrenheit, celsius)
fahrenheit = list(fahrenheit_iterator) # Konversi iterator ke list
print(fahrenheit)
# Output: [32.0, 50.0, 68.0, 86.0, 104.0]
```

### `sum(iterable, start=0)`

Fungsi `sum()` menghitung jumlah semua item dalam *iterable* yang diberikan.

```python
numbers_to_sum = [10, 20, 30]
print(sum(numbers_to_sum))          # Output: 60 (default start=0)
print(sum(numbers_to_sum, 10))      # Output: 70 (dengan start=10)
print(sum(numbers_to_sum, start=10))# Output: 70 (menggunakan keyword argument untuk start)
```

## Fungsi Lambda

**Definisi**
Fungsi `lambda` adalah fungsi anonim (tanpa nama) yang ringkas. Fungsi ini dapat didefinisikan dalam satu baris kode dan sering digunakan sebagai argumen untuk fungsi tingkat tinggi lainnya seperti `map()`, `filter()`, dan `sorted()`.

Sintaksnya adalah `lambda arguments: expression`.

```python
numbers_for_lambda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Menggunakan lambda dengan filter untuk mendapatkan bilangan genap
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers_for_lambda))
print(even_numbers_lambda)
# Output: [2, 4, 6, 8, 10]

# Menggunakan lambda dengan map untuk mengkuadratkan setiap angka
squared_numbers = list(map(lambda x: x**2, numbers_for_lambda))
print(squared_numbers)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**Praktik Terbaik dalam Penggunaan Lambda:**
*   **Jangan menetapkan lambda ke variabel:** Meskipun secara teknis bisa, ini menghilangkan tujuan fungsi anonim dan lebih baik menggunakan fungsi `def` biasa untuk keterbacaan.
*   **Jaga agar sederhana dan mudah dibaca:** Lambda paling baik untuk ekspresi satu baris yang mudah dipahami.
*   **Gunakan hanya untuk fungsi pendek yang sekali pakai:** Jika fungsi Anda menjadi kompleks atau Anda perlu menggunakannya di lebih dari satu tempat, definisikan sebagai fungsi bernama (`def`).