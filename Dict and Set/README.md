## Ulasan `Dictionary` dan `Set`

### Dictionary

`Dictionary` adalah struktur data bawaan Python yang menyimpan koleksi pasangan *key-value*. Setiap *key* harus unik dan bertipe data *immutable* (seperti *string*, angka, atau *tuple*), sedangkan *value* bisa bertipe data apa saja.

**Sintaks Umum:**

```python
dictionary = {
    key1: value1,
    key2: value2,
    # ...
}
```

**Konstruktor `dict()`:**

Anda dapat membuat `dictionary` menggunakan konstruktor `dict()`. Metode ini menerima *list* dari *tuple*, di mana setiap *tuple* berisi pasangan `(key, value)`.

```python
pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
print(pizza)
# Output: {'name': 'Margherita Pizza', 'price': 8.9, 'calories_per_slice': 250, 'toppings': ['mozzarella', 'basil']}
```

**Mengakses Nilai dengan Notasi Kurung Siku:**

Untuk mengakses *value* yang terkait dengan sebuah *key*, gunakan notasi kurung siku `[]`.

```python
dictionary[key]
```
Contoh:
```python
print(pizza['name'])
# Output: Margherita Pizza
```

### Metode `Dictionary` yang Umum

Berikut adalah beberapa metode yang sering digunakan pada `dictionary`:

*   **`get(key, default)`**:
    Mengembalikan *value* yang terkait dengan `key` yang diberikan. Jika `key` tidak ditemukan, ia akan mengembalikan `default` (jika disediakan), atau `None` jika `default` tidak disediakan. Ini lebih aman daripada notasi kurung siku karena tidak akan memunculkan `KeyError`.

    ```python
    print(pizza.get('price', 0.0))
    # Output: 8.9
    print(pizza.get('weight', 0.0))
    # Output: 0.0 (key 'weight' tidak ada, mengembalikan default)
    ```

*   **`keys()`**:
    Mengembalikan *view object* yang berisi semua *key* dalam `dictionary`. *View object* ini mencerminkan perubahan pada `dictionary`.

    ```python
    print(pizza.keys())
    # Output: dict_keys(['name', 'price', 'calories_per_slice', 'toppings'])
    ```

*   **`values()`**:
    Mengembalikan *view object* yang berisi semua *value* dalam `dictionary`.

    ```python
    print(pizza.values())
    # Output: dict_values(['Margherita Pizza', 8.9, 250, ['mozzarella', 'basil']])
    ```

*   **`items()`**:
    Mengembalikan *view object* yang berisi semua pasangan *key-value* dalam `dictionary` sebagai *tuple*.

    ```python
    print(pizza.items())
    # Output: dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
    ```

*   **`clear()`**:
    Menghapus semua pasangan *key-value* dari `dictionary`, membuatnya kosong.

    ```python
    my_dict = {'a': 1, 'b': 2}
    my_dict.clear()
    print(my_dict)
    # Output: {}
    ```

*   **`pop(key, default)`**:
    Menghapus item dengan `key` yang ditentukan dan mengembalikan *value*nya.
    *   Jika `key` tidak ditemukan dan `default` disediakan, `default` akan dikembalikan.
    *   Jika `key` tidak ditemukan dan `default` tidak disediakan, akan memunculkan `KeyError`.

    ```python
    print(pizza.pop('price', 10))
    # Output: 8.9
    # pizza sekarang adalah: {'name': 'Margherita Pizza', 'calories_per_slice': 250, 'toppings': ['mozzarella', 'basil']}

    # pizza.pop('total_price') # Ini akan memunculkan KeyError
    ```
    *Catatan:* Urutan argumen adalah `key` kemudian `default`.

*   **`popitem()`**:
    Menghapus dan mengembalikan pasangan *key-value* terakhir yang dimasukkan ke dalam `dictionary`. Mulai Python 3.7, `dictionary` mempertahankan urutan penyisipan.

    ```python
    pizza = {'name': 'Margherita Pizza', 'price': 8.9, 'calories_per_slice': 250}
    print(pizza.popitem())
    # Output: ('calories_per_slice', 250)
    print(pizza)
    # Output: {'name': 'Margherita Pizza', 'price': 8.9}
    ```

*   **`update(other_dict)`**:
    Memperbarui `dictionary` dengan pasangan *key-value* dari `other_dict`.
    *   Jika `key` dari `other_dict` sudah ada di `dictionary` awal, *value*nya akan ditimpa.
    *   Jika `key` baru, pasangan *key-value* tersebut akan ditambahkan.

    ```python
    pizza.update({'price': 15, 'total_time': 25})
    print(pizza)
    # Output: {'name': 'Margherita Pizza', 'price': 15, 'total_time': 25}
    ```

