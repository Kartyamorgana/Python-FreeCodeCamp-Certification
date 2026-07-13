## Catatan Lengkap Python: Algoritma, Notasi Big O, Teknik Pemecahan Masalah, dan Struktur Data

---

### 1. Apa Itu Algoritma dan Bagaimana Notasi Big O Bekerja?

Setiap program komputer menjalankan serangkaian instruksi spesifik dalam urutan tertentu untuk menyelesaikan suatu tugas, seperti mengurutkan angka, memodifikasi gambar, atau melacak inventaris.

Di sinilah **algoritma** berperan. **Algoritma** adalah serangkaian instruksi yang tidak ambigu untuk menyelesaikan masalah atau melaksanakan tugas. Anda dapat membayangkan algoritma sebagai "resep" yang memberi tahu komputer apa yang harus dilakukan dan bagaimana melakukannya.

**Dua karakteristik kunci algoritma:**
- Algoritma harus berakhir dalam jumlah langkah yang terbatas.
- Setiap langkah harus tepat dan tidak ambigu.

Algoritma dapat memiliki nol, satu, atau lebih _input_, dan menghasilkan satu atau lebih _output_. Langkah-langkah algoritma bersifat independen dari bahasa pemrograman. Namun, untuk menjalankannya di komputer, Anda perlu mengimplementasikannya dalam bahasa pemrograman seperti Python atau JavaScript.

Algoritma yang benar akan menghasilkan _output_ yang sesuai untuk setiap _input_ yang valid. Selain benar, algoritma juga harus **efisien**.

Efisiensi algoritma diukur dari segi **waktu** yang dibutuhkan untuk berjalan dan **ruang memori** yang diperlukan. Mengetahui efisiensi sangat penting karena memberikan gambaran tentang performanya saat ukuran _input_ bertambah. Contoh: mengurutkan 15 bilangan bulat berbeda dengan mengurutkan 1 juta bilangan bulat. Algoritma yang tidak efisien dapat membuat program sangat lambat atau bahkan macet ketika prosesnya semakin besar dan kompleks.

Di sinilah **notasi Big O** menjadi sangat penting. **Notasi Big O** menggambarkan performa kasus terburuk (_worst-case_) atau laju pertumbuhan suatu algoritma seiring bertambahnya ukuran _input_.

Laju pertumbuhan mengacu pada bagaimana sumber daya yang dibutuhkan meningkat seiring ukuran _input_ membesar. Big O fokus pada performa kasus terburuk karena ini krusial untuk memahami seberapa efisien algoritma, bahkan dalam skenario terburuk sekalipun, terlepas dari _input_ awalnya.

Kembali ke contoh pengurutan, mengurutkan 1 juta bilangan tentu memakan lebih banyak waktu dan sumber daya daripada mengurutkan 15 bilangan. Big O tidak memberikan angka pasti, tetapi memberikan gambaran bagaimana algoritma berskala seiring bertambahnya ukuran _input_ (`n`), berdasarkan jumlah operasi yang dilakukan.

Dalam Big O, kita biasanya menyatakan ukuran _input_ dengan huruf **`n`**. Misalnya, jika _input_ adalah sebuah _list_, `n` adalah jumlah elemen dalam _list_ tersebut.

**Faktor konstanta dan suku orde rendah diabaikan** saat menentukan kompleksitas waktu berdasarkan jumlah operasi. Seiring `n` membesar, dampak suku-suku kecil tersebut semakin kecil. Suku yang akan mendominasi perilaku algoritma adalah suku dengan orde tertinggi terhadap `n`.

Contoh: Algoritma yang membutuhkan **`7n + 20`** operasi. Seiring `n` membesar, dampak konstanta 20 semakin kecil. Suku `7n` akan mendominasi dan menentukan efisiensi keseluruhan algoritma.

Contoh lain: Algoritma dengan **`20n² + 15n + 7`** operasi. Suku `20n²` akan mendominasi seiring `n` tumbuh, sehingga algoritma ini memiliki **kompleksitas waktu kuadratik** karena suku dominannya memiliki `n²`.

Kompleksitas waktu kuadratik hanyalah salah satu dari banyak jenis kompleksitas waktu. Berikut beberapa yang paling umum:

#### Kompleksitas Waktu Umum

