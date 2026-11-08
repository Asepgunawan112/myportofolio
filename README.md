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

1. Dalam project ini saya memakai chat ai GEMINI untuk membantu saya membuat test pada test.py yaitu pada pembuatan test edit, selain itu saya meminta cara agar navbar dari tempalte css uiverse.io tidak mereload ulang posisi navbar ketika browser reload karena berpindah page, ini menghasilkan kode ` {% if request.resolver_match.url_name == 'show_main' %}checked{% endif %`. ![alt text](image.png).
2. untuk cara membuat edit page di project ini, saya mengambil refrensi dari video youtube ` https://youtu.be/_myGxUnoGHY?si=UROz4cRxx_XejHNP` dan stack overflow (benar, saya akhirnya membuka platform ini lagi).

---

### Tugas 4

- AI Discolsure

* Di tugas kali ini saya menggunakan AI untuk membantu penggunaan syntax pada permission accesss di html untuk access editor (syntax untuk mengatur agar editor hanya memunculkan tombol edit di tampilannya). Ini saya lakukan karena pada django forum, syntax yang saya temukan agak berbeda. LINK : '''https://forum.djangoproject.com/t/allow-staff-users-to-use-django-admin-to-manage-users-only-for-specific-group/9194/2'''

* Link refrensi grouping user untuk editor : '''https://youtu.be/IF_ZpCiZKkw?si=K-S0cW3HiMh6WN_p'''
* Refrensi untuk fitur grouping dan required condition yang saya pakai = `https://forum.djangoproject.com/t/allow-staff-users-to-use-django-admin-to-manage-users-only-for-specific-group/9194/2 , https://docs.djangoproject.com/en/6.1/topics/auth/default/#the-login-required-decorator`
* Refrensi untuk superuser : '''https://youtu.be/LRNk6LLDUII?si=1KYsuGO9PD4PCcHO''' dan disini saya juga meminta ai untuk memvalidasi langkah saya.

---

### Tugas 5

---

1. Fungsi debounce berguna untuk mengatasi server agar tidak melakukan proses berat terus-menerus dalam waktu yang berdekatan (yang mana akan membuat server bekerja terlalu berat). Contoh penerapan pada project ini ada pada proses get oleh ajax yang mana dipakai di fitur search. Pada fitur search, dipakai teknik debounce yang mana setelah pengguna selesai mengetik, lalu 300 milidetik selanjutnya ajax baru akan mengrimkan http request get ke server. Tanpa teknik debounce, ajax akan melakukan request terus menerus setiap pengguna mengetik huruf baru. Jadim debounce menunggu dulu sampai pengguna berhenti mengetik selama 300 milidetik, barulah setelahnya memberikan request.
2. Jadi, await itu berhubungan dengan async. Proses ini bisa digambarkan seperti "Tunggu saya fetch dulu (async), jika sudah beres baru lakukan instruksi selanjutnya(await)". Jadi, tanpa await, maka instruksi akan terganggu karena belum tentu fetch berhasil terpanggil, tetapi instruksi selanjutnya sudah dijalankan(ini akan menimbulkan fetch menghasilkan promise yang tidak terhandle).
3. Serangan XSS adalah serangan dimana ada sebuah serangan dimana seseorang memasukkan suatu script/code ke dalam form website sehingga membuat front-end menerima dan memproses script tersebut sehingga membuat website mengalami serangan-serangan tertentu (mengakses session pengguna lain atau menganggu tampilan web yang ada). Alasan mengapa template django lebih aman akan serangan ini karena form dan templating pada django sudah memuat validasi mereka sendiri yang sudah termasuk kedalam django nya sehingga memuat fitur auto-escape secara otomatis. Sementara pada AJAX, validasi atau pengecekan data harus dibuat sendiri oleh developer karena tidak memiliki fitur bawaan tersebut, sehingga membuat ajax lebih rentan terhadpat serangan XSS ini.

---

- Sumber

1. '''https://youtu.be/E9XcoEMu1lk?si=7ylNjHA2-IxFj20H'''
2. YT WPU, Tutorial JS lanjutan

# AI Disclosure

1. Saya menggunakan AI untuk melakukan penyesuaian pada card css di page certificate agar lebih rapih.
2. Saya menggunakan AI untuk memberi contoh dalam pembuatan test.py

---

# Tugas 6

---

