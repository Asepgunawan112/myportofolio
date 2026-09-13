Nama : Ayyasi

NPM : 2506550482

## Kelas : PBP F

---

# Instruksi Setup

1. Clone repo ---> `git clone <REPO_URL>`
2. Setup venv python ----> `python -m venv env` lalu jalankan `env\Scripts\activate` untuk mengaktifkan venv
3. Install dependensi ----> `pip install -r requirements.txt`
4. Jalankan migrasi ----> `python manage.py makemigrations` lalu `python manage.py migrate`
5. Jalankan unit test----> `python manage.py test main`
6. Jalankan server lokal----> `python manage.py runserver`

---

### Tugas 1

1. ya, dengan memakai elemen semantic html saya menjadi lebih mudah untuk mengenali elemen-elemen web yang saya buat seperti <nav>,<header>, <footer>, dan <section> yang saya pakai.
2. tantangan yang ditemukan ditemukan saat membuat section baru terutama pada bagian grid dan saat saya membuat 2 bagian dalam satu section (kiri-kanan). Pada saat mengatur grid, cukup sulit untuk membuatnya responsive karena disini terdapat card yang saya buat cukup terbatas untuk ukuran nya, sehingga ketika membuat tampilan responsive konten di dalamnya harus mengikuti ukuran card juga. Dalam kasus ini yang paling rumit (ribet) ada di <figcaption> pada card education karena cukup sulit untuk mengatur font nya agar tetap rapih.
3. Ada beberapa batasan yang saya sadari. Salah satu contohnya adalah ketika memasukkan konten gambar, dimana saya harus memasukkan kontek gambar satu-persatu pada html. Yang saya tahu, jika sudah memakai logika pada backend atau mungkin akses API/Database, untuk mengakses konten yang banyak bisa dengan iterasi atau map() konten yang dibutuhkan dengan singkat sehingga tidak perlu memasukkan nya secara manual. Dan itu juga adalah hal yang akan saya lakukan ketika sudah masuk ke logika back-end. Selain itu, saya berniat untuk menambah endpoint berupa contact dan blog di iterasi berikutnya dan juga melakukan fungsi fitur untuk sendEmail.

###

---

AI disclosure

1. di tugas 1 ini saya memakai gemini AI untuk membantu menjelaskan properti css lebih lanjut untuk kebutuhan saya setelah saya mencari syntax nya di w3school dan juga ringkasan google. Penggunaan ini sebagian besar digunakan pada proses perapihan grid. Saya juga menggunakan AI untuk memberikan warna shadow yang pas di card education (ada pada warna rgb style.ss).
2. Untuk card yang saya pakai di web, saya menggunakan template card dari bootstrap dan tailwind yang saya rewrite ke css, disini saya menggunakan bantuan AI untuk meminta saran syntax yang harus saya pakai ketika mendapati utility class yang saya bingung untuk di rewrite ke css biasa.
3. Saya juga menanyakan saran untuk menggunakan logo tech-stack kepada Gemini dan akhirnya saya pakai dari web https://devicon.dev/ untuk web dari techstack nya <i>.
4. Saya juga menanyakan pada AI elemen semantic apa yang tepat digunakan untuk section baru yang saya buat (<figure>).

---

### Tugas 2

1. Pada saat pengguna membuka link/url dari website, browser akan mengirim HTTP request yang akan diteruskan eke urls.py yang ada di folder portofolio/root, jika request yang dikirimkan memiliki route '' maka request akan diteruskan ke main.urls (urls.py pada folder main). Setelah sampai di urls.py di main, disini akan mencocokan request yang dikirim dengan path yang tersedia. Setelah keduanya cocok, maka django akan melanjutkan ke fungsi view yang bersangkutan dan mengeksekusi kodenya. Pada tahap tersebut, django akan merender request, template, dan context. Pada tahap ini, view memanggil model yang ada di models.py untuk mengambil data dari database lalu menyusun nya di dalam context. Lalu pada template, django mengembalikan response berupa tampilan template.html yang dapat dilihat dengan rapi oleh pengguna, lengkap dengan isi data yang berasal dari context.
2. Ada beberapa keuntungan diantaranya:
   -Kemudahan dalam mengelola data, jika data ada banyak kita tidak perlu mengetik satu-satu data yang kita punya di dalam html. Dengan models yang sudah kita miliki kita bisa memasukkan data-data secara perlahan ke database lalu untuk menampilkan data-data tersebut, kita cukup mengiterasikan data nya di html dengan berbagai metode iterasi yang tersedia sehingga kita dapat memangkas penegmbalian data di tampilan cukup dengan satu baris kode saja (dont repeat yourself). Dengan metode ini juga kita jadi lebih mudah untuk melakukan proses CRUD. Karena perlakuan ini pun, kita menjadi lebih mudah untuk mengatur style dari tampilan data karena tidak perlu mengelola baris kode data yang banyak di file html. Metode ini juga merupakan best-practice dalam pembuatan API karena data yang tersimpan di database bisa menjadi lebih dinamis karena format yang kita gunakan bisa diubah menjadi json atau xml untuk kebutuhan dalam pembuatan API.

3. makemigration --> tracking perubahan schema/field di models
   migrate --> eksekusi perubahan schem/field di database
   contoh:
   ````id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title= models.CharField(max_length=255)```
    makemigration & migrate untuk memasukan models ke database
    edit:
    ```id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title= models.CharField(max_length=255)
    organization= models.CharField(max_length=255)
   ````
   makemigration & migrate lagi untuk update perubahan schema models.

---

# AI Disclosure 2

1. Saya memakai Gemini AI Flash untuk meminta saran cara memasukkan img.png kedalam template atau lebih tepatnya bagaimana membuat field yang nantinya bisa menerima file gambar.
2. Untuk task lainnya saya memakai instruksi yang berasal dari tutorial sebelumnya untuk penambahan endpoint dan template dari uiverse.io untuk card.

---