-   **O(1) – Waktu Konstan (_Constant Time_)**
    Algoritma membutuhkan waktu yang sama tanpa memandang ukuran _input_.
    Contoh: memeriksa apakah bilangan genap atau ganjil.

    ```python
    def periksa_genap_ganjil(bilangan):
        if bilangan % 2 == 0:
            return 'Genap'
        else:
            return 'Ganjil'
    ```

-   **O(log n) – Waktu Logaritmik (_Logarithmic Time_)**
    Waktu bertambah perlahan seiring _input_ membesar. Umum pada algoritma yang terus-menerus mengurangi ukuran masalah dengan pecahan konstan. Contoh: _Binary Search_ memiliki O(log n) pada kasus terburuk.

-   **O(n) – Waktu Linear (_Linear Time_)**
    Waktu eksekusi bertambah secara proporsional terhadap ukuran _input_.
    Contoh: _loop_ `for` yang mengiterasi seluruh elemen _list_.

    ```python
    for nilai in daftar_nilai:
        print(nilai)
    ```

-   **O(n log n) – Waktu Log-Linear (_Log-Linear Time_)**
    Kompleksitas waktu yang umum pada algoritma pengurutan efisien seperti _Merge Sort_ dan _Quick Sort_.

-   **O(n²) – Waktu Kuadratik (_Quadratic Time_)**
    Waktu bertambah secara kuadratik relatif terhadap ukuran _input_. Umumnya tidak efisien untuk masalah nyata dan sering muncul pada _loop_ bersarang (nested loop).

    ```python
    for i in range(n):
        for j in range(n):
            print("Halo, Dunia!")
    ```

-   Kompleksitas lainnya termasuk **O(2ⁿ)** (_Exponential Time_) dan **O(n!)** (_Factorial Time_). Keduanya sangat tidak efisien untuk skenario dunia nyata.

Pada grafik yang membandingkan pertumbuhan fungsi matematika untuk kompleksitas-kompleksitas di atas, sumbu x (horizontal) adalah ukuran _input_, dan sumbu y (vertikal) adalah waktu berjalan. Kompleksitas Kuadratik cenderung tumbuh jauh lebih cepat, sementara Kompleksitas Konstan tetap datar meskipun _input_ membesar.

#### Kompleksitas Ruang (_Space Complexity_)

Notasi Big O juga berlaku untuk kebutuhan ruang memori yang digunakan algoritma:
-   **O(1) – Ruang Konstan**: Algoritma selalu membutuhkan jumlah memori tetap, berapa pun ukuran _input_. Contoh: algoritma yang hanya membuat beberapa variabel.
-   **O(n) – Ruang Linear**: Memori bertambah proporsional terhadap ukuran _input_. Contoh: membuat salinan _list_ sepanjang `n`.
-   **O(n²) – Ruang Kuadratik**: Memori bertambah kuadratik. Contoh: membuat matriks 2D dengan dimensi berdasarkan ukuran _input_.

Algoritma adalah blok bangunan program komputer, sedangkan notasi Big O adalah kerangka kerja untuk menganalisis efisiensinya berdasarkan bagaimana kebutuhan waktu dan ruang pada kasus terburuk berskala seiring ukuran _input_. Memahami efisiensi ini sangat penting untuk mengembangkan perangkat lunak yang bekerja secara efisien dalam skenario nyata.

#### Pertanyaan

1.  Manakah yang paling tepat menggambarkan algoritma?
    Jawaban: Serangkaian instruksi langkah demi langkah yang dirancang untuk menyelesaikan masalah atau melakukan tugas.

2.  Apa tujuan utama notasi Big O dalam konteks algoritma?
    Jawaban: Untuk menggambarkan bagaimana penggunaan sumber daya suatu algoritma tumbuh seiring ukuran _input_ meningkat.

3.  Jika suatu algoritma memiliki kompleksitas waktu O(n), apa artinya tentang performanya?
    Jawaban: Waktu berjalan algoritma meningkat secara proporsional dengan ukuran _input_.

---

### 2. Teknik Pemecahan Masalah yang Baik dan Cara Menghadapi Tantangan Algoritmik

Menyelesaikan tantangan algoritmik adalah cara yang bagus untuk melatih kemampuan pemecahan masalah. Ini membutuhkan cara berpikir analitis, kemampuan memecah masalah menjadi komponen inti, dan menemukan solusi yang menghasilkan _output_ yang benar secara efisien.

**Contoh Tantangan:**
*"Diberikan sebuah string, buat algoritma yang mengembalikan string baru dengan karakter dalam urutan terbalik."*