### Melakukan *Loop* pada `Dictionary`

Misalkan kita memiliki `dictionary` berikut:
```python
products = {'Laptop': 990, 'Smartphone': 600, 'Tablet': 250, 'Headphones': 70}
```

*   **Iterasi pada *Value*:**
    Untuk mengulang hanya *value*-nya, gunakan metode `values()`.

    ```python
    for price in products.values():
        print(price)
    ```
    Output:
    ```
    990
    600
    250
    70
    ```

*   **Iterasi pada *Key*:**
    Anda bisa mengulang `dictionary` secara langsung atau menggunakan metode `keys()`. Keduanya akan mengulang *key*.

    ```python
    for product in products.keys():
        print(product)
    # atau
    for product in products: # Default iterasi pada dictionary adalah keys
        print(product)
    ```
    Output:
    ```
    Laptop
    Smartphone
    Tablet
    Headphones
    ```

*   **Iterasi pada Pasangan *Key-Value*:**
    Metode `items()` mengembalikan *tuple* `(key, value)` untuk setiap item.

    ```python
    for item in products.items():
        print(item)
    ```
    Output:
    ```
    ('Laptop', 990)
    ('Smartphone', 600)
    ('Tablet', 250)
    ('Headphones', 70)
    ```

    Untuk membongkar (*unpacking*) *key* dan *value* ke dalam variabel terpisah saat iterasi:

    ```python
    for product, price in products.items():
        print(product, price)
    ```
    Output:
    ```
    Laptop 990
    Smartphone 600
    Tablet 250
    Headphones 70
    ```

*   **Fungsi `enumerate()` dengan `Dictionary`:**
    Jika Anda perlu melacak indeks saat mengulang item, gunakan `enumerate()`. Ini akan memberikan indeks dan item untuk setiap iterasi.

    ```python
    for index, item in enumerate(products.items()):
        print(index, item)
    ```
    Output:
    ```
    0 ('Laptop', 990)
    1 ('Smartphone', 600)
    2 ('Tablet', 250)
    3 ('Headphones', 70)
    ```

    Anda dapat mengatur nilai awal hitungan `enumerate()` dengan argumen kedua:

    ```python
    for index, item in enumerate(products.items(), 1):
        print(index, item)
    ```
    Output:
    ```
    1 ('Laptop', 990)
    2 ('Smartphone', 600)
    3 ('Tablet', 250)
    4 ('Headphones', 70)
    ```

---

### Set

`Set` adalah struktur data bawaan di Python yang menyimpan koleksi item unik yang tidak terurut (tidak ada urutan tertentu). Ini berarti elemen tidak bisa diakses berdasarkan indeks atau *key*. `Set` bersifat *mutable*, tetapi hanya dapat berisi elemen bertipe data *immutable* (seperti angka, *string*, atau *tuple*).

**Mendefinisikan `Set`:**

Elemen `set` ditulis di dalam kurung kurawal `{}` dan dipisahkan dengan koma.

```python
my_set = {1, 2, 3, 4, 5}
print(my_set)
# Output: {1, 2, 3, 4, 5}
```

**Mendefinisikan `Set` Kosong:**

Untuk membuat `set` kosong, gunakan fungsi `set()`. Menggunakan `{}` akan membuat `dictionary` kosong, bukan `set` kosong.

```python
empty_set = set() # Ini adalah set kosong
empty_dict = {}   # Ini adalah dictionary kosong

print(type(empty_set))
# Output: <class 'set'>
print(type(empty_dict))
# Output: <class 'dict'>
```

### Metode `Set` yang Umum

*   **`add(element)`**:
    Menambahkan `element` ke dalam `set`. Jika `element` sudah ada, tidak ada yang terjadi karena `set` hanya berisi elemen unik.

    ```python
    my_set = {1, 2, 3}
    my_set.add(4)
    print(my_set)
    # Output: {1, 2, 3, 4}
    my_set.add(2) # Tidak ada perubahan
    print(my_set)
    # Output: {1, 2, 3, 4}
    ```

