## Ulasan Instalasi dan Penggunaan Python

### Python di Lingkungan Lokal Anda

**Instalasi Python:**
Cara terbaik untuk memasang Python di sistem operasi Windows, macOS, dan Linux adalah dengan mengunduh penginstal resmi dari situs web Python: [https://www.python.org/](https://www.python.org/).

**Antarmuka Baris Perintah (Terminal):**
Terminal adalah antarmuka berbasis teks yang memungkinkan Anda berinteraksi dengan komputer melalui perintah yang diketik. Setiap sistem operasi memiliki aplikasi terminal bawaan:
*   **macOS:** Aplikasi *Terminal*.
*   **Windows:** *Command Prompt* atau *PowerShell*.
*   **Linux:** Setiap lingkungan desktop memiliki aplikasi terminal bawaannya sendiri, seperti *GNOME Terminal* atau *Konsole*.

**Integrated Development Environment (IDE):**
IDE adalah singkatan dari *Integrated Development Environment*. IDE adalah lingkungan perangkat lunak komprehensif yang menyediakan fasilitas lengkap untuk pengembangan perangkat lunak. Fitur utama IDE meliputi:
*   Editor kode
*   Alat pengujian (debugger)
*   Terminal terintegrasi
*   Fitur-fitur lain yang memudahkan proses pengembangan (misalnya, manajemen proyek, penyelesaian kode otomatis).

**Editor Kode dan IDE Populer untuk Python:**
Beberapa editor kode dan IDE yang umum digunakan untuk pengembangan Python antara lain:
*   **VS Code** (Visual Studio Code)
*   **PyCharm**
*   **Spyder**

**Menjalankan Kode Python Secara Lokal:**
Ada beberapa metode untuk menjalankan skrip Python di lingkungan lokal Anda:

1.  **Melalui IDE/Editor Kode (Contoh: VS Code):**
    Di VS Code, Anda dapat mengeklik tombol "Run" yang biasanya berbentuk segitiga (simbol putar) yang terletak di pojok kanan atas. Aksi ini akan membuka terminal terintegrasi di VS Code dan menjalankan skrip Python Anda di sana.

2.  **Melalui Terminal Secara Manual:**
    Anda dapat menjalankan program Python secara manual melalui terminal. Berikut adalah langkah-langkahnya:
    *   **Navigasi ke Direktori Program:** Pastikan Anda berada di direktori (folder) tempat file `.py` program Anda disimpan. Gunakan perintah `cd` (change directory) untuk berpindah antar folder.
        **Contoh:** Jika file `main.py` Anda berada di dalam folder bernama `python-projects`, gunakan perintah berikut:
        ```bash
        cd python-projects
        ```
    *   **Jalankan Skrip Python:** Setelah berada di direktori yang benar, gunakan perintah `python` diikuti dengan nama file skrip Anda:
        ```bash
        python main.py
        ```

### Menggunakan Shell Interaktif Python

**Definisi:**
*Interactive shell* (atau juga dikenal sebagai *Python Prompt* atau *REPL*) adalah program yang memungkinkan Anda mengetik perintah Python satu per satu dan langsung melihat hasilnya secara *real-time*.

**Cara Membuka Shell Interaktif:**
1.  Buka aplikasi terminal di sistem operasi Anda.
2.  Ketik perintah `python` (atau `python3` di beberapa sistem) lalu tekan `Enter`.
3.  Anda akan melihat simbol `>>>` yang menandakan bahwa Python siap menerima perintah.

**Contoh Penggunaan:**
Untuk mencetak teks "Hello, world!" ke terminal:
```python
>>> print("Hello, world!")
Hello, world!
>>>
```
Setelah teks dicetak, Python akan kembali menampilkan `>>>`, menandakan bahwa ia siap untuk perintah berikutnya.

**Siklus Read, Evaluate, Print, Loop (REPL):**
REPL adalah siklus kerja inti dari shell interaktif Python. Setiap kali Anda mengetik perintah, interpreter Python akan melakukan hal berikut:
*   **Read:** Membaca masukan (perintah) yang Anda ketik.
*   **Evaluate:** Mengevaluasi atau menjalankan perintah tersebut.
*   **Print:** Mencetak hasil dari evaluasi perintah ke layar.
*   **Loop:** Kembali menampilkan `>>>` untuk menunggu masukan perintah berikutnya, mengulangi siklus.