#### Langkah 1: Pahami Masalah
Baca deskripsi berulang kali agar tidak melewatkan informasi penting. Kemudian pecah masalah menjadi komponen inti. Ajukan pertanyaan berikut:
-   Apa _input_nya? (`string`)
-   Apa _output_ yang diharapkan? (`string` baru dengan karakter terbalik)
-   Bagaimana cara mengubah _input_ menjadi _output_?

#### Langkah 2: Rencanakan dengan Pseudocode
**Pseudocode** adalah deskripsi tingkat tinggi dari logika algoritma, yang tidak terikat pada bahasa pemrograman tertentu. Biasanya merupakan campuran bahasa sehari-hari dengan konstruksi pemrograman dasar (IF, ELSE, FOR, WHILE). Contoh pseudocode untuk "Membalik String":

```
FUNGSI balik_string(original_string):
  SET reversed_string = ""
  UNTUK SETIAP karakter DI original_string:
    TAMBAHKAN karakter KE AWAL reversed_string
  KEMBALIKAN reversed_string
```

#### Langkah 3: Pertimbangkan Berbagai Pendekatan dan Efisiensinya
Ada banyak cara untuk menyelesaikan masalah. Pilihlah yang paling efisien. Misalnya, untuk membalik _string_ di Python, kita bisa:
-   Menggunakan _extended slice_ `[::-1]`.
-   Melakukan _loop_ dari kiri ke kanan dan menambahkan karakter ke awal _string_ baru (ini bisa inefisien untuk _string_ besar karena _string_ bersifat _immutable_).
-   Menggunakan fungsi `reversed()` yang dikombinasikan dengan `"".join()`.

#### Langkah 4: Periksa _Edge Cases_
**_Edge cases_** adalah _input_ spesifik yang valid pada batasan-batasan tertentu. Untuk tantangan ini, _string_ kosong adalah _edge case_. Pastikan algoritma menanganinya dengan benar.

#### Langkah 5: Implementasi
Tulis kode yang modular, mudah dibaca, dan ikuti praktik terbaik bahasa yang digunakan. Manfaatkan _tools_ bawaan jika memungkinkan. Uji kode saat Anda menulis, dan pastikan _edge cases_ ditangani.

#### Langkah 6: Refaktor dan Evaluasi
Setelah mengimplementasikan, periksa apakah kode berfungsi untuk semua contoh. Refaktor jika perlu untuk kejelasan atau efisiensi. Proses pengembangan tidak selalu linear; Anda dapat kembali dan memperbaiki kode.

**Kesimpulan:** Latihan yang konsisten akan mengembangkan kemampuan pemecahan masalah Anda.

#### Pertanyaan

1.  Langkah pertama paling penting saat menghadapi tantangan pemecahan masalah adalah?
    Jawaban: Memahami pernyataan masalah, _input_, dan batasan.

2.  Apa tujuan utama menulis pseudocode?
    Jawaban: Untuk menguraikan logika algoritma dengan cara yang dapat dibaca manusia, bebas bahasa pemrograman.

3.  Mengapa penting mempertimbangkan _edge cases_ sebelum menulis kode akhir?
    Jawaban: _Edge cases_ membantu memastikan algoritma berfungsi dengan benar untuk semua _input_ yang valid.

---

### 3. Bagaimana _Array_ Dinamis Berbeda dari _Array_ Statis?

#### _Array_ Statis
-   Memiliki ukuran tetap, dialokasikan saat inisialisasi, dan tidak dapat diubah selama program berjalan.
-   Elemen disimpan di lokasi memori yang berdekatan (**kontigu**), membuat pengambilan data efisien (akses O(1)).
-   Cocok jika jumlah elemen diketahui di awal dan akses sering dilakukan.
-   Jika penuh, untuk menambah elemen, Anda harus membuat _array_ baru yang lebih besar dan menyalin semua elemen yang ada, ini adalah operasi yang tidak efisien (O(n)).
-   Python **tidak** memiliki _array_ statis bawaan, tetapi bahasa seperti Java memilikinya. Contoh di Java: `int[] numbers = new int[3];`

