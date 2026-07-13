## Catatan Lengkap Python: Pencarian, Divide and Conquer, dan Algoritma Pengurutan

---

### 1. Apa Itu Binary Search dan Perbedaannya dengan Linear Search?

Pencarian melalui sekumpulan item adalah hal yang umum dalam ilmu komputer. Terdapat dua algoritma utama yang penting dalam hal pencarian: **Linear Search** dan **Binary Search**.

#### 1.1 Linear Search (Pencarian Linear)
Linear search dimulai dari awal sebuah *list* (atau array/daftar) dan melakukan iterasi melalui setiap item hingga menemukan nilai target yang dicarinya. Jika nilai target ditemukan, indeks (posisi) tempat nilai tersebut berada di dalam *list* akan dikembalikan. Jika nilai target tidak ditemukan, fungsi akan mengembalikan `-1`. Pengembalian nilai `-1` umumnya digunakan karena ia bukan merupakan indeks yang valid di sebagian besar bahasa pemrograman.

**Contoh Kode Linear Search:**
```python
def linear_search(arr, target):
    """
    Melakukan pencarian linear pada list untuk menemukan target.

    Args:
        arr (list): List tempat pencarian dilakukan.
        target: Nilai yang ingin dicari.

    Returns:
        int: Indeks target jika ditemukan, -1 jika tidak.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Contoh penggunaan
my_list = [13, 4, 7, 9, 10]
print(f"Mencari 9 di {my_list}: {linear_search(my_list, 9)}") # Output: 3
print(f"Mencari 5 di {my_list}: {linear_search(my_list, 5)}") # Output: -1
```

Jika *list* yang akan dicari adalah `[13, 4, 7, 9, 10]` dan targetnya `9`, fungsi akan mengembalikan `3` karena `9` berada di indeks `3`. Jika target diubah menjadi `5`, fungsi akan mengembalikan `-1` karena `5` tidak ada di dalam *list*.

Meskipun algoritma ini cukup sederhana, ia bukan yang paling efisien. Jika Anda memiliki *list* item yang sangat besar, linear search dapat memakan waktu lama untuk menemukan targetnya.

**Kompleksitas Algoritma Linear Search:**
-   **Waktu (Time Complexity):** O(n) – Waktu pencarian bertambah secara linear (proporsional) seiring dengan bertambahnya ukuran *list* (n). Pada kasus terburuk, kita harus memeriksa setiap elemen.
-   **Ruang (Space Complexity):** O(1) – Tidak memerlukan ruang tambahan yang signifikan karena hanya menggunakan beberapa variabel tetap.

#### 1.2 Binary Search (Pencarian Biner)
Binary search adalah algoritma yang jauh lebih efisien untuk mencari di dalam *list* item yang besar dibandingkan linear search. **Syarat utama dan terpenting untuk menggunakan binary search adalah *list* harus sudah terurut** (biasanya dalam urutan naik).

Binary search bekerja dengan strategi "bagi dan taklukkan" (divide and conquer). Algoritma ini akan terus membagi *list* menjadi dua bagian dan memeriksa apakah nilai target berada di tengah *list*.
1.  Jika target ditemukan di tengah, indeksnya dikembalikan.
2.  Jika tidak, algoritma akan memeriksa apakah target lebih kecil atau lebih besar dari elemen tengah.
3.  Berdasarkan perbandingan tersebut, algoritma kemudian hanya akan fokus pada paruh kiri atau paruh kanan *list*, sehingga mengabaikan setengah bagian lainnya.
Proses ini terus membagi bagian *list* yang tersisa hingga target ditemukan. Jika target tidak ada setelah seluruh rentang pencarian habis, ia mengembalikan `-1`.

**Contoh Kode Binary Search:**
```python
def binary_search(arr, target):
    """
    Melakukan pencarian biner pada list yang sudah terurut untuk menemukan target.

    Args:
        arr (list): List terurut tempat pencarian dilakukan.
        target: Nilai yang ingin dicari.

    Returns:
        int: Indeks target jika ditemukan, -1 jika tidak.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Menghitung indeks tengah

        if arr[mid] == target:
            return mid  # Target ditemukan
        elif arr[mid] < target:
            low = mid + 1  # Target ada di paruh kanan
        else: # arr[mid] > target
            high = mid - 1 # Target ada di paruh kiri

    return -1 # Target tidak ditemukan

# Contoh penggunaan
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Mencari 7 di {sorted_list}: {binary_search(sorted_list, 7)}") # Output: 6
print(f"Mencari 11 di {sorted_list}: {binary_search(sorted_list, 11)}") # Output: -1

another_sorted_list = [10, 20, 30, 40, 50]
print(f"Mencari 30 di {another_sorted_list}: {binary_search(another_sorted_list, 30)}") # Output: 2
```

