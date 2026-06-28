# Daftar Isi

- [Menginstal, Mengonfigurasi, dan Menggunakan Python di Lingkungan Lokal](#menginstal-mengonfigurasi-dan-menggunakan-python-di-lingkungan-lokal)
  - [Mengapa Perlu Penyiapan Lokal?](#mengapa-perlu-penyiapan-lokal)
  - [2. Cara Menginstal Python di macOS](#2-cara-menginstal-python-di-macos)
    - [Verifikasi Instalasi](#verifikasi-instalasi)
  - [3. Cara Menginstal Python di Windows](#3-cara-menginstal-python-di-windows)
  - [4. Python di Linux](#4-python-di-linux)
  - [5. Menjalankan Skrip Python secara Lokal](#5-menjalankan-skrip-python-secara-lokal)
    - [Menyiapkan Folder Proyek di VS Code](#menyiapkan-folder-proyek-di-vs-code)
  - [6. Menggunakan Shell Interaktif Python (*Interactive Shell*)](#6-menggunakan-shell-interaktif-python-interactive-shell)
    - [Memulai Shell Interaktif](#memulai-shell-interaktif)
    - [Siklus REPL (*Read, Evaluate, Print, Loop*)](#siklus-repl-read-evaluate-print-loop)
    - [Keluar dari Shell Interaktif](#keluar-dari-shell-interaktif)
    - [Kapan Menggunakan Shell Interaktif vs Editor](#kapan-menggunakan-shell-interaktif-vs-editor)
  - [7. Ringkasan Instalasi Python](#7-ringkasan-instalasi-python)
    - [Python di Lingkungan Lokal](#python-di-lingkungan-lokal)
    - [Menggunakan Shell Interaktif Python](#menggunakan-shell-interaktif-python)

---

## Menginstal, Mengonfigurasi, dan Menggunakan Python di Lingkungan Lokal

Modul ini akan memandu Anda dalam menyiapkan Python pada komputer lokal, menjalankan skrip Python, dan menggunakan *shell* interaktif Python. Semua langkah akan dijelaskan untuk sistem operasi Windows, macOS, dan Linux.

---

### Mengapa Perlu Penyiapan Lokal?
Sepanjang workshop dan lab, Anda akan banyak menggunakan editor Python milik freeCodeCamp. Namun, penting untuk tetap mempelajari cara menyiapkan Python di mesin lokal Anda sendiri. Hal ini memungkinkan Anda untuk berlatih dan mengembangkan proyek di luar platform freeCodeCamp.

---

## 2. Cara Menginstal Python di macOS

Metode termudah untuk menginstal Python di Windows dan Mac adalah dengan mengunduh *installer* dari situs web resmi Python. Kita akan membahas instalasi di macOS terlebih dahulu.

Langkah-langkahnya adalah sebagai berikut:

1. Kunjungi [https://www.python.org/](https://www.python.org/) dan arahkan kursor ke menu **"Downloads"**. Sebuah *modal* akan muncul menampilkan versi terbaru Python yang sesuai untuk sistem operasi Anda.
2. Klik tombol yang menampilkan versi Python saat ini (dari *modal* yang muncul). Pengunduhan berkas *installer* `.pkg` akan dimulai secara otomatis.
3. Setelah *installer* `.pkg` selesai diunduh, buka berkas tersebut, lalu klik **"Continue"** pada jendela yang muncul.
4. Terus klik tombol **"Continue"** hingga Anda mencapai bagian **"Installation Type"**. Di sana, klik tombol **"Install"**.
5. Masukkan kata sandi Anda jika diminta, lalu biarkan proses instalasi berjalan hingga selesai.
6. Setelah instalasi selesai, Anda akan melihat pesan yang menyatakan bahwa Python telah berhasil terpasang. Klik **"Close"** untuk menutup *installer*.

### Verifikasi Instalasi
Untuk memverifikasi instalasi Python Anda:

- Buka aplikasi **Terminal** (aplikasi bawaan macOS untuk antarmuka teks).
- Jalankan salah satu perintah berikut:
  ```bash
  python --version
  ```
  atau
  ```bash
  python3 --version
  ```
- Anda juga dapat membuka *interpreter* Python secara langsung dengan mengetik `python` atau `python3` di terminal.

> **Catatan Penting:**
> *Interpreter Python* adalah program yang membaca kode Python, menerjemahkannya menjadi instruksi yang dapat dipahami komputer, dan menjalankan instruksi tersebut.
>
> *Terminal* adalah antarmuka berbasis teks yang memungkinkan Anda berinteraksi dengan komputer dengan mengetikkan perintah. Setiap sistem operasi memiliki aplikasi terminal bawaan: **Terminal** di macOS, **Command Prompt** atau **PowerShell** di Windows, dan terminal seperti **GNOME Terminal** atau **Konsole** di Linux.
>
> Pada beberapa sistem macOS dan Linux yang lebih lama, perintah `python` mungkin merujuk ke Python 2, sementara `python3` khusus untuk Python 3. Jika Anda menjalankan `python --version` dan melihat versi seperti `Python 2.7.18`, kemungkinan sistem Anda memiliki perangkat lunak lama yang bergantung pada Python 2. Dalam kasus ini, gunakan `python3` untuk menjalankan semua kode Python Anda ke depannya. **Perlu diingat bahwa Python 2 sudah tidak lagi didukung (end-of-life) dan tidak boleh digunakan untuk pengembangan baru.**

---

## 3. Cara Menginstal Python di Windows

1. Kunjungi [https://www.python.org/](https://www.python.org/) dan arahkan kursor ke **"Downloads"**. Anda akan melihat *modal* yang bertuliskan *"Download for Windows"* dan tombol unduh dengan versi Python terbaru.
2. Klik nomor versi tersebut, dan pengunduhan berkas *executable* (`.exe`) untuk Windows akan dimulai secara otomatis.
3. Setelah berkas *installer* Python selesai diunduh untuk Windows, klik dua kali berkas tersebut, lalu ikuti petunjuk instalasi.
4. **Sangat penting:** Saat Anda melihat opsi **"Add python.exe to Path"**, centang opsi tersebut, lalu klik **"Install Now"**. Langkah ini akan sangat memudahkan Anda untuk memanggil Python dari baris perintah di kemudian hari.
5. Verifikasi instalasi dengan membuka *shell* baris perintah seperti **PowerShell** atau **Command Prompt**, kemudian jalankan perintah:
   ```bash
   python --version
   ```
   Anda juga bisa membuka *interpreter* Python dengan mengetik `python`.

---

## 4. Python di Linux

Sebagian besar distribusi Linux utama seperti Ubuntu, Debian, dan Fedora sudah menyertakan Python secara bawaan.

Untuk memeriksa versi Python yang terinstal, buka terminal dan jalankan salah satu perintah berikut:
```bash
python --version
```
atau
```bash
python3 --version
```

Jika perintah tersebut tidak menampilkan versi Python yang valid, Anda dapat mencari paket instalasi untuk distribusi Linux Anda di [https://www.python.org](https://www.python.org), atau mencari secara *online* tentang cara yang direkomendasikan untuk menginstal Python pada distro Linux yang Anda gunakan.

---

## 5. Menjalankan Skrip Python secara Lokal

Sebelum mulai membuat skrip Python, Anda perlu memasang **editor kode** atau **IDE** (*Integrated Development Environment*). IDE adalah aplikasi yang menyatukan editor kode, alat pengujian, terminal, dan fitur lain dalam satu lingkungan terpadu.

Editor populer yang banyak digunakan adalah **VS Code** (Visual Studio Code). Anda dapat mengunduhnya dari [https://code.visualstudio.com/download](https://code.visualstudio.com/download). VS Code tersedia untuk Mac, Windows, dan Linux. Editor inilah yang akan digunakan dalam contoh pelajaran ini.

Pilihan lain yang umum untuk pengembangan Python meliputi:
- PyCharm
- Spyder

### Menyiapkan Folder Proyek di VS Code
1. Buka aplikasi VS Code.
2. Klik menu **File** di pojok kiri atas, lalu pilih **Open Folder**.
3. Pilih atau buat folder baru untuk proyek Anda (misalnya, folder bernama `python-projects`).
4. Setelah folder terbuka, Anda akan melihat **Explorer** di bilah sisi kiri. Klik ikon **New File** (ikon kertas dengan tanda plus), lalu buat berkas baru bernama `main.py`. Ekstensi `.py` menandakan bahwa ini adalah berkas Python.

### Menulis dan Menjalankan Kode
Buka berkas `main.py` yang baru Anda buat dan ketik kode berikut:
```python
print("Hello, world!")
```

Anda memiliki beberapa opsi untuk menjalankan kode ini:

**Opsi 1: Menggunakan Tombol Run di VS Code**
Klik tombol *run* (ikon segitiga/play) yang terletak di pojok kanan atas editor. Ini akan membuka terminal terintegrasi di VS Code dan menjalankan skrip Python Anda. Anda akan melihat output teks `Hello, world!` di terminal.

**Opsi 2: Menggunakan Terminal Secara Manual**
Buka terminal (bisa terminal bawaan VS Code atau terminal sistem operasi Anda), lalu jalankan perintah berikut:
```bash
python main.py
```
Perintah ini harus dijalankan dari dalam folder tempat `main.py` disimpan. Misalnya, jika `main.py` ada di dalam folder `python-projects`, navigasikan ke folder tersebut terlebih dahulu menggunakan perintah:
```bash
cd python-projects
```
Kemudian, barulah jalankan:
```bash
python main.py
```

**Opsi 3: Menggunakan `python3` (Jika Diperlukan)**
Di beberapa lingkungan, terutama di macOS dan Linux di mana Python 2 dan Python 3 terinstal berdampingan, Anda mungkin perlu menggunakan `python3` secara eksplisit:
```bash
python3 main.py
```
Gunakan perintah ini jika `python` tidak dikenal, atau menunjuk ke versi Python yang lebih tua dan Anda ingin menggunakan Python 3.

> **Tips Belajar:** Sepanjang kursus ini, disarankan untuk mencoba menjalankan contoh-contoh dari pelajaran di komputer lokal Anda. Jangan ragu untuk menulis contoh kode sendiri guna menguji dan memperdalam pemahaman Anda.

---

## 6. Menggunakan Shell Interaktif Python (*Interactive Shell*)

Ada kalanya Anda tidak ingin membuat program Python lengkap, melainkan hanya ingin menguji sepotong kode singkat atau mencoba fungsi tertentu. Di sinilah *shell* interaktif Python berperan.

### Memulai Shell Interaktif
Buka aplikasi terminal Anda, ketik `python` (atau `python3` jika diperlukan), lalu tekan Enter. Anda akan melihat tampilan seperti ini (contoh output awal):
```
Python 3.12.2 (main, Mar 21 2024, 22:48:26) [Clang 14.0.3 (clang-1403.0.22.14.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Tanda `>>>` adalah *prompt* yang menandakan bahwa Python sedang menunggu Anda untuk mengetikkan perintah. Coba cetak teks:
```python
print("Hello, world!")
```
Output yang akan muncul adalah:
```
>>> print("Hello, world!")
Hello, world!
```
Setelah teks dicetak, Python akan kembali menampilkan `>>>`, menandakan Anda bisa mengetik perintah berikutnya.

### Siklus REPL (*Read, Evaluate, Print, Loop*)
*Interpreter* Python mengikuti siklus yang dikenal sebagai **REPL**:
- **Read** – membaca masukan (input) dari Anda.
- **Evaluate** – mengevaluasi (mengeksekusi) kode tersebut.
- **Print** – mencetak hasilnya.
- **Loop** – kembali ke prompt `>>>` agar Anda bisa mengetik perintah lain.

Apa yang terjadi jika Anda mengetik perintah yang tidak valid?
```python
>>> something random
```
*Interpreter* tetap mengikuti proses REPL, tetapi akan menghasilkan pesan kesalahan:
```
  File "<stdin>", line 1
    something random
              ^^^^^^
SyntaxError: invalid syntax
```

### Keluar dari Shell Interaktif
Untuk keluar dari *shell* interaktif, Anda bisa mengetik `exit()` dan menekan Enter, atau menggunakan pintasan keyboard:
- **Mac/Linux**: Tekan `Ctrl + D`
- **Windows**: Tekan `Ctrl + Z` lalu `Enter`

### Kapan Menggunakan Shell Interaktif vs Editor
- **Shell interaktif** sangat cocok untuk eksperimen kecil, menguji metode atau fungsi baru secara cepat, atau melakukan eksplorasi data singkat.
- **Editor/IDE** lebih tepat jika Anda mengerjakan program yang lebih panjang dan kompleks, atau ketika Anda bekerja dengan banyak berkas kode yang saling terkait.

---

## 7. Ringkasan Instalasi Python

### Python di Lingkungan Lokal
- **Instalasi**: Cara terbaik untuk menginstal Python di Windows, Mac, dan Linux adalah dengan mengunduh *installer* dari situs web resmi Python ([https://www.python.org/](https://www.python.org/)).
- **Terminal**: Adalah antarmuka berbasis teks untuk menjalankan perintah. Setiap sistem operasi memiliki terminal bawaan: **Terminal** di macOS, **Command Prompt** atau **PowerShell** di Windows, dan berbagai terminal seperti **GNOME Terminal** atau **Konsole** di Linux.
- **IDE** (*Integrated Development Environment*): Menggabungkan editor kode, alat pengujian, terminal, dan fitur lainnya. Pilihan populer meliputi **VS Code**, **PyCharm**, dan **Spyder**.
- **Menjalankan Kode**: Di VS Code, Anda dapat mengeklik tombol *run* (ikon play) di pojok kanan atas untuk menjalankan skrip di terminal terintegrasi. Alternatifnya, melalui terminal manual dengan perintah:
  ```bash
  python main.py
  ```
  (atau `python3 main.py` jika diperlukan). Pastikan Anda berada di direktori (folder) yang tepat sebelum menjalankan perintah (gunakan `cd nama-folder` jika perlu).

### Menggunakan Shell Interaktif Python
- **Definisi**: Program yang memungkinkan Anda mengetik satu perintah Python dan langsung melihat hasilnya. Mulai dengan mengetik `python` (atau `python3`) di terminal Anda.
- **Prompt `>>>`**: Menandakan bahwa Python siap menerima dan mengeksekusi perintah Anda.
- **Siklus REPL** (*Read, Evaluate, Print, Loop*): *Interpreter* membaca masukan, mengevaluasi kode, mencetak hasilnya, lalu kembali ke *prompt* untuk perintah berikutnya.
- **Keluar**: Gunakan perintah `exit()` atau pintasan keyboard `Ctrl + D` (untuk Mac/Linux) / `Ctrl + Z` lalu `Enter` (untuk Windows).

---

Dengan menyelesaikan panduan ini, Anda kini sudah berhasil menginstal Python, dapat menjalankan skrip Python pertama Anda, dan memahami cara memanfaatkan *shell* interaktif untuk bereksperimen dengan kode Python secara lokal.