#### _Array_ Dinamis
-   Dapat tumbuh atau menyusut secara otomatis saat program berjalan.
-   Mekanisme pengubahan ukuran otomatis: ketika penuh, _array_ baru yang lebih besar dibuat dan elemen disalin. Proses ini dioptimalkan agar operasi mahal (pengubahan ukuran) jarang terjadi.
-   Akses elemen berdasarkan indeks: O(1).
-   Menyisipkan di tengah: O(n) karena elemen setelahnya harus digeser.
-   Menyisipkan di akhir: Rata-rata O(1) (jika ada ruang), tetapi bisa O(n) saat _array_ perlu diubah ukurannya.
-   Cocok jika ukuran data tidak diketahui sebelumnya atau sering terjadi penyisipan/penghapusan.
-   Di Python, **_list_** adalah implementasi dari _array_ dinamis. Contoh:

    ```python
    angka = [3, 4, 5, 6]

    # Akses elemen
    print(angka[0])  # Output: 3

    # Ubah elemen
    angka[2] = 16
    print(angka) # Output: [3, 4, 16, 6]

    # Tambah elemen di akhir (append)
    angka.append(7)
    print(angka) # Output: [3, 4, 16, 6, 7]

    # Sisipkan elemen di indeks tertentu (insert)
    angka.insert(3, 15)
    print(angka) # Output: [3, 4, 16, 15, 6, 7]

    # Hapus elemen di indeks tertentu (pop)
    angka.pop(2) # Menghapus 16
    print(angka) # Output: [3, 4, 15, 6, 7]

    # Hapus elemen terakhir
    angka.pop() # Menghapus 7
    print(angka) # Output: [3, 4, 15, 6]
    ```

**Kesimpulan:** Gunakan _array_ statis jika ukuran data tetap dan akses sangat sering. Gunakan _array_ dinamis jika ukuran data bervariasi dan Anda memerlukan fleksibilitas. Pertimbangkan _trade-off_ antara kesederhanaan dan fleksibilitas.

#### Pertanyaan

1.  Perbedaan utama ukuran antara _array_ statis dan dinamis?
    Jawaban: _Array_ statis memiliki ukuran tetap yang ditentukan saat kompilasi atau inisialisasi, sedangkan _array_ dinamis dapat mengubah ukurannya selama waktu eksekusi (`runtime`).

2.  Jika _array_ statis penuh, proses apa yang harus dilakukan untuk menambah elemen?
    Jawaban: Membuat _array_ baru yang lebih besar, lalu menyalin semua elemen dari _array_ lama ke _array_ baru.

3.  Kapan _array_ statis lebih cocok daripada _array_ dinamis?
    Jawaban: Ketika ukuran data sudah diketahui saat program ditulis dan tidak akan berubah, serta performa memori dan akses langsung diindeks menjadi prioritas.

---

### 4. Bagaimana _Stack_ dan _Queue_ Bekerja?

#### _Stack_ (Tumpukan)
-   Struktur data **_Last-In, First-Out (LIFO)_**. Elemen yang terakhir dimasukkan adalah yang pertama dikeluarkan.
-   Memiliki dua ujung: **atas** (_top_) dan **bawah** (_bottom_). Semua operasi penambahan dan penghapusan hanya dilakukan di bagian atas.
-   **_Push_**: Menambah elemen ke atas tumpukan (O(1)).
-   **_Pop_**: Menghapus elemen dari atas tumpukan (O(1)).
-   Kompleksitas ruang untuk operasi _push_/_pop_ adalah O(1).
-   Analogi: tumpukan piring; Anda hanya bisa menaruh dan mengambil piring dari bagian paling atas.

#### _Queue_ (Antrean)
-   Struktur data **_First-In, First-Out (FIFO)_**. Elemen yang pertama masuk adalah yang pertama keluar.
-   Memiliki dua ujung: **depan** (_front_) dan **belakang** (_rear_ atau _back_).
-   **_Enqueue_**: Menambah elemen ke belakang antrean (O(1)).
-   **_Dequeue_**: Menghapus elemen dari depan antrean (O(1)).
-   Kompleksitas ruang untuk operasi _enqueue_/_dequeue_ adalah O(1).
-   Analogi: antrean orang di kasir; orang pertama yang datang akan dilayani pertama.

**Implementasi di Python:**
-   _Stack_ dapat menggunakan _list_ biasa dengan `.append()` untuk _push_ dan `.pop()` untuk _pop_.
-   _Queue_ dapat menggunakan `collections.deque` untuk efisiensi: `.append()` untuk _enqueue_ dan `.popleft()` untuk _dequeue_.