**Cara Kerja Binary Search:**
1.  Inisialisasi `low` ke indeks pertama (0) dan `high` ke indeks terakhir (`len(arr) - 1`). Kedua variabel ini menentukan rentang pencarian saat ini.
2.  Selama `low` kurang dari atau sama dengan `high` (`low <= high`):
    *   Hitung indeks tengah `mid` menggunakan `(low + high) // 2`.
    *   Bandingkan elemen di `arr[mid]` dengan `target`:
        *   Jika `arr[mid]` sama dengan `target`, berarti target ditemukan, dan `mid` dikembalikan.
        *   Jika `arr[mid]` lebih kecil dari `target`, berarti target (jika ada) harus berada di sebelah kanan `mid`. Maka, `low` diperbarui menjadi `mid + 1`.
        *   Jika `arr[mid]` lebih besar dari `target`, berarti target (jika ada) harus berada di sebelah kiri `mid`. Maka, `high` diperbarui menjadi `mid - 1`.
3.  Jika perulangan (`while`) selesai tanpa menemukan target (yaitu, `low` menjadi lebih besar dari `high`), itu berarti target tidak ada di dalam *list*, dan fungsi mengembalikan `-1`.

**Kompleksitas Algoritma Binary Search:**
-   **Waktu (Time Complexity):** O(log n) – Setiap langkah dalam algoritma ini mengurangi ukuran masalah menjadi setengahnya. Ini membuatnya sangat efisien untuk *list* yang besar.
-   **Ruang (Space Complexity):** O(1) – Sama seperti Linear Search, algoritma ini hanya menggunakan beberapa variabel tetap, sehingga tidak memerlukan ruang tambahan yang signifikan.

#### 1.3 Perbedaan Utama antara Linear Search dan Binary Search

| Aspek               | Linear Search                                | Binary Search                                    |
| :------------------ | :------------------------------------------- | :----------------------------------------------- |
| **Kondisi Data**    | Tidak memerlukan data terurut                | **Membutuhkan data yang sudah terurut**          |
| **Cara Kerja**      | Mengecek setiap elemen satu per satu dari awal | Membagi dua rentang pencarian terus-menerus      |
| **Kompleksitas Waktu** | O(n) (Linear)                                | O(log n) (Logaritmik)                            |
| **Kompleksitas Ruang** | O(1)                                         | O(1)                                             |
| **Kapan Digunakan** | Untuk *list* kecil, atau *list* yang tidak terurut, atau jika data sering berubah acak. | Untuk *list* besar yang sudah terurut atau dapat diurutkan terlebih dahulu. |

#### Pertanyaan Pemahaman
1.  **Apa perbedaan utama antara Linear Search dan Binary Search?**
    Jawaban: Perbedaan utama adalah Binary Search **memerlukan *list* yang terurut**, sedangkan Linear Search tidak. Selain itu, Binary Search jauh lebih efisien untuk *list* besar (O(log n) vs O(n)).

2.  **Berapa kompleksitas waktu Linear Search?**
    Jawaban: O(n)

3.  **Pada Binary Search, apa yang terjadi jika target tidak ditemukan?**
    Jawaban: Fungsi mengembalikan `-1`.

---

### 2. Apa Itu Divide and Conquer, dan Bagaimana Merge Sort Bekerja?

**Divide and Conquer** (bagi dan taklukkan) adalah sebuah paradigma desain algoritma dalam ilmu komputer. Ini adalah teknik pemecahan masalah secara rekursif menjadi sub-masalah yang lebih kecil, secara independen menyelesaikan sub-masalah tersebut, dan kemudian menggabungkan solusi dari sub-masalah untuk mendapatkan solusi dari masalah asli. Salah satu aspek kuncinya adalah **rekursi**, yaitu ketika sebuah fungsi memanggil dirinya sendiri berulang kali hingga mencapai kasus dasar (*base case*) yang dapat diselesaikan secara langsung. Salah satu contoh klasik algoritma yang menggunakan paradigma ini adalah **Merge Sort**.

