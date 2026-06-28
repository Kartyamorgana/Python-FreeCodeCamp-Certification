# Daftar Isi

- [### Apa Itu Dictionary dan Bagaimana Cara Kerjanya?](#apa-itu-dictionary-dan-bagaimana-cara-kerjanya)
  - [Sintaks Dasar Dictionary](#sintaks-dasar-dictionary)
  - [Membuat Dictionary dengan Konstruktor `dict()`](#membuat-dictionary-dengan-konstruktor-dict)
  - [Mengakses dan Memperbarui Nilai](#mengakses-dan-memperbarui-nilai)
- [### Metode-Metode Penting pada Dictionary](#metode-metode-penting-pada-dictionary)
  - [`get()` – Mengambil Nilai dengan Nilai Default](#get--mengambil-nilai-dengan-nilai-default)
  - [`keys()` dan `values()` – Melihat Semua Kunci dan Nilai](#keys-dan-values--melihat-semua-kunci-dan-nilai)
  - [`items()` – Melihat Pasangan Kunci-Nilai](#items--melihat-pasangan-kunci-nilai)
  - [`clear()` – Menghapus Semua Isi](#clear--menghapus-semua-isi)
  - [`pop()` – Menghapus dan Mengembalikan Nilai](#pop--menghapus-dan-mengembalikan-nilai)
  - [`popitem()` – Menghapus Item Terakhir yang Disisipkan](#popitem--menghapus-item-terakhir-yang-disisipkan)
  - [`update()` – Memperbarui/Menambah Banyak Pasangan Sekaligus](#update--memperbaruimenambah-banyak-pasangan-sekaligus)
- [### Teknik Umum untuk Melakukan Perulangan (*Loop*) pada Dictionary](#teknik-umum-untuk-melakukan-perulangan-loop-pada-dictionary)
  - [Iterasi Hanya Nilai](#iterasi-hanya-nilai)
  - [Iterasi Hanya Kunci](#iterasi-hanya-kunci)
  - [Iterasi Pasangan Kunci-Nilai](#iterasi-pasangan-kunci-nilai)
  - [Contoh Praktis: Diskon 20%](#contoh-praktis-diskon-20)
  - [Menggunakan `enumerate()` untuk Mendapatkan Penghitung (*Counter*)](#menggunakan-enumerate-untuk-mendapatkan-penghitung-counter)
- [### Apa Itu Set dan Bagaimana Cara Kerjanya?](#apa-itu-set-dan-bagaimana-cara-kerjanya)
  - [Mendefinisikan Set](#mendefinisikan-set)
  - [Menambah Elemen – `add()`](#menambah-elemen--add)
  - [Menghapus Elemen – `remove()` dan `discard()`](#menghapus-elemen--remove-dan-discard)
  - [Menghapus Semua Elemen – `clear()`](#menghapus-semua-elemen--clear)
- [### Operasi Himpunan Matematika pada Set](#operasi-himpunan-matematika-pada-set)
  - [Subset dan Superset](#subset-dan-superset)
  - [Disjoint (Saling Lepas) – `isdisjoint()`](#disjoint-saling-lepas--isdisjoint)
  - [Union (Gabungan) – Operator `|` atau Metode `union()`](#union-gabungan--operator--atau-metode-union)
  - [Intersection (Irisan) – Operator `&` atau Metode `intersection()`](#intersection-irisan--operator--atau-metode-intersection)
  - [Difference (Selisih) – Operator `-` atau Metode `difference()`](#difference-selisih--operator---atau-metode-difference)
  - [Symmetric Difference (Beda Setangkup) – Operator `^` atau Metode `symmetric_difference()`](#symmetric-difference-beda-setangkup--operator--atau-metode-symmetric_difference)
  - [Operator Penugasan Majemuk (*Compound Assignment*)](#operator-penugasan-majemuk-compound-assignment)
  - [Memeriksa Keanggotaan dengan `in`](#memeriksa-keanggotaan-dengan-in)
- [### Pustaka Standar Python dan Cara Mengimpor Modul](#pustaka-standar-python-dan-cara-mengimpor-modul)
  - [Pernyataan `import`](#pernyataan-import)
  - [Memberikan Alias pada Modul](#memberikan-alias-pada-modul)
  - [Mengimpor Elemen Tertentu](#mengimpor-elemen-tertentu)
  - [Mengimpor Semua Isi Modul dengan Asterisk `*`](#mengimpor-semua-isi-modul-dengan-asterisk-)
  - [Mengimpor Konstanta dan Kelas](#mengimpor-konstanta-dan-kelas)
- [### Idiom Penting: `if __name__ == '__main__'`](#idiom-penting-if-__name__--__main__)
- [## Rangkuman: Dictionary dan Set](#rangkuman-dictionary-dan-set)
  - [### Dictionary](#dictionary)
  - [### Set](#set)
  - [### Pustaka Standar dan `import`](#pustaka-standar-dan-import)

---

### Apa Itu Dictionary dan Bagaimana Cara Kerjanya?

Dictionary dalam Python adalah struktur data bawaan yang menyimpan koleksi pasangan **kunci-nilai** (*key-value pairs*). Cara kerjanya sangat mirip dengan kamus sungguhan: Anda mencari sebuah kata (kunci) untuk menemukan maknanya (nilai).

Dengan dictionary Python, Anda menggunakan **kunci** untuk mendapatkan **nilai** yang terkait. Gunakan dictionary ketika Anda perlu:
* Mengasosiasikan nilai dengan kunci yang unik.
* Mencari nilai dengan cepat berdasarkan kuncinya.
* Merepresentasikan data yang terstruktur.

#### Sintaks Dasar Dictionary

```python
dictionary = {
    key1: value1,
    key2: value2
}
```

*   Variabel di sisi kiri menampung objek dictionary. (Menyimpan dictionary di variabel sangat umum agar tetap ada di memori dan bisa digunakan lagi.)
*   Kurung kurawal `{}` membungkus seluruh pasangan kunci-nilai.
*   Setiap kunci dipisahkan dari nilainya oleh tanda titik dua `:`.
*   Antar pasangan dipisahkan oleh koma `,` (kecuali setelah pasangan terakhir, koma boleh ada atau tidak).
*   **Kunci harus unik** dalam satu dictionary, dan harus bertipe data *immutable* (tidak dapat diubah, misalnya string, angka, tuple). Nilai boleh duplikat dan bisa bertipe data apa pun.

**Contoh** dictionary yang menyimpan informasi resep *Margherita Pizza*:

```python
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}
```

Dictionary ini memiliki empat pasangan kunci-nilai: `'name'`, `'price'`, `'calories_per_slice'`, dan `'toppings'`.

#### Membuat Dictionary dengan Konstruktor `dict()`

Alternatif lain adalah menggunakan konstruktor `dict()`, yang membangun dictionary dari urutan pasangan kunci-nilai.

Sintaks ekuivalen untuk contoh pizza di atas:

```python
pizza = dict([
    ('name', 'Margherita Pizza'),
    ('price', 8.9),
    ('calories_per_slice', 250),
    ('toppings', ['mozzarella', 'basil'])
])
```

Kita memberikan daftar (*list*) yang berisi *tuple*. Setiap tuple memiliki kunci sebagai elemen pertama dan nilai sebagai elemen kedua.

#### Mengakses dan Memperbarui Nilai

Untuk mengakses nilai dari suatu pasangan, gunakan notasi kurung siku (*bracket notation*):

```python
dictionary[key]
```

*   Tulis nama variabel dictionary, diikuti sepasang kurung siku `[]`, dan di dalamnya kunci yang ingin diakses.

**Contoh**:

```python
print(pizza['name'])
# Output: Margherita Pizza
```

Ekspresi ini akan menghasilkan `'Margherita Pizza'`.

**Memperbarui nilai** cukup dengan menggunakan operator penugasan `=` diikuti nilai baru:

```python
pizza['name'] = 'Margherita'
print(pizza['name'])
# Output: Margherita
```

Sekarang nilai dari kunci `'name'` telah berubah menjadi `'Margherita'`.

> **Catatan**: Jika kunci yang ditulis belum ada di dictionary, maka sebuah pasangan kunci-nilai baru akan ditambahkan. Mulai Python versi 3.7, dictionary mempertahankan urutan penyisipan (*insertion order*), yang membantu saat Anda perlu melakukan iterasi.

---

### Metode-Metode Penting pada Dictionary

Dictionary memiliki beragam metode bawaan untuk operasi sehari-hari.

#### `get()` – Mengambil Nilai dengan Nilai Default

Metode `.get()` mengambil nilai yang terkait dengan suatu kunci. Ia mirip dengan notasi kurung siku, namun memiliki keuntungan: Anda dapat menetapkan **nilai default** sehingga tidak muncul error jika kunci tidak ditemukan.

```python
dictionary.get(key, default)
```

**Contoh**:

```python
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

print(pizza.get('toppings', []))   # Output: ['mozzarella', 'basil']
print(pizza.get('crust_type', 'thin')) # Output: thin
```

Jika `'toppings'` ada, metode akan mengembalikan daftar aslinya. Jika `'crust_type'` tidak ada, ia akan mengembalikan `thin` (nilai default yang diberikan).

#### `keys()` dan `values()` – Melihat Semua Kunci dan Nilai

Metode `keys()` mengembalikan *view object* (objek tampilan) yang berisi seluruh kunci dictionary.
Metode `values()` mengembalikan *view object* yang berisi seluruh nilai dictionary.

*View object* hanyalah cara untuk melihat isi dictionary tanpa membuat salinan data terpisah. Ini berarti jika dictionary berubah, *view object* juga akan mencerminkan perubahan tersebut secara *real-time*.

```python
print(pizza.keys())
# Output: dict_keys(['name', 'price', 'calories_per_slice', 'toppings'])

print(pizza.values())
# Output: dict_values(['Margherita Pizza', 8.9, 250, ['mozzarella', 'basil']])
```

#### `items()` – Melihat Pasangan Kunci-Nilai

Mengembalikan *view object* berisi semua pasangan (kunci, nilai) sebagai tuple.

```python
print(pizza.items())
# Output: dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
```

#### `clear()` – Menghapus Semua Isi

Menghapus seluruh pasangan kunci-nilai dari dictionary.

```python
pizza.clear()
print(pizza)
# Output: {}
```

#### `pop()` – Menghapus dan Mengembalikan Nilai

```python
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250
}

# Menghapus 'price' dan mengembalikan nilainya
print(pizza.pop('price'))      # Output: 8.9
print(pizza)                   # Output: {'name': 'Margherita Pizza', 'calories_per_slice': 250}

# Menghapus 'total_price' (tidak ada), mengembalikan nilai default 10
print(pizza.pop('total_price', 10)) # Output: 10
print(pizza)                        # Output: {'name': 'Margherita Pizza', 'calories_per_slice': 250}

# Jika kunci tidak ada dan tidak disertakan default, Python akan melempar KeyError
# pizza.pop('non_existent_key') # Ini akan menyebabkan KeyError
```

*   Argumen pertama: kunci yang akan dihapus.
*   Argumen kedua (opsional): nilai default yang dikembalikan jika kunci tidak ditemukan.
*   Jika kunci tidak ada dan tidak disertakan default, Python akan melempar `KeyError`.

#### `popitem()` – Menghapus Item Terakhir yang Disisipkan

Sejak Python 3.7, dictionary mempertahankan urutan penyisipan. `.popitem()` akan menghapus pasangan yang **terakhir dimasukkan** dan mengembalikannya sebagai tuple.

```python
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250
}

print(pizza.popitem())
# Output: ('calories_per_slice', 250)
print(pizza)
# Output: {'name': 'Margherita Pizza', 'price': 8.9}
```

#### `update()` – Memperbarui/Menambah Banyak Pasangan Sekaligus

Metode `update()` digunakan untuk memperbarui dictionary dengan pasangan kunci-nilai dari dictionary atau iterable lain.

```python
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

pizza.update({'price': 15, 'total_time': 25})
print(pizza)
```

Setelah operasi di atas, dictionary `pizza` menjadi:

```
{
    'name': 'Margherita Pizza',
    'price': 15,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil'],
    'total_time': 25
}
```

*   Jika kunci sudah ada (misalnya `'price'`), nilainya akan **ditimpa**.
*   Jika kunci baru (misalnya `'total_time'`), maka pasangan tersebut **ditambahkan**.

---

### Teknik Umum untuk Melakukan Perulangan (*Loop*) pada Dictionary

Anda dapat melakukan perulangan pada dictionary untuk mengakses dan memproses pasangan kunci-nilai. Hal ini berguna saat memperbarui nilai atau menerapkan logika tertentu.

Misalkan kita memiliki dictionary `products` yang memetakan produk ke harganya:

```python
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
```

#### Iterasi Hanya Nilai

Gunakan `products.values()` di dalam `for` loop:

```python
for price in products.values():
    print(price)
```

**Keluaran**:

```
990
600
250
70
```

#### Iterasi Hanya Kunci

Gunakan `products.keys()` atau langsung iterasi pada objek dictionary karena secara default iterasi akan melalui kuncinya:

```python
for product_name in products.keys():
    print(product_name)

# atau

for product_name in products: # Default iterasi pada dictionary adalah kuncinya
    print(product_name)
```

**Keluaran**:

```
Laptop
Smartphone
Tablet
Headphones
```

#### Iterasi Pasangan Kunci-Nilai

Gunakan `products.items()`. Setiap iterasi menghasilkan tuple `(kunci, nilai)`:

```python
for item_tuple in products.items():
    print(item_tuple)
```

**Keluaran**:

```
('Laptop', 990)
('Smartphone', 600)
('Tablet', 250)
('Headphones', 70)
```

Jika Anda ingin memisahkan kunci dan nilai ke dalam dua variabel loop terpisah, gunakan *unpacking* tuple:

```python
for product_name, price_value in products.items():
    print(f"{product_name}: ${price_value}")
```

**Keluaran**:

```
Laptop: $990
Smartphone: $600
Tablet: $250
Headphones: $70
```

> **Urutan variabel penting**: variabel pertama menampung kunci, variabel kedua menampung nilai.

#### Contoh Praktis: Diskon 20%

Kita bisa memperbarui semua harga dengan diskon 20% (mengalikan dengan 0.8) dan membulatkannya. Perhatikan bahwa Anda perlu mengakses dictionary berdasarkan kunci untuk memperbarui nilai.

```python
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product_name, price_value in products.items():
    products[product_name] = round(price_value * 0.8)

print(products)
```

**Keluaran**:

```
{
    'Laptop': 792,
    'Smartphone': 480,
    'Tablet': 200,
    'Headphones': 56
}
```

#### Menggunakan `enumerate()` untuk Mendapatkan Penghitung (*Counter*)

Fungsi `enumerate()` mengembalikan objek enumerate yang memberikan bilangan bulat (seperti indeks atau counter) untuk setiap elemen yang diiterasi. Secara default, counter dimulai dari 0.

Ketika digunakan langsung pada dictionary, `enumerate()` akan mengiterasi kuncinya:

```python
for count, product_name in enumerate(products):
    print(count, product_name)
```

**Keluaran**:

```
0 Laptop
1 Smartphone
2 Tablet
3 Headphones
```

Untuk nilai-nilai, gunakan `products.values()`:

```python
for count, price_value in enumerate(products.values()):
    print(count, price_value)
```

**Keluaran**:

```
0 990
1 600
2 250
3 70
```

Untuk pasangan kunci-nilai, gunakan `products.items()`:

```python
for count, item_tuple in enumerate(products.items()):
    print(count, item_tuple)
```

**Keluaran**:

```
0 ('Laptop', 990)
1 ('Smartphone', 600)
2 ('Tablet', 250)
3 ('Headphones', 70)
```

Anda juga bisa membongkar counter bersamaan dengan kunci dan nilai:

```python
for count, (product_name, price_value) in enumerate(products.items()):
    print(f"{count+1}. {product_name}: ${price_value}") # +1 agar dimulai dari 1
```

**Keluaran**:

```
1. Laptop: $990
2. Smartphone: $600
3. Tablet: $250
4. Headphones: $70
```

**Menentukan Nilai Awal Counter**: Berikan argumen kedua pada `enumerate()`.

```python
for count, (product_name, price_value) in enumerate(products.items(), 1):
    print(f"{count}. Item: {product_name}, Price: ${price_value}")
```

Sekarang counter dimulai dari 1:

```
1. Item: Laptop, Price: $990
2. Item: Smartphone, Price: $600
3. Item: Tablet, Price: $250
4. Item: Headphones, Price: $70
```

Teknik ini berlaku untuk semua variasi iterasi yang telah kita lihat.

---

### Apa Itu Set dan Bagaimana Cara Kerjanya?

**Set** (himpunan) adalah struktur data bawaan Python yang **tidak menyimpan nilai duplikat**. Jika Anda mencoba menambahkan nilai yang sudah ada, set akan secara otomatis mengabaikannya dan hanya satu instance yang akan disimpan.

Karakteristik utama set:

*   **Mutable** (dapat diubah): Anda bisa menambah atau menghapus elemen. Namun, elemen-elemennya sendiri harus bertipe *immutable* (misalnya angka, string, tuple). List atau dictionary tidak bisa menjadi elemen set.
*   **Unordered** (tidak berurutan): elemen tidak disimpan dalam urutan tertentu, sehingga Anda tidak bisa mengakses elemen menggunakan indeks (misalnya `my_set[0]`) atau kunci.
*   Mendukung operasi himpunan matematika: *union*, *intersection*, *difference*, *symmetric difference*.

#### Mendefinisikan Set

Tulis elemen-elemennya di dalam kurung kurawal `{}`, dipisahkan oleh koma.

```python
my_set = {1, 2, 3, 4, 5}
print(my_set)
# Output: {1, 2, 3, 4, 5} (urutan mungkin berbeda)

# Jika ada duplikat, hanya satu yang disimpan
duplicate_set = {1, 2, 2, 3, 1}
print(duplicate_set)
# Output: {1, 2, 3}
```

**Catatan khusus untuk set kosong**:
Jika Anda menulis `{}`, Python akan membuat **dictionary kosong**, bukan set kosong. Untuk membuat set kosong, gunakan fungsi `set()`.

```python
empty_set = set()   # Ini adalah set kosong
empty_dict = {}     # Ini adalah dictionary kosong

print(type(empty_set))  # Output: <class 'set'>
print(type(empty_dict)) # Output: <class 'dict'>
```

#### Menambah Elemen – `add()`

Gunakan metode `.add()` untuk menambahkan satu elemen ke set.

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
# Output: {1, 2, 3, 4}

# Jika elemen sudah ada, set tidak berubah
my_set.add(3)
print(my_set)
# Output: {1, 2, 3, 4}
```

#### Menghapus Elemen – `remove()` dan `discard()`

*   `.remove(elemen)`: menghapus elemen yang ditentukan. **Melempar `KeyError` jika elemen tidak ditemukan** di dalam set.
*   `.discard(elemen)`: menghapus elemen yang ditentukan. **Tidak error** jika elemen tidak ada di dalam set.

```python
my_set = {1, 2, 3, 4, 5}

my_set.remove(4)
print(my_set)
# Output: {1, 2, 3, 5}

my_set.discard(4) # Aman meskipun 4 sudah tidak ada
print(my_set)
# Output: {1, 2, 3, 5}

# Ini akan melempar KeyError karena 9 tidak ada
# my_set.remove(9)
```

#### Menghapus Semua Elemen – `clear()`

Metode `clear()` menghapus seluruh elemen dari set, menjadikannya set kosong.

```python
my_set = {1, 2, 3}
my_set.clear()
print(my_set)
# Output: set()
```

---

### Operasi Himpunan Matematika pada Set

Python menyediakan metode dan operator untuk melakukan operasi himpunan (set operations) layaknya dalam matematika.

Misalkan kita punya dua set:
```python
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4, 6, 7}
```

#### Subset dan Superset

*   `issubset(other_set)`: Mengembalikan `True` jika semua elemen dari set saat ini ada di `other_set`.
*   `issuperset(other_set)`: Mengembalikan `True` jika semua elemen dari `other_set` ada di set saat ini.

```python
print(set_a.issubset(set_b))    # Output: False (karena 1 dan 5 tidak ada di set_b)
print(set_b.issuperset(set_a))  # Output: False (set_b tidak memuat semua elemen set_a)
```

**Contoh bernilai `True`**:

```python
set_x = {1, 2}
set_y = {1, 2, 3}
print(set_x.issubset(set_y))   # Output: True
print(set_y.issuperset(set_x)) # Output: True
```

#### Disjoint (Saling Lepas) – `isdisjoint()`

Mengembalikan `True` jika kedua set tidak memiliki elemen yang sama (irisannya kosong).

```python
set_c = {1, 2, 3}
set_d = {4, 5, 6}
print(set_c.isdisjoint(set_d))  # Output: True

set_e = {1, 2}
set_f = {2, 3}
print(set_e.isdisjoint(set_f))  # Output: False (karena ada elemen 2 yang sama)
```

#### Union (Gabungan) – Operator `|` atau Metode `union()`

Menghasilkan set baru berisi semua elemen unik dari kedua set (gabungan).

```python
print(set_a | set_b)          # Output: {1, 2, 3, 4, 5, 6, 7}
print(set_a.union(set_b))     # Output: {1, 2, 3, 4, 5, 6, 7}
```

#### Intersection (Irisan) – Operator `&` atau Metode `intersection()`

Menghasilkan set baru berisi elemen yang ada di **kedua** set.

```python
print(set_a & set_b)                # Output: {2, 3, 4}
print(set_a.intersection(set_b))    # Output: {2, 3, 4}
```

#### Difference (Selisih) – Operator `-` atau Metode `difference()`

Menghasilkan set baru berisi elemen yang ada di set pertama tetapi **tidak** ada di set kedua.

```python
print(set_a - set_b)                # Output: {1, 5} (elemen di set_a yang tidak ada di set_b)
print(set_b - set_a)                # Output: {6, 7} (elemen di set_b yang tidak ada di set_a)
print(set_a.difference(set_b))      # Output: {1, 5}
```

#### Symmetric Difference (Beda Setangkup) – Operator `^` atau Metode `symmetric_difference()`

Menghasilkan set baru berisi elemen yang hanya ada di salah satu set, tetapi tidak di keduanya (gabungan dikurangi irisan).

```python
print(set_a ^ set_b)                                # Output: {1, 5, 6, 7}
print(set_a.symmetric_difference(set_b))            # Output: {1, 5, 6, 7}
```

#### Operator Penugasan Majemuk (*Compound Assignment*)

Setiap operator di atas memiliki versi penugasan majemuk (misalnya `|=`, `&=`, `-=`, `^=`). Versi ini langsung memodifikasi set di sisi kiri dengan hasil operasi, tanpa membuat set baru.

```python
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4, 6, 7}

set_a -= set_b # Sama dengan set_a = set_a - set_b
print(set_a)   # Output: {1, 5}
```

#### Memeriksa Keanggotaan dengan `in`

Anda dapat menggunakan operator `in` untuk memeriksa apakah suatu elemen adalah anggota dari set.

```python
my_set = {1, 2, 3}
print(2 in my_set)   # Output: True
print(5 in my_set)   # Output: False
```

---

### Pustaka Standar Python dan Cara Mengimpor Modul

Dalam pengembangan perangkat lunak, **pustaka** (*library*) dan **modul** ibarat kotak perkakas yang penuh peralatan. Alih-alih menulis semua kode dari nol, pustaka menyediakan kode yang sudah jadi dan dapat digunakan kembali, seperti fungsi, kelas, dan struktur data. Modul adalah satu berkas `.py` yang berisi definisi-definisi tersebut.

Python memiliki **pustaka standar** yang sangat luas, berisi modul-modul bawaan yang telah teruji untuk berbagai kebutuhan, misalnya:

*   Berinteraksi dengan sistem operasi (`os`, `sys`).
*   Bekerja dengan berkas (`io`, `pathlib`).
*   Jaringan (`socket`, `http`).
*   Tanggal dan waktu (`datetime`, `time`).
*   Operasi matematika (`math`, `decimal`).
*   Ekspresi reguler (`re`).
*   Pengujian dan debugging (`unittest`, `pdb`).
*   Dan masih banyak lagi.

**Contoh** modul bawaan yang populer:

*   `math` – fungsi matematika lanjutan (akar kuadrat, trigonometri, dll.).
*   `random` – menghasilkan angka acak.
*   `re` – bekerja dengan ekspresi reguler.
*   `datetime` – bekerja dengan tanggal dan waktu.

#### Pernyataan `import`

Untuk mengakses variabel, konstanta, fungsi, atau kelas yang didefinisikan dalam modul, gunakan pernyataan `import`. Pernyataan ini biasanya ditulis di bagian atas berkas Python.

**Bentuk paling dasar**:

```python
import module_name
```

Setelah diimpor, Anda dapat memanggil fungsi atau mengakses atribut modul dengan notasi titik:

```python
module_name.function_name()
module_name.variable_name
```

**Contoh**: menghitung akar kuadrat dari 36 menggunakan modul `math`.

```python
import math
result = math.sqrt(36)
print(result) # Output: 6.0
```

#### Memberikan Alias pada Modul

Gunakan kata kunci `as` untuk memberi nama alias (nama panggilan) pada modul. Ini sering dipakai untuk menyingkat nama modul yang panjang atau menghindari konflik penamaan jika ada beberapa modul dengan nama yang serupa.

```python
import math as m
result = m.sqrt(36)
print(result) # Output: 6.0
```

#### Mengimpor Elemen Tertentu

Jika Anda hanya membutuhkan beberapa fungsi atau kelas dari sebuah modul, gunakan sintaks `from ... import ...`.

```python
from module_name import name1, name2
```

Dengan cara ini, Anda bisa langsung memanggil `name1` atau `name2` tanpa awalan modul.

**Contoh**: hanya mengimpor `radians`, `sin`, dan `cos` dari `math`.

```python
from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees) # Tidak perlu math.radians()

sine_value = sin(angle_radians)        # Tidak perlu math.sin()
cos_value = cos(angle_radians)         # Tidak perlu math.cos()

print(sine_value)  # Output: 0.6427876096865393
print(cos_value)   # Output: 0.766044443118978
```

Anda juga bisa memberikan alias pada elemen yang diimpor:

```python
from math import radians as rad, sin as s, cos as c

angle_degrees = 40
angle_radians = rad(angle_degrees)
print(s(angle_radians))
print(c(angle_radians))
```

> **Peringatan**: Mengimpor elemen satu per satu seperti ini dapat menyebabkan konflik nama jika sudah ada fungsi atau variabel dengan nama yang sama di skrip Anda. Pertimbangkan jenis impor yang paling sesuai untuk kejelasan dan menghindari konflik.

#### Mengimpor Semua Isi Modul dengan Asterisk `*`

```python
from module_name import *
```

Artinya: impor semua nama (fungsi, kelas, variabel) dari modul, dan jadikan tersedia langsung di *namespace* saat ini tanpa awalan modul.

```python
from math import *
print(sqrt(36))   # Output: 6.0
print(pow(5, 2))  # Output: 25.0
print(exp(1))     # Output: 2.718281828459045
```

> **Tidak disarankan** untuk penggunaan umum, terutama dalam proyek besar atau modul, karena dapat menyebabkan *namespace collision* (bentrokan nama) dan menyulitkan pelacakan asal-usul suatu nama (misalnya, dari modul mana `sqrt` berasal?). Ini lebih sering digunakan dalam skrip kecil atau saat *interactive shell*.

#### Mengimpor Konstanta dan Kelas

Pernyataan `import` berlaku sama untuk konstanta, kelas, dan elemen lainnya yang didefinisikan dalam modul.

**Contoh konstanta `pi`**:

```python
import math
print(math.pi)   # Output: 3.141592653589793
```

**Contoh kelas `date` dari modul `datetime`**:

```python
import datetime
# Membuat objek tanggal dengan tahun, bulan, hari
birthday = datetime.date(1959, 7, 15)
print(birthday.day)    # Output: 15
print(birthday.month)  # Output: 7
print(birthday.year)   # Output: 1959
```

Informasi lebih lengkap mengenai modul dapat ditemukan di dokumentasi resmi Python.

---

### Idiom Penting: `if __name__ == '__main__'`

`__name__` adalah variabel bawaan khusus di Python yang secara otomatis diatur oleh interpreter.

*   Ketika sebuah berkas Python **dijalankan langsung** (misalnya `python myscript.py`), Python mengatur nilai variabel `__name__` menjadi string `"`__main__`"`.
*   Jika berkas tersebut **diimpor sebagai modul** ke skrip lain (misalnya `import myscript`), nilai `__name__` akan berisi nama modul tersebut (biasanya nama berkas tanpa ekstensi `.py`, seperti `"myscript"`).

Oleh karena itu, Anda akan sering menemukan kondisi berikut dalam skrip Python:

```python
if __name__ == '__main__':
    # Kode di sini hanya akan dijalankan saat skrip ini dieksekusi sebagai program utama.
    print("Saya berjalan sebagai skrip utama!")
    # Panggil fungsi atau jalankan logika utama aplikasi di sini
    main_function()
else:
    # Kode di sini akan dijalankan jika skrip ini diimpor sebagai modul.
    print("Saya diimpor sebagai modul.")

def main_function():
    print("Fungsi utama telah dijalankan.")
```

Kode di dalam blok `if __name__ == '__main__':` hanya akan dieksekusi jika skrip dijalankan secara langsung. Jika skrip diimpor sebagai modul, blok tersebut tidak akan dijalankan, melainkan blok `else` (jika ada) atau kode di luar `if`.

Pola ini memungkinkan sebuah berkas Python memiliki dua tujuan: bisa dijalankan langsung untuk logika utamanya, atau diimpor sebagai modul untuk menyediakan fungsi atau kelas tanpa secara otomatis menjalankan logika utama di dalamnya. Ini adalah praktik terbaik untuk membuat kode Python yang *reusable* (dapat digunakan kembali).

---

## Rangkuman: Dictionary dan Set

### Dictionary

*   **Dictionary**: Struktur data bawaan yang menyimpan koleksi pasangan kunci-nilai. Kunci harus unik dan bertipe *immutable*.
*   **Sintaks umum**:
    ```python
    my_dict = {
        key1: value1,
        key2: value2
    }
    ```
*   **Konstruktor `dict()`**: Cara alternatif membangun dictionary dari iterable pasangan (*tuple* atau *list* dari *list*).
    ```python
    another_dict = dict([('key_a', 1), ('key_b', 2)])
    ```
*   **Akses dan Perbarui**: Menggunakan notasi kurung siku `my_dict[key]`. Jika kunci tidak ada saat mengakses, akan melempar `KeyError`. Saat memperbarui, akan menambah jika kunci baru atau menimpa nilai jika kunci sudah ada.

#### Metode-Metode Penting Dictionary (Ringkasan)

| Metode | Deskripsi |
| :----- | :------------------------------------------------------ |
| `get(key, default)` | Mengambil nilai untuk `key`. Jika `key` tidak ada, kembalikan `default` (jika diberikan) atau `None`. |
| `keys()` | Mengembalikan *view object* dari semua kunci. |
| `values()` | Mengembalikan *view object* dari semua nilai. |
| `items()` | Mengembalikan *view object* dari semua pasangan (kunci, nilai) sebagai tuple. |
| `clear()` | Menghapus semua pasangan kunci-nilai dari dictionary. |
| `pop(key, default)` | Menghapus `key` dan mengembalikan nilainya. Jika `key` tidak ada, kembalikan `default` (jika diberikan) atau melempar `KeyError`. |
| `popitem()` | Menghapus dan mengembalikan pasangan (kunci, nilai) yang terakhir disisipkan (sejak Python 3.7). |
| `update(other_dict)` | Memperbarui dictionary dengan pasangan dari `other_dict`. Kunci yang sama akan ditimpa, kunci baru akan ditambahkan. |

#### Perulangan pada Dictionary (Ringkasan)

```python
products = {'A': 10, 'B': 20}

# Iterasi nilai
for price in products.values():
    print(price)

# Iterasi kunci (default)
for product_name in products:    # atau products.keys()
    print(product_name)

# Iterasi pasangan kunci-nilai
for product_name, price_value in products.items():
    print(f"{product_name}: {price_value}")

# Iterasi dengan counter menggunakan enumerate()
for index, (product_name, price_value) in enumerate(products.items(), start=1):
    print(f"{index}. {product_name}: {price_value}")
```

### Set

*   **Set**: Struktur data yang tidak menyimpan duplikat, *mutable* (elemennya bisa ditambah/dihapus), *unordered* (tidak berurutan). Elemen set harus bertipe *immutable*.
*   **Mendefinisikan set**: Menggunakan kurung kurawal `{}` (misalnya `{1, 2, 3}`). Duplikat akan otomatis dihapus.
*   **Set kosong**: Gunakan `set()` karena `{}` membuat dictionary kosong.

#### Metode-Metode Set (Ringkasan)

| Metode | Deskripsi |
| :----- | :------------------------------------------------------ |
| `add(elem)` | Menambah elemen ke set. Jika elemen sudah ada, set tidak berubah. |
| `remove(elem)` | Menghapus elemen. Melempar `KeyError` jika elemen tidak ditemukan. |
| `discard(elem)` | Menghapus elemen. Tidak error jika elemen tidak ditemukan. |
| `clear()` | Menghapus semua elemen dari set. |

#### Operasi Himpunan (Ringkasan)

| Operator | Metode                | Hasil                                     |
| :------- | :-------------------- | :---------------------------------------- |
| `&#124;` (union) | `union()`             | Set baru berisi semua elemen unik dari kedua set. |
| `&` (intersection) | `intersection()`      | Set baru berisi elemen yang ada di kedua set. |
| `-` (difference) | `difference()`        | Set baru berisi elemen di set kiri yang tidak ada di set kanan. |
| `^` (symmetric difference) | `symmetric_difference()` | Set baru berisi elemen yang unik di salah satu set (bukan di keduanya). |

*   **Operator penugasan majemuk**: `|=`, `&=`, `-=`, `^=` digunakan untuk memodifikasi set secara in-place.
*   **Keanggotaan**: Gunakan `elem in my_set` untuk memeriksa keberadaan elemen.

### Pustaka Standar dan `import`

*   **Pustaka standar Python** menyediakan modul-modul bawaan yang kaya fungsi, seperti `math`, `random`, `re`, `datetime`, dll.
*   **Import dasar**: `import module_name`. Elemen diakses dengan `module_name.element_name`.
*   **Alias**: `import module_name as alias`. Element diakses dengan `alias.element_name`.
*   **Impor spesifik**: `from module_name import element1, element2`. Elemen diakses langsung dengan `element1`.
*   **Impor semua `*`**: `from module_name import *`. **Tidak disarankan** karena dapat menyebabkan bentrokan nama dan mengurangi kejelasan kode.
*   **Variabel `__name__`**:
    *   Bernilai `"__main__"` jika berkas dieksekusi langsung.
    *   Bernilai nama modul jika berkas diimpor.
    *   Digunakan dalam `if __name__ == '__main__':` untuk menjalankan kode hanya saat berkas dieksekusi sebagai program utama.