*   **`remove(element)` dan `discard(element)`**:
    Kedua metode ini digunakan untuk menghapus `element` dari `set`.
    *   **`remove(element)`**: Akan memunculkan `KeyError` jika `element` tidak ditemukan.
    *   **`discard(element)`**: Tidak akan melakukan apa-apa (dan tidak memunculkan *error*) jika `element` tidak ditemukan.

    ```python
    my_set = {1, 2, 3, 4, 5}
    my_set.remove(4)
    print(my_set)
    # Output: {1, 2, 3, 5}

    my_set.discard(10) # Tidak ada error, tidak ada perubahan
    print(my_set)
    # Output: {1, 2, 3, 5}

    # my_set.remove(10) # Ini akan memunculkan KeyError
    ```

*   **`clear()`**:
    Menghapus semua elemen dari `set`, membuatnya kosong.

    ```python
    my_set = {1, 2, 3}
    my_set.clear()
    print(my_set)
    # Output: set()
    ```

### Operasi Himpunan Matematika

`Set` mendukung berbagai operasi himpunan yang mirip dengan matematika. Misalkan kita memiliki dua `set`:
```python
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}
```

*   **`issubset(other_set)` dan `issuperset(other_set)`**:
    *   `issubset()`: Mengembalikan `True` jika semua elemen `set` pertama ada di `other_set`.
    *   `issuperset()`: Mengembalikan `True` jika semua elemen `other_set` ada di `set` pertama.

    ```python
    small_set = {2, 3}
    print(small_set.issubset(my_set))   # Output: True
    print(my_set.issuperset(small_set)) # Output: True
    ```

*   **`isdisjoint(other_set)`**:
    Mengembalikan `True` jika dua `set` tidak memiliki elemen yang sama (saling lepas).

    ```python
    another_set = {7, 8, 9}
    print(my_set.isdisjoint(another_set)) # Output: True
    print(my_set.isdisjoint(your_set))    # Output: False (karena ada irisan {2,3,4})
    ```

*   **Operator Gabungan (`|`) atau `union()`**:
    Menggabungkan semua elemen unik dari kedua `set`.

    ```python
    print(my_set | your_set)  # Output: {1, 2, 3, 4, 5, 6}
    print(my_set.union(your_set)) # Output: {1, 2, 3, 4, 5, 6}
    ```

*   **Operator Irisan (`&`) atau `intersection()`**:
    Mengembalikan elemen yang sama (irisan) di kedua `set`.

    ```python
    print(my_set & your_set)  # Output: {2, 3, 4}
    print(my_set.intersection(your_set)) # Output: {2, 3, 4}
    ```

*   **Operator Selisih (`-`) atau `difference()`**:
    Mengembalikan elemen yang ada di `set` pertama, tetapi tidak ada di `set` kedua.

    ```python
    print(my_set - your_set)  # Output: {1, 5} (Elemen di my_set yang tidak di your_set)
    print(your_set - my_set)  # Output: {6}   (Elemen di your_set yang tidak di my_set)
    print(my_set.difference(your_set)) # Output: {1, 5}
    ```

*   **Operator Beda Setangkup (`^`) atau `symmetric_difference()`**:
    Mengembalikan elemen yang ada di salah satu `set`, tetapi tidak di keduanya. Ini adalah gabungan dikurangi irisan.

    ```python
    print(my_set ^ your_set)  # Output: {1, 5, 6}
    print(my_set.symmetric_difference(your_set)) # Output: {1, 5, 6}
    ```

*   **Operator `in`**:
    Memeriksa keberadaan elemen di dalam `set`. Mengembalikan `True` jika ada, `False` jika tidak.

    ```python
    print(5 in my_set) # Output: True
    print(10 in my_set) # Output: False
    ```

---

### Python Standard Library

*Python Standard Library* (PSL) adalah koleksi modul bawaan Python yang menyediakan fungsionalitas siap pakai untuk berbagai tugas. Modul-modul ini mengimplementasikan solusi terstandardisasi, sehingga Anda tidak perlu menulis kode dasar dari awal.

Contoh modul bawaan populer meliputi:
*   `math`: Untuk fungsi matematika.
*   `random`: Untuk menghasilkan angka acak.
*   `re`: Untuk operasi reguler expression.
*   `datetime`: Untuk manipulasi tanggal dan waktu.

### Pernyataan `Import`

Untuk menggunakan fungsionalitas dari modul yang ada di *Python Standard Library* (atau modul kustom lainnya), Anda perlu mengimpornya. Pernyataan `import` biasanya ditempatkan di bagian atas berkas Python.