#### 2.1 Ilustrasi Divide and Conquer dengan Merge Sort

Misalkan kita memiliki *list* angka yang belum terurut: `[42, 37, 53, 17]`. Tujuan kita adalah mengurutkan *list* ini dari terkecil ke terbesar menggunakan Merge Sort.

**Langkah-langkah Merge Sort:**

1.  **Divide (Pembagian):**
    *   Bagi *list* menjadi dua bagian yang sama besar secara rekursif hingga setiap sub-list hanya memiliki satu elemen. Sebuah *list* dengan satu elemen secara *default* sudah terurut.
    *   Initial list: `[42, 37, 53, 17]`
    *   Bagi: `[42, 37]` | `[53, 17]`
    *   Bagi lagi: `[42]` | `[37]` dan `[53]` | `[17]`

2.  **Conquer (Penaklukkan – Pengurutan/Penggabungan Sub-List):**
    *   Mulai dari sub-list terkecil (satu elemen), lalu gabungkan mereka secara terurut.
    *   Gabungkan `[42]` dan `[37]` → `[37, 42]`
    *   Gabungkan `[53]` dan `[17]` → `[17, 53]`

3.  **Combine (Penggabungan Akhir):**
    *   Gabungkan dua bagian yang sudah terurut (`[37, 42]` dan `[17, 53]`) menjadi satu *list* terurut akhir.
    *   Gabungkan `[37, 42]` dan `[17, 53]` → `[17, 37, 42, 53]`

#### 2.2 Implementasi Merge Sort dalam Python

Berikut adalah dua versi implementasi Merge Sort dalam Python. Versi pertama mengembalikan *list* baru yang terurut, sedangkan versi kedua memodifikasi *list* asli (in-place).

**Versi 1: Mengembalikan List Baru**
```python
def merge_sort_returns_new_list(arr):
    """
    Mengurutkan list menggunakan Merge Sort dan mengembalikan list baru yang terurut.
    """
    if len(arr) <= 1:
        return arr # Base case: list dengan 0 atau 1 elemen sudah terurut

    # Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort_returns_new_list(left_half) # Conquer (rekursif)
    right_sorted = merge_sort_returns_new_list(right_half) # Conquer (rekursif)

    # Combine (penggabungan dua sub-list terurut)
    sorted_list = []
    i = 0 # Indeks untuk left_sorted
    j = 0 # Indeks untuk right_sorted

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            sorted_list.append(left_sorted[i])
            i += 1
        else:
            sorted_list.append(right_sorted[j])
            j += 1

    # Tambahkan sisa elemen jika ada dari salah satu sub-list
    sorted_list.extend(left_sorted[i:])
    sorted_list.extend(right_sorted[j:])

    return sorted_list

# Contoh penggunaan
numbers = [4, 10, 6, 14, 2, 1, 8, 5]
print(f"List asli: {numbers}")
sorted_numbers = merge_sort_returns_new_list(numbers)
print(f"List terurut (versi baru): {sorted_numbers}")
```

**Versi 2: Mengurutkan di Tempat (In-place - sedikit modifikasi pada list asli)**
Versi ini memodifikasi *list* asli yang diberikan sebagai argumen. Meskipun disebut "in-place", perlu dicatat bahwa `left_part` dan `right_part` masih membuat salinan *slice* dari *list* asli, yang memengaruhi kompleksitas ruang.

```python
def merge_sort_in_place(array):
    """
    Mengurutkan list menggunakan Merge Sort secara 'in-place'.
    Perhatikan bahwa slicing di Python membuat salinan, jadi ini BUKAN true in-place.
    """
    if len(array) <= 1:
        return # Base case: list dengan 0 atau 1 elemen sudah terurut

    # Divide
    middle_point = len(array) // 2
    # Membuat salinan (slice) untuk bagian kiri dan kanan
    left_part = array[:middle_point] 
    right_part = array[middle_point:]

    # Conquer (rekursif)
    merge_sort_in_place(left_part)
    merge_sort_in_place(right_part)

    # Combine (gabungkan kembali ke array asli)
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0 # Indeks untuk mengisi array asli

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Tambahkan sisa elemen dari left_part jika ada
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Tambahkan sisa elemen dari right_part jika ada
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers_in_place = [4, 10, 6, 14, 2, 1, 8, 5]
    print(f'Unsorted array (in-place): {numbers_in_place}')
    merge_sort_in_place(numbers_in_place)
    print(f'Sorted array (in-place): {numbers_in_place}') # List numbers_in_place sekarang terurut
```