```python
# Implementasi Stack menggunakan list
tumpukan = []
tumpukan.append(1)   # Operasi push
tumpukan.append(2)
tumpukan.append(3)
print("Tumpukan setelah push:", tumpukan) # Output: [1, 2, 3]

print("Pop elemen:", tumpukan.pop())       # Operasi pop, mengeluarkan 3
print("Tumpukan setelah pop:", tumpukan) # Output: [1, 2]

# Implementasi Queue menggunakan collections.deque
from collections import deque

antrian = deque()
antrian.append(1)    # Operasi enqueue
antrian.append(2)
antrian.append(3)
print("Antrian setelah enqueue:", antrian) # Output: deque([1, 2, 3])

print("Dequeue elemen:", antrian.popleft()) # Operasi dequeue, mengeluarkan 1
print("Antrian setelah dequeue:", antrian) # Output: deque([2, 3])
```

#### Pertanyaan

1.  Perbedaan utama antara _stack_ dan _queue_?
    Jawaban: _Stack_ beroperasi dengan prinsip LIFO (Last-In, First-Out), sedangkan _queue_ beroperasi dengan prinsip FIFO (First-In, First-Out).

2.  Operasi untuk menambah elemen pada _stack_ disebut?
    Jawaban: _Push_.

3.  Operasi untuk menghapus elemen dari _queue_ disebut?
    Jawaban: _Dequeue_.

---

### 5. Bagaimana _Singly Linked List_ Bekerja dan Bedanya dengan _Doubly Linked List_?

**_Linked list_** adalah struktur data linear di mana setiap _node_ terhubung ke _node_ berikutnya. Setiap _node_ menyimpan data dan referensi (atau _pointer_) ke _node_ selanjutnya. _Linked list_ sering digunakan untuk mengimplementasikan struktur data lain (seperti _stack_ dan _queue_) dan algoritma graf.

#### _Singly Linked List_
-   Setiap _node_ hanya memiliki satu referensi, yaitu ke _node_ berikutnya. Ini berarti traversal (penelusuran) hanya bisa dilakukan dalam satu arah (maju).
-   **_Head node_**: _Node_ pertama dalam _list_. Ini biasanya satu-satunya _node_ yang dapat diakses secara langsung; traversal dimulai dari sini.
-   **_Tail node_**: _Node_ terakhir dalam _list_ yang penunjuk berikutnya (_next pointer_) menunjuk ke `None`.

**Operasi Penyisipan:**
-   **Di awal**: O(1). Cukup ubah referensi _head_ untuk menunjuk ke _node_ baru, lalu hubungkan _node_ baru ke _head_ lama.
-   **Di akhir**: O(n). Harus melakukan traversal dari _head_ hingga _node_ terakhir (_tail_), lalu sambungkan _node_ baru ke _tail_ tersebut.
-   **Di tengah**: O(n). Pertama, cari posisi yang diinginkan (O(n)), lalu perbarui referensi dari _node_ sebelumnya dan _node_ baru.
-   Kompleksitas ruang untuk penyisipan adalah O(1) (untuk _node_ baru).

**Operasi Penghapusan:**
-   **Di awal**: O(1). _Head_ cukup diubah untuk menunjuk ke _node_ berikutnya.
-   **Di akhir**: O(n). Traversal ke _node_ sebelum _tail_, lalu putuskan referensi yang menunjuk ke _tail_ lama.
-   **Di tengah**: O(n). Traversal untuk menemukan _node_ sebelumnya (O(n)), lalu hubungkan _node_ sebelumnya ke _node_ setelah _node_ yang dihapus, "melewati" _node_ yang akan dihapus.
-   Kompleksitas ruang untuk penghapusan adalah O(1).

#### _Doubly Linked List_
-   Setiap _node_ memiliki **dua referensi**: satu ke _node_ berikutnya (_next_) dan satu lagi ke _node_ sebelumnya (_previous_).
-   Traversal dapat dilakukan baik maju maupun mundur.
-   Umumnya juga menyimpan referensi ke _tail_ (_last node_) untuk memungkinkan traversal yang efisien dari belakang.
-   Lebih fleksibel dalam operasi traversal dan penghapusan, tetapi membutuhkan memori lebih besar karena setiap _node_ menyimpan dua referensi.
-   Operasi penyisipan/penghapusan pada dasarnya sama, namun harus memperbarui dua referensi (_next_ dan _previous_) dari _node_ yang terlibat. Penyisipan di akhir bisa O(1) jika referensi ke _tail_ sudah disimpan.