1. Karena ada gagasan lain dalam REST selain komunikasi melalui JSON, yaitu data diperlakukan sebagai resource (sehingga URL murni menunjuk pada data), http method tidak dituliskan di dalam URL melainkan dikirimkan dari client ke server dengan mengubahnya menjadi request, lalu barulah server mengembalikan response berupa JSON. Jadi, pertukaran data dengan JSON saja belum cukup untuk disebut REST. Perbedaan put dan patch adalah dari cara kerjanya. Walaupun keduanya sama-sama mengedit (atau memperbarui) data, tetapi teknisnya berbeda. Ketika melakukan PUT, data baru akan menimpa semua data lama. Jadi jika suatu data memperoleh http method PUT, walaupun yang diubah hanya 1 atribut, tetapi dalam balik layar sebenarnya semua atribut tersebut ditimpa/diperbarui dengan data baru. Berbeda dengan PATCH, PATCH hanya mengedit/memperbarui atribut yang ingin diganti saja tanpa mengusik atribut lainnya dalam data.

2. Peran serializer DRF Django adalah untuk menerjemahkan data raw object di server menjadi format JSON yang siap dikirim melalui response dan juga deserialize yaitu menerjemahkan lagi JSON menjadi object python. Keuntungan dari serializer ini adalah kita bisa memakai validasi bawaan django dan juga membuat validator sendiri, sehingga akan lebih mempercepat produksi dan juga fleksibel. Selain itu, serializer memetakan seluruh atribut model secara otomatis, sehingga kita tidak perlu menulis kode dictionary (context pada views biasa).

3. Autentikasi-> proses untuk server mengenali user agar bisa mengenali jenis user dan user permission di website. Disini jugs proses login dilakukan yang mana akan menentukan masuk ke akun mana user.
   Authorisasi-> logika akses user, dimana user akan dibagi akses-aksesnya di dalam website berdasakan jenis usernya, apakah user merupakan superuser, editor, atau user biasa. Disini akan diatur http method apa yang bisa dilakukan oleh user yang login (misal semua method pada superuser, get saja untuk reguler user, PUT/PATCH dan get untuk editor). hak akses harus diproteksi/validasi oleh server dan harus melalui permission karena ini merupakan upaya keamanan dari server. Dalam proses ini, hak akses benar-benar diatur untuk menentukan hak autorisasi yang cocok untuk pengguna. Sementara itu, menyembunyikan tombol di template (atau yang django buat hidden) itu hanyalah proses menyembunyikan ui atau tampilannya saja sementara alur kerjanya masih berjalan di balik layar. Jadi jika pengguna melakukan manipulasi html di inspect element browser untuk memunculkan tombol/form yang dibuat hidden atau menggunakan API testing seperti POSTMAN, pengguna tetap dapat memunculkan atau menggunakan hak akses yang disembunyikan tersebut karena fitur tersebut hanya disembunyikan secara tampilannya saja.

4. Karena ketika program memakai session Authentication, browser mengirimkan cookie session di browser milik pengguna yang mana hal tersebut bisa digunakan untuk mengakses authentikasi yang nantinya menuju ke hak autorisiasi pengguna. CSRF token tetap dibutuhkan di tahap ini karena session cookie tersebut bisa dimanfaatkan oleh pihak lain ketika user mendapat serangan dari website lain yang sedang dibuka secara bersamaan (CSRF attack), tanpa csrf token, webiste tidak dapat mengenali apakah session key yang sedang login saat ini merupakan token yang berasal dari website kita atau tidak dan membuat website berbahaya tadi dapat menyerang website kita. Test yang memakai force_authenticate tidak cukup untuk menguji csrf karena force_authenticate hanya mensimulasikan test dengan membuat seolah user sudah login yang mana hanya menguji autorisasi atau hak akses user saja. Jadi, proses-proses validasi login tidak dilakukan yang mana hal tersebut menjadi sebuah kekurangan.

---

# AI DISCLOSURE

1. Pada tugas ini, proses refactoring saya lakukan dengan melakukan hal serupa yang dicontohkan oleh tutorial 07, beberapa fungsi khusunya untuk fitur terakhir yang saya refactor saya meminta ai copilot untuk membuatnya karena prosesnya akan sangat repetitif. Oleh karena itu, saya memakainya untuk mempersingkat waktu.
2. Test case saya memakai diskusi ai untuk berdiskusi apakah test sudah sesuai atau tidak.
3. Copilot juga digunakan untuk refacotring script js yang melalui proses repetitif (sudah dikerjakan manual lalu untuk fitur terakhir digunakan ai karena proses refactoring nya sama saja dengan yang sebelumnya).

---