**Kompleksitas Merge Sort:**
-   **Waktu (Time Complexity):** O(n log n) – Algoritma ini membagi *list* menjadi dua terus-menerus (`log n` kali) dan kemudian menggabungkan kembali (`n` operasi pada setiap tingkat rekursi). Ini menjadikannya algoritma pengurutan yang sangat efisien, stabil, dan paling baik di antara algoritma berbasis perbandingan.
-   **Ruang (Space Complexity):** O(n) – Merge Sort memerlukan ruang tambahan untuk menyimpan sub-list sementara selama proses penggabungan. Bahkan pada versi "in-place" Python, operasi *slicing* seperti `arr[:mid]` membuat salinan baru, sehingga tetap memerlukan ruang O(n).

#### Pertanyaan Pemahaman
1.  **Apa itu paradigma Divide and Conquer dalam ilmu komputer?**
    Jawaban: Divide and Conquer adalah teknik pemecahan masalah secara rekursif menjadi sub-masalah yang lebih kecil, menyelesaikannya secara independen, lalu menggabungkan solusinya.

2.  **Berapa kompleksitas waktu algoritma Merge Sort?**
    Jawaban: O(n log n)

3.  **Berapa kompleksitas ruang algoritma Merge Sort?**
    Jawaban: O(n)

---

### 3. Contoh Implementasi Algoritma Lainnya

Selain algoritma pencarian dan Merge Sort, penting juga untuk familiar dengan algoritma lain yang relevan dalam studi ilmu komputer. Berikut adalah beberapa contoh.

#### 3.1 Binary Search dengan Pelacakan Jalur (Modifikasi dari Binary Search)
Versi ini memodifikasi fungsi `binary_search` untuk tidak hanya mencari nilai, tetapi juga merekam dan mengembalikan jalur atau elemen-elemen yang diperiksa selama pencarian. Ini berguna untuk tujuan debugging atau visualisasi.

```python
def binary_search_with_path(search_list, value):
    """
    Melakukan pencarian biner dan mencatat setiap elemen yang diperiksa.

    Args:
        search_list (list): List terurut tempat pencarian dilakukan.
        value: Nilai yang ingin dicari.

    Returns:
        tuple: (list_of_checked_values, message_string)
               Menampilkan elemen yang diperiksa dan hasil pencarian.
    """
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle) # Mencatat elemen yang diperiksa
        
        if value == value_at_middle:
            return path_to_target, f'Value found at index {mid}'
        elif value > value_at_middle:
            low = mid + 1
        else: # value < value_at_middle
            high = mid - 1
    
    return path_to_target, "Value not found" # Mengembalikan jalur bahkan jika tidak ditemukan

# Contoh penggunaan
print(f"Pencarian 3 di [1, 2, 3, 4, 5]: {binary_search_with_path([1, 2, 3, 4, 5], 3)}")
# Output: ([3], 'Value found at index 2')
print(f"Pencarian 4 di [1, 2, 3, 4, 5, 9]: {binary_search_with_path([1, 2, 3, 4, 5, 9], 4)}")
# Output: ([4], 'Value found at index 3')
print(f"Pencarian 10 di [1, 3, 5, 9, 14, 22]: {binary_search_with_path([1, 3, 5, 9, 14, 22], 10)}")
# Output: ([9, 14], 'Value not found')
```

#### 3.2 Quick Sort
Quick Sort adalah algoritma pengurutan **Divide and Conquer** lainnya. Algoritma ini bekerja dengan memilih elemen sebagai `pivot` dan mempartisi (membagi) elemen-elemen lainnya ke dalam dua sub-list: elemen yang lebih kecil dari pivot dan elemen yang lebih besar dari pivot. Kemudian, algoritma ini secara rekursif mengurutkan sub-list tersebut.