**Kesimpulan:** Pilih _singly linked list_ jika Anda ingin menghemat memori dan hanya membutuhkan traversal satu arah. Pilih _doubly linked list_ jika Anda membutuhkan fleksibilitas untuk menelusuri _list_ ke dua arah dan siap dengan penggunaan memori yang sedikit lebih besar.

#### Pertanyaan

1.  Apa yang dimaksud dengan _linked list_?
    Jawaban: Struktur data linear di mana elemen-elemennya (_node_) terhubung satu sama lain melalui referensi (atau _pointer_) daripada diletakkan di lokasi memori yang bersebelahan.

2.  Apa perbedaan utama antara _singly linked list_ dan _doubly linked list_?
    Jawaban: _Singly linked list_ hanya memungkinkan traversal satu arah (maju) karena setiap _node_ hanya memiliki referensi ke _node_ berikutnya. _Doubly linked list_ memungkinkan traversal dua arah (maju dan mundur) karena setiap _node_ memiliki referensi ke _node_ berikutnya dan _node_ sebelumnya.

3.  Berapa kompleksitas waktu untuk menyisipkan _node_ di awal _singly linked list_?
    Jawaban: O(1) (Waktu Konstan).

---

### 6. Bagaimana _Map, Hash Map,_ dan _Set_ Bekerja?

#### _Abstract Data Type_ (ADT)
ADT adalah representasi konseptual dari tipe data, termasuk operasi yang bisa dilakukan terhadapnya, tanpa merinci implementasi internalnya. Contoh: **_Map_** adalah ADT yang mengelola koleksi pasangan kunci-nilai (_key-value pairs_). Setiap kunci bersifat unik, tetapi nilai boleh berulang. Operasi umum _Map_: menyisipkan, mengambil, memperbarui, menghapus, dan memeriksa keberadaan kunci.

#### _Hash Map_ (_Hash Table_)
_Hash Map_ adalah implementasi konkret dari ADT _Map_. Menggunakan teknik **_hashing_**:
-   Sebuah fungsi _hash_ mengambil sebuah kunci dan menghasilkan nilai _hash_ (biasanya bilangan bulat), yang kemudian digunakan untuk menghitung indeks di dalam sebuah _array_ internal.
-   **_Hash collision_**: Terjadi ketika dua kunci berbeda menghasilkan nilai _hash_ dan/atau indeks yang sama. Strategi penanganan _collision_ meliputi:
    -   **_Chaining_**: Setiap indeks _array_ menunjuk ke sebuah _linked list_ yang berisi semua elemen yang memiliki _hash_ yang sama.
    -   **_Open Addressing_**: Jika sebuah indeks sudah terisi, algoritma mencari indeks kosong berikutnya berdasarkan urutan pencarian yang ditentukan (misalnya, mencari indeks berikutnya secara linear).
-   Kompleksitas rata-rata untuk operasi _insert, get, delete_ adalah O(1).
-   Kompleksitas kasus terburuk: O(n) jika terjadi banyak _collision_ dan penanganannya tidak efisien (misalnya, semua elemen berakhir dalam satu _linked list_).
-   Di Python, **_dictionary_** adalah implementasi dari _hash map_.

```python
# Membuat dictionary
kamus = {
    'A': 1,
    'B': 2,
    'C': 3
}
# Alternatif lain untuk membuat dictionary
kamus_alt = dict(A=1, B=2, C=3)

# Akses nilai dengan kunci
print(kamus['A'])       # Output: 1

# Memperbarui nilai
kamus['A'] = 4
print(kamus)            # Output: {'A': 4, 'B': 2, 'C': 3}

# Menghapus pasangan kunci-nilai
del kamus['A']
print(kamus)            # Output: {'B': 2, 'C': 3}

# Memeriksa keanggotaan kunci
print('C' in kamus)     # Output: True

# Mengakses semua kunci, nilai, atau item
print(kamus.keys())     # Output: dict_keys(['B', 'C'])
print(kamus.values())   # Output: dict_values([2, 3])
print(kamus.items())    # Output: dict_items([('B', 2), ('C', 3)])
```

#### _Set_ (Himpunan)
-   Koleksi elemen unik dan tidak berurutan.
-   Elemen _set_ tidak bisa diakses menggunakan indeks.
-   Hanya bisa menyimpan objek **_immutable_** (misalnya, bilangan bulat, _string_, _tuple_), karena nilai _hash_ dari elemen harus tetap konsisten.
-   Operasi dasar: menambah, menghapus, dan memeriksa keanggotaan. Kompleksitas rata-rata O(1), dan kasus terburuk O(n) akibat _collision_.
-   Implementasi Python menggunakan _hash table_ (secara internal hanya menyimpan kunci, tanpa nilai).

