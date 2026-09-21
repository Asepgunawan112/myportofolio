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

### Tugas 3

1. Karena dengan memakai form bawaan dari django, kita bisa menghemat waktu produksi karena tidak perlu lagi memikirkan keamanan pengiriman data yang kita buat di dalam form, data akan tehindar dari masalah-msalah umum seperti sql injection atau CORS (tetap harus dihandle oleh beberapa method)---> dibahas dikelas. Keuntungan lainnya adalah kita bisa mempersingkat waktu development karena form django telah menyediakan fungsi-fungsi seperti form date, url, textarea, text input yang membuat validasi otomatis dan kita juga tidak perlu membuat fungsi-fugsi form dari awal. Yang kedua, csrf token berfungsi sebagai "kartu akses (ini dari kelas diterangin kak, pls bukan dari ai :'D)" suatu url agar bisa mengubah data-data di dalam server.

2. Karena JSON memiliki readability yang lebih baik daripada xml, ini terjadi karena pada JSON kita melihat hierarki suatu objek dan juga isi dari key dan value secara simple ('key' : value). Sementara pada xml, syntax yang dipakai lebih menyulitkan untuk dibaca karena memakai syntax <> layaknya html yang mana ini juga berakibat pada proses pemahaman hierarki objek oleh developer. Selain itu, framework saat ini banyak yang banyak menggunakan JSON sebagai format data (ex.MongoDB).

3. alur:
   -Browser mengirimkan HTTP request ke server (dalam kasus ini get), django mencocokan request dengan path yang ada di urls dan meneruskan nya ke fungsi view yang bersangkutan, fungsi view mengakses data dari database (experience.object.all), django melakukan parse data dari database tersebut dengan `certificate_json = serializers.serialize("json", certificate)`, data yang sudah dalam format JSON dikirimkan ke klien.

- karena JSON menjadi standar pengiriman data saat ini, jika pada kasus lain yang mana front-end bukan berasal dari keluarga python, jika kita mengirimkan request ke API dari framework non-python (ex.React) maka front-end sudah pasti membutuhkan data dalam format universal yaitu JSON, bukan dalam object python.

---
# AI Disclosure
1. Dalam project ini saya memakai chat ai GEMINI untuk membantu saya membuat test pada test.py yaitu pada pembuatan test edit, selain itu saya meminta cara agar navbar dari tempalte css uiverse.io tidak mereload ulang posisi navbar ketika browser reload karena berpindah page, ini menghasilkan kode ``` {% if request.resolver_match.url_name == 'show_main' %}checked{% endif %```. ![alt text](image.png).
2. untuk cara membuat edit page di project ini, saya mengambil refrensi dari video youtube ``` https://youtu.be/_myGxUnoGHY?si=UROz4cRxx_XejHNP``` dan stack overflow (benar, saya akhirnya membuka platform ini lagi).