```python
def quick_sort(list_to_sort):
    """
    Mengurutkan list menggunakan algoritma Quick Sort.
    """
    if len(list_to_sort) <= 1:
        return list_to_sort # Base case: list dengan 0 atau 1 elemen sudah terurut
    
    pivot_value = list_to_sort[0] # Memilih elemen pertama sebagai pivot
    
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for num in list_to_sort:
        if num < pivot_value:
            less_than_pivot.append(num)
        elif num == pivot_value:
            equal_to_pivot.append(num)
        else: # num > pivot_value
            greater_than_pivot.append(num)

    # Rekursif mengurutkan sub-list dan menggabungkannya
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

# Contoh penggunaan
unsorted_list_qs = [3, 6, 8, 10, 1, 2, 1]
print(f"Unsorted list (Quick Sort): {unsorted_list_qs}")
sorted_list_qs = quick_sort(unsorted_list_qs)
print(f"Sorted list (Quick Sort): {sorted_list_qs}")
# Output: [1, 1, 2, 3, 6, 8, 10]
```
**Kompleksitas Quick Sort:**
-   **Waktu:** Rata-rata O(n log n), Kasus terburuk O(n²) (terjadi jika pivot selalu elemen terkecil/terbesar).
-   **Ruang:** Rata-rata O(log n), Kasus terburuk O(n) (untuk stack rekursi). Quick Sort umumnya lebih cepat dalam praktiknya daripada Merge Sort karena lebih sedikit *overhead* pada konstanta, meskipun memiliki kompleksitas kasus terburuk yang lebih buruk.

#### 3.3 Selection Sort
Selection Sort adalah algoritma pengurutan sederhana yang bekerja dengan berulang kali menemukan elemen minimum (atau maksimum) dari bagian yang belum terurut dan menukarnya dengan elemen pertama (atau terakhir) dari bagian tersebut.

```python
def selection_sort(items):
    """
    Mengurutkan list menggunakan algoritma Selection Sort.
    Modifikasi list secara in-place.
    """
    n = len(items)
    
    # Iterasi melalui seluruh elemen list
    for i in range(n):
        # Temukan indeks elemen terkecil di sub-list yang belum terurut
        min_index = i
        
        # Bandingkan dengan elemen sisa di sebelah kanan i
        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j
                
        # Tukar elemen terkecil yang ditemukan dengan elemen di posisi i
        # Kecuali jika i sudah menjadi elemen terkecil
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]
            
    return items

# Contoh penggunaan
unsorted_list_ss = [64, 25, 12, 22, 11]
print(f"Unsorted list (Selection Sort): {unsorted_list_ss}")
selection_sort(unsorted_list_ss)
print(f"Sorted list (Selection Sort): {unsorted_list_ss}")
# Output: [11, 12, 22, 25, 64]
```
**Kompleksitas Selection Sort:**
-   **Waktu:** O(n²) – Karena memiliki dua *loop* bersarang, jumlah perbandingan dan pertukaran sebanding dengan kuadrat jumlah elemen.
-   **Ruang:** O(1) – Ini adalah algoritma pengurutan *in-place* yang sesungguhnya.

#### 3.4 Verifikasi Nomor Kartu (Algoritma Luhn)
Algoritma Luhn (juga dikenal sebagai rumus modulus 10 atau mod 10) adalah rumus *checksum* sederhana yang digunakan untuk memvalidasi berbagai nomor identifikasi, seperti nomor kartu kredit. Ini adalah cara non-kriptografi untuk memastikan bahwa data kartu kredit telah dimasukkan dengan benar.

```python
def verify_card_number(num_str):
    """
    Memverifikasi sebuah nomor kartu menggunakan Algoritma Luhn.

    Args:
        num_str (str): String nomor kartu (dapat mengandung spasi atau tanda hubung).

    Returns:
        str: 'VALID!' jika nomor kartu valid, 'INVALID!' jika tidak.
    """
    # 1. Bersihkan string: hapus spasi dan tanda hubung
    cleaned_num = num_str.replace(" ", "").replace("-", "")
    
    # Validasi input: pastikan hanya digit setelah pembersihan
    if not cleaned_num.isdigit():
        return 'INVALID! (Contains non-digit characters)'

    total_sum = 0
    # 2. Balikkan digit nomor kartu
    # ['4', '5', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4'] -> dibalik
    reversed_digits = cleaned_num[::-1]
    
    # 3. Iterasi melalui digit yang dibalik
    for index, char_digit in enumerate(reversed_digits):
        digit = int(char_digit)
        
        # 4. Melipatgandakan setiap digit kedua (dimulai dari digit paling kanan)
        if index % 2 == 1: # Jika indeks ganjil (digit kedua, keempat, dst. dari kanan)
            digit *= 2
            # Jika hasil penggandaan lebih besar dari 9, kurangi 9
            if digit > 9:
                digit -= 9
                
        total_sum += digit # 5. Jumlahkan semua digit
        
    # 6. Jika total_sum modulo 10 sama dengan 0, maka nomor valid
    if total_sum % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'

# Contoh penggunaan
print(f"Verifikasi '79927398713': {verify_card_number('79927398713')}") # Valid
print(f"Verifikasi '79927398714': {verify_card_number('79927398714')}") # Invalid
print(f"Verifikasi '49927398716': {verify_card_number('49927398716')}") # Valid
print(f"Verifikasi '1234 5678 9012 3452': {verify_card_number('1234 5678 9012 3452')}") # Valid
print(f"Verifikasi '1234-5678-9012-3456': {verify_card_number('1234-5678-9012-3456')}") # Invalid
```

