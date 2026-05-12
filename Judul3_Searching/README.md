PROGRAM PENCARIAN NOMOR PLAT MOBIL MENGGUNAKAN SEQUENTIAL SEARCH SENTINEL  

Program ini dibuat untuk melakukan pencarian nomor plat mobil pada sistem parkiran menggunakan algoritma Sequential Search Sentinel. Program menerima input berupa daftar nomor plat mobil, kemudian pengguna dapat mencari nomor plat tertentu pada data yang telah disimpan. Algoritma Sequential Search Sentinel digunakan untuk mempermudah proses pencarian secara berurutan dengan menambahkan nilai penanda (sentinel) di akhir data sehingga proses pengecekan menjadi lebih efisien. Program akan menampilkan posisi indeks nomor plat jika ditemukan, dan memberikan pesan bahwa data tidak ditemukan jika nomor plat yang dicari tidak ada di dalam daftar.


Fungsi sequential_search_sentinel  
Fungsi ini digunakan untuk melakukan pencarian data menggunakan metode Sequential Search Sentinel.
 <img width="1064" height="672" alt="fungsi search" src="https://github.com/user-attachments/assets/a0bb6510-6b14-4bff-97ba-be6176d4265e" />
Baris 1: Mendefinisikan fungsi sequential_search_sentinel dengan parameter data, n, dan target.  
Baris 2: Menambahkan nilai target ke akhir list sebagai sentinel (penanda akhir pencarian).  
Baris 3: Menginisialisasi variabel i dengan nilai 0 sebagai indeks awal pencarian.  
Baris 4: Melakukan perulangan selama elemen pada indeks i belum sama dengan target.  
Baris 5: Menambah nilai indeks i sebanyak 1 untuk melanjutkan pencarian ke elemen berikutnya.  
Baris 6: Menghapus kembali elemen sentinel yang sebelumnya ditambahkan ke akhir list.  
Baris 7: Memeriksa apakah indeks i masih kurang dari jumlah data asli (n).  
Baris 8: Mengembalikan nilai True dan indeks i jika target ditemukan di dalam data asli.  
Baris 9: Menjalankan kondisi alternatif jika target tidak ditemukan.  
Baris 10: Mengembalikan nilai False dan -1 sebagai tanda bahwa target tidak ditemukan dalam data.  

Fungsi Main  
Fungsi utama dalam program untuk menerima input data nomor plat mobil, menyimpan data ke dalam list, lalu mencari nomor plat menggunakan metode Sequential Search Sentinel.
 <img width="1496" height="1318" alt="fungsi main" src="https://github.com/user-attachments/assets/1c306889-a14b-42a0-b4a9-7f8a4cc91c3e" />
Baris 1: Mendefinisikan fungsi main().  
Baris 2: Membuat list kosong bernama data untuk menyimpan nomor plat mobil.  
Baris 3: Memulai blok try untuk menangani kemungkinan kesalahan input.  
Baris 4: Meminta pengguna memasukkan jumlah mobil pada parkiran lalu mengubah input menjadi tipe integer.  
Baris 5: Memeriksa apakah jumlah mobil kurang dari atau sama dengan 0.  
Baris 6: Menampilkan pesan bahwa jumlah mobil harus lebih dari 0.  
Baris 7: Menghentikan fungsi menggunakan return jika input tidak valid.  
Baris 8: Menangani kesalahan ValueError jika input bukan angka.  
Baris 9: Menampilkan pesan bahwa input harus berupa angka yang valid.  
Baris 10: Menghentikan fungsi menggunakan return jika terjadi kesalahan input.  
Baris 11: Menampilkan teks pemberitahuan untuk memasukkan nomor plat mobil.  
Baris 12: Membuat variabel plat dengan list kosong.  
Baris 13: Melakukan perulangan sebanyak jumlah mobil (n).  
Baris 14: Meminta pengguna memasukkan nomor plat mobil ke-i+1.  
Baris 15: Menambahkan nomor plat yang diinput ke dalam list data.  
Baris 16: Menampilkan seluruh data nomor plat mobil yang tersimpan pada list data.  
Baris 17: Memulai perulangan tak terbatas menggunakan while True.  
Baris 18: Memulai blok try untuk menangani kemungkinan kesalahan input pencarian.  
Baris 19: Meminta pengguna memasukkan nomor plat mobil yang ingin dicari.  
Baris 20: Menghentikan perulangan while jika input berhasil diterima.  
Baris 21: Menangani kesalahan ValueError.  
Baris 22: Menampilkan pesan bahwa input tidak valid.  
Baris 23: Memanggil fungsi sequential_search_sentinel(data, n, target) untuk mencari nomor plat mobil.  
Baris 24: Memeriksa apakah data ditemukan (found bernilai True).  
Baris 25: Menampilkan pesan bahwa nomor plat ditemukan beserta indeksnya.  
Baris 26: Menjalankan kondisi alternatif jika nomor plat tidak ditemukan.  
Baris 27: Menampilkan pesan bahwa nomor plat tidak ditemukan.  