```python
# Membuat set
angka = {1, 2, 3, 4}
kosong = set()   # Penting: jangan menggunakan {} karena ini akan membuat dictionary kosong

# Menambah/menghapus elemen
angka.add(5)
print(angka)           # Output: {1, 2, 3, 4, 5}
angka.remove(4)      # Menghapus 4. Akan memunculkan KeyError jika elemen tidak ada
print(angka)           # Output: {1, 2, 3, 5}
angka.discard(10)    # Menghapus 10 jika ada, tidak memunculkan error jika tidak ada
print(angka)           # Output: {1, 2, 3, 5} (tidak berubah)


# Operasi Himpunan (menggunakan metode)
set_a = {1, 2, 3, 4}
set_b = {2, 3, 4, 5, 6}

print(set_a.union(set_b))                # Gabungan: Output: {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b))         # Irisan: Output: {2, 3, 4}
print(set_a.difference(set_b))           # Selisih: Output: {1}
print(set_a.symmetric_difference(set_b)) # Selisih simetris: Output: {1, 5, 6}

# Operasi Himpunan (menggunakan operator)
print(set_a | set_b)   # Union
print(set_a & set_b)   # Intersection
print(set_a - set_b)   # Difference
print(set_a ^ set_b)   # Symmetric difference

# Pengecekan subset/superset
print(set_a.issubset(set_b))    # Output: False
print(set_b.issuperset(set_a))  # Output: False (karena set_a punya 1 yang tidak di set_b)
print({1,2}.issubset(set_a))    # Output: True
print(set_a.isdisjoint({7, 8})) # Output: True (tidak ada elemen yang sama)

# Cek keanggotaan
print(5 in angka)              # Output: True
```

#### Pertanyaan

1.  Apa perbedaan mendasar data yang disimpan oleh _hash map_ dan _set_?
    Jawaban: _Hash map_ menyimpan pasangan kunci-nilai (_key-value pairs_) di mana setiap kunci unik. _Set_ menyimpan koleksi elemen individu yang unik.

2.  Mekanisme utama yang memungkinkan _hash map_ dan _set_ mencapai kompleksitas waktu O(1) rata-rata untuk operasi dasar?
    Jawaban: Penggunaan fungsi _hash_ untuk secara langsung menghitung lokasi memori (indeks _array_) tempat data disimpan atau dicari.

3.  Dalam konteks _hash map_ dan _set_, apa yang dimaksud dengan "_hash collision_"?
    Jawaban: _Hash collision_ terjadi ketika dua kunci atau elemen yang berbeda menghasilkan nilai _hash_ atau indeks _array_ yang sama.

---

### Rangkuman Struktur Data

#### Algoritma dan Notasi Big O
-   **Algoritma**: Sekumpulan instruksi langkah demi langkah yang jelas, terbatas, dan benar untuk menyelesaikan masalah.
-   **Notasi Big O**: Mengukur bagaimana performa (_waktu_ dan _ruang_) algoritma tumbuh dalam kasus terburuk seiring peningkatan ukuran _input_ (`n`). Mengabaikan konstanta dan suku orde rendah.

**Kompleksitas Waktu Umum:**
| Notasi     | Nama           | Karakteristik                                      | Contoh                                  |
| :--------- | :------------- | :------------------------------------------------- | :-------------------------------------- |
| **O(1)**   | Konstan        | Waktu eksekusi tetap, tidak peduli ukuran _input_. | Mengecek ganjil/genap, akses elemen _array_ berdasarkan indeks. |
| **O(log n)** | Logaritmik     | Waktu tumbuh sangat lambat, mengurangi masalah secara signifikan. | _Binary Search_.                        |
| **O(n)**   | Linear         | Waktu eksekusi proporsional terhadap ukuran _input_ `n`. | _Loop_ sederhana yang mengiterasi seluruh _list_. |
| **O(n log n)** | Log-Linear     | Kompleksitas umum untuk algoritma pengurutan yang efisien. | _Merge Sort_, _Quick Sort_.             |
| **O(n²)**  | Kuadratik      | Waktu eksekusi tumbuh secara kuadratik, sangat tidak efisien untuk _input_ besar. | _Nested loop_ (dua _loop_ bersarang).  |
| **O(2ⁿ)**  | Eksponensial   | Waktu tumbuh sangat cepat, sangat tidak praktis.   | Mencari semua _subset_ dari sebuah _set_. |
| **O(n!)**  | Faktorial      | Waktu tumbuh eksplosif, tidak praktis sama sekali. | Menghasilkan semua permutasi.           |

