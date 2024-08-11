# Data Scraping dari RomHacking

## Deskripsi

Repositori ini berisi data hasil scraping berupa file JSON yang diambil dari situs RomHacking. Data ini diambil karena pemilik situs tersebut akan menjadikan situsnya menjadi "Forum Only" dan mungkin saja halaman yang berkaitan dengan _Rom Hack_ akan ditutup.

## Konten

- [data](/data): Folder ini berisi file-file JSON hasil scraping (Baru).
- [data_lama](data_lama): Sama kaya Folder di atas, cuman ini hasil scraping dari internet arsip.
- **README.md**: Berkas yang kamu baca saat ini.

## Struktur Data

Setiap file JSON punya struktur data berisi id untuk setiap entri sebagai identitas.

Pada file [data/translations.json](/data/translations.json) terdapat data berupa `"img"` yang hanya berisi ektensi images (.jpg, .png, .gif). File tersebut adalah screenshot dari game yang telah diterjemahkan 
- contoh url: `/1234screenshot1.png`

     - **1234** adalah ID dari patch
     - **screenshot** adalah nama images nya
     - **1** pada akhiran screenshot adalah sambungan screenshot satu hingga 4
     - **.png** adalah ektensi file images
       
## Lisensi

Repositori ini berlisensi di bawah [MIT License](LICENSE).

## Pengakuan

Data dalam repositori ini diambil dari [RomHacking.net](https://romhacking.net). Saya mengucapkan terima kasih kepada mereka atas data yang disediakan. Saya juga bersedia menghapus repository ini jika mereka keberatan dengan hal yang saya lakukan.