---

### 4. Rangkuman: Algoritma Pencarian dan Pengurutan

#### Algoritma Pencarian
-   **Linear Search**
    *   **Cara Kerja:** Memeriksa setiap item dari awal *list* hingga target ditemukan.
    *   **Hasil:** Mengembalikan indeks target atau -1 jika tidak ditemukan.
    *   **Kelemahan:** Tidak efisien untuk *list* yang sangat besar.
    *   **Kompleksitas Waktu:** O(n)
    *   **Kompleksitas Ruang:** O(1)

-   **Binary Search**
    *   **Cara Kerja:** Membagi *list* yang **sudah terurut** menjadi dua secara berulang, mengabaikan setengah bagian di mana target tidak mungkin berada.
    *   **Kelebihan:** Jauh lebih efisien untuk *list* besar.
    *   **Syarat:** *List* harus terurut.
    *   **Kompleksitas Waktu:** O(log n)
    *   **Kompleksitas Ruang:** O(1)

**Perbedaan Utama Pencarian:** Binary Search lebih cocok untuk *list* besar yang terurut, sedangkan Linear Search lebih sederhana untuk *list* kecil atau data yang tidak terurut.

#### Divide and Conquer dan Merge Sort
-   **Divide and Conquer:** Paradigma desain algoritma yang memecah masalah menjadi sub-masalah yang lebih kecil, memecahkannya secara individual, dan menggabungkan hasilnya. Sering melibatkan rekursi.
-   **Merge Sort:** Algoritma pengurutan yang menerapkan paradigma Divide and Conquer.
    *   **Cara Kerja:**
        1.  **Divide:** Membagi *list* menjadi dua bagian sampai setiap bagian berisi satu elemen (yang dianggap sudah terurut).
        2.  **Conquer & Combine:** Menggabungkan sub-list yang terurut tersebut secara berpasangan hingga seluruh *list* terurut.
    *   **Kompleksitas Waktu:** O(n log n) – Sangat efisien dan stabil.
    *   **Kompleksitas Ruang:** O(n) – Memerlukan ruang tambahan untuk proses penggabungan sementara.

#### Algoritma Pengurutan Lainnya (Contoh Tambahan)
-   **Quick Sort:** Menggunakan strategi Divide and Conquer. Memilih elemen `pivot`, mempartisi *list* menjadi elemen yang lebih kecil dan lebih besar dari `pivot`, lalu secara rekursif mengurutkan kedua bagian.
    *   **Kompleksitas Waktu:** Rata-rata O(n log n), Kasus terburuk O(n²).
    *   **Kompleksitas Ruang:** Rata-rata O(log n), Kasus terburuk O(n).

-   **Selection Sort:** Mengurutkan *list* dengan berulang kali mencari elemen minimum dari bagian yang belum terurut dan meletakkannya di posisi yang benar.
    *   **Kompleksitas Waktu:** O(n²) – Tidak efisien untuk *list* besar.
    *   **Kompleksitas Ruang:** O(1) – Merupakan algoritma *in-place*.

-   **Algoritma Luhn:** Bukan algoritma pengurutan atau pencarian, melainkan algoritma *checksum* sederhana yang digunakan untuk memvalidasi nomor identifikasi seperti nomor kartu kredit.

Dengan pemahaman tentang berbagai algoritma ini, Anda dapat membuat pilihan yang tepat untuk tugas pencarian dan pengurutan, menimbang antara efisiensi, kebutuhan akan data terurut, dan penggunaan sumber daya.