**Kompleksitas Ruang:**
-   **O(1)**: Kebutuhan memori tetap independen dari ukuran _input_.
-   **O(n)**: Kebutuhan memori tumbuh secara linear proporsional dengan ukuran _input_.
-   **O(n²)**: Kebutuhan memori tumbuh secara kuadratik dengan ukuran _input_.

#### Teknik Pemecahan Masalah
1.  **Pahami Masalah**: Identifikasi _input_, _output_, dan batasan.
2.  **Rencanakan dengan Pseudocode**: Buat kerangka logika algoritma yang mudah dibaca.
3.  **Pertimbangkan Berbagai Pendekatan**: Evaluasi solusi alternatif dan efisiensinya.
4.  **Periksa _Edge Cases_**: Pastikan algoritma bekerja untuk _input_ pada batasan atau kasus _spesial_.
5.  **Implementasikan**: Tulis kode yang bersih dan modular.
6.  **Refaktor dan Evaluasi**: Periksa kebenaran, kejelasan, dan efisiensi setelah implementasi.

#### _Array_
-   **Statis**: Ukuran tetap, dialokasikan di awal. Akses `O(1)`. Tidak ada di Python secara bawaan (gunakan _list_ jika perlu _array_ dinamis).
-   **Dinamis**: Ukuran dapat berubah _runtime_ (misalnya, _list_ di Python). Akses `O(1)`. Penambahan/penghapusan di akhir rata-rata `O(1)`, di tengah/awal `O(n)`.

#### _Stack_ dan _Queue_
-   **_Stack_ (LIFO)**: _Last-In, First-Out_. Operasi _push_ dan _pop_ `O(1)`. Ideal untuk _undo_ fungsionalitas, _backtracking_.
-   **_Queue_ (FIFO)**: _First-In, First-Out_. Operasi _enqueue_ (tambah) dan _dequeue_ (hapus) `O(1)`. Ideal untuk antrean tugas, _Breadth-First Search (BFS)_.

#### _Linked List_
-   **_Singly Linked List_**: Setiap _node_ hanya punya referensi ke _node_ berikutnya. Traversal satu arah.
-   **_Doubly Linked List_**: Setiap _node_ punya referensi ke _node_ berikutnya dan sebelumnya. Traversal dua arah, lebih fleksibel tapi konsumsi memori lebih besar.
-   Operasi penyisipan/penghapusan di awal `O(1)`, di akhir atau tengah `O(n)` (kecuali _doubly linked list_ dengan _tail pointer_ memungkinkan penyisipan akhir `O(1)`).

#### _Hash Map_ dan _Set_
-   **_Hash Map_**: (Python _dictionary_). Menyimpan pasangan kunci-nilai unik. Operasi _insert, get, delete_ rata-rata `O(1)`.
-   **_Set_**: (Python _set_). Koleksi elemen unik dan tidak berurutan. Operasi _add, remove, check membership_ rata-rata `O(1)`.
-   **_Hash Collision_**: Terjadi ketika dua kunci (_hash map_) atau elemen (_set_) memiliki nilai _hash_ yang sama. Ditangani dengan _chaining_ (menggunakan _linked list_) atau _open addressing_. Dalam kasus terburuk (banyak _collision_), kompleksitas bisa menjadi `O(n)`.

**Kapan Menggunakan Setiap Struktur Data:**
-   **_List_**: Ketika Anda membutuhkan koleksi terurut yang dapat diindeks, dan ukurannya mungkin berubah.
-   **_Stack_**: Ketika urutan LIFO penting (misalnya, pelacakan riwayat, ekspresi matematika).
-   **_Queue_**: Ketika urutan FIFO penting (misalnya, pemrosesan tugas, penjadwalan).
-   **_Linked List_**: Ketika sering ada penyisipan atau penghapusan elemen di awal atau tengah, dan akses berdasarkan indeks tidak sering dilakukan.
-   **_Hash Map_**: Ketika Anda membutuhkan pencarian, penyisipan, dan penghapusan yang sangat cepat berdasarkan kunci unik.
-   **_Set_**: Ketika Anda membutuhkan koleksi elemen unik dan sering melakukan operasi himpunan (union, intersection, dll.).