*   **Import Dasar:**
    Gunakan kata kunci `import` diikuti nama modul. Untuk memanggil fungsi atau variabel dari modul tersebut, gunakan sintaks `module_name.function_name()`.

    ```python
    import math

    # Menggunakan fungsi sqrt dari modul math
    print(math.sqrt(36))
    # Output: 6.0
    ```

*   **Mengimpor Modul dengan Alias:**
    Anda dapat memberikan nama lain (*alias*) pada modul yang diimpor menggunakan kata kunci `as`. Ini berguna untuk nama modul yang panjang atau untuk mencegah konflik nama.

    ```python
    import math as m

    print(m.sqrt(36))
    # Output: 6.0
    ```

*   **Mengimpor Elemen Tertentu dari Modul:**
    Gunakan `from module_name import item1, item2, ...` untuk mengimpor hanya elemen-elemen spesifik (fungsi, kelas, variabel) dari modul. Setelah diimpor, elemen-elemen ini dapat langsung digunakan tanpa awalan nama modul.

    ```python
    from math import radians, sin, cos

    angle_degrees = 45
    angle_radians = radians(angle_degrees) # Tidak perlu math.radians
    sine_value = sin(angle_radians)       # Tidak perlu math.sin
    cosine_value = cos(angle_radians)     # Tidak perlu math.cos

    print(f"Sudut {angle_degrees} derajat sama dengan {angle_radians:.2f} radian.")
    print(f"Nilai sinus: {sine_value:.2f}")
    print(f"Nilai cosinus: {cosine_value:.2f}")
    ```

*   **Memberi Alias pada Elemen yang Diimpor:**
    Mirip dengan modul, Anda bisa memberi alias pada elemen spesifik yang diimpor.

    ```python
    from os import path as pth, system as syscmd

    # Sekarang Anda bisa menggunakan pth.join() atau syscmd()
    ```

*   **Import dengan Asterisk (`*`)**:
    Digunakan untuk mengimpor semua nama (fungsi, kelas, variabel) yang didefinisikan dalam sebuah modul secara langsung ke *namespace* saat ini.

    ```python
    from math import *

    print(sqrt(36))  # Bisa langsung memanggil sqrt() tanpa awalan math.
    print(pi)        # Bisa langsung memanggil pi
    ```
    **Peringatan:** Penggunaan `from module import *` tidak disarankan dalam kode produksi karena dapat menyebabkan beberapa masalah:
    1.  **Konflik Nama:** Jika Anda mengimpor dari beberapa modul dan mereka memiliki nama yang sama, salah satu definisi akan menimpa yang lain.
    2.  **Kode Kurang Jelas:** Menjadi sulit untuk mengetahui dari modul mana sebuah fungsi berasal hanya dengan melihat namanya.
    3.  **Masalah Performa:** Dapat mengimpor lebih banyak hal daripada yang sebenarnya Anda butuhkan.

---

### `if __name__ == '__main__':`

Variabel bawaan `__name__` adalah variabel khusus di Python. Perilakunya bergantung pada bagaimana berkas Python dieksekusi:

*   Jika berkas Python dieksekusi secara langsung (sebagai program utama), nilai `__name__` akan menjadi `"__main__"`.
*   Jika berkas Python diimpor sebagai modul ke berkas Python lain, nilai `__name__` akan menjadi nama modul itu sendiri (misalnya, `my_module` jika berkasnya `my_module.py`).

Kondisional `if __name__ == '__main__':` adalah pola umum yang digunakan untuk menjalankan kode hanya ketika skrip dieksekusi sebagai program utama. Ini sangat berguna untuk:

*   **Menjalankan Kode Pengujian:** Kode pengujian atau contoh penggunaan dapat ditempatkan di sini.
*   **Menginisialisasi Program Utama:** Fungsi utama dari skrip (misalnya, `main()` function) sering dipanggil di dalam blok ini.
*   **Mencegah Eksekusi Kode saat Diimpor:** Memastikan bahwa kode tertentu tidak dieksekusi ketika skrip diimpor ke berkas lain sebagai modul.

```python
# my_script.py

def greet(name):
    return f"Halo, {name}!"

def main():
    print("Ini adalah fungsi utama dari skrip.")
    print(greet("Dunia"))

# Kode di dalam blok ini hanya akan dieksekusi jika my_script.py dijalankan langsung
if __name__ == '__main__':
    main()
    print("Skrip ini dijalankan sebagai program utama.")

# Jika my_script.py diimpor ke file lain, misalnya:
# import my_script
# print(my_script.greet("Pengguna"))
# Output:
# Halo, Pengguna!
# (Fungsi main() tidak akan terpanggil secara otomatis)