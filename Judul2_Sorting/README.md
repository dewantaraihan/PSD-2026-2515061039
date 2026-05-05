PROGRAM INSERTION SORT ITEM PADA INVENTORY GAME BERDASARKAN ATTACK

Pendahuluan
Program ini dibuat untuk mengurutkan data item dalam sistem inventory game berdasarkan nilai attack. Algoritma yang digunakan adalah insertion sort, dengan prioritas utama attack tertinggi dan jika sama maka diurutkan berdasarkan nama secara alfabet.

Fungsi insertion_sort  
Fungsi ini digunakan untuk melakukan proses pengurutan data.  
<img width="1772" height="672" alt="fungsi insertion" src="https://github.com/user-attachments/assets/ca2681c1-f13d-4fa9-8d78-147ab5bb48a1" />

Baris 1: Mendefinisikan fungsi insertion_sort dengan parameter array dan jumlah data.  
Baris 2: Perulangan dimulai dari indeks ke-1 hingga ke-(n-1) karena elemen pertama dianggap sudah terurut.  
Baris 3: Menyimpan elemen yang akan dibandingkan ke variabel sementara bernama temp.  
Baris 4: Menentukan indeks sebelumnya (j = i - 1) untuk proses perbandingan.  
Baris 6: Melakukan perulangan selama indeks masih valid dan kondisi perbandingan terpenuhi.  
Baris 7: Membandingkan data untuk menentukan urutan (attack terbesar dulu, jika sama maka nama A–Z).  
Baris 8: Mengurangi indeks j untuk melanjutkan perbandingan ke elemen sebelumnya.  
Baris 10: Menempatkan kembali elemen temp ke posisi yang sesuai setelah proses pergeseran selesai.  

Fungsi main  
Fungsi utama program untuk menginput nama item dan nilai attack.  
<img width="1356" height="1698" alt="fungsi main" src="https://github.com/user-attachments/assets/1d70e452-c2d0-41b1-a398-6931457a5dfd" />

Baris 1: Mendefinisikan fungsi main() sebagai fungsi utama program.  
Baris 2: Menggunakan blok try untuk menangani kemungkinan error saat input nilai selain integer.  
Baris 3: Meminta user memasukkan jumlah item dan mengubahnya menjadi integer.  
Baris 4: Melakukan pengecekan apakah jumlah item kurang dari atau sama dengan nol.  
Baris 5: Menampilkan pesan error jika jumlah item tidak valid.  
Baris 6: Menghentikan program menggunakan return jika input tidak sesuai.  
Baris 7: Menangani error jika input bukan angka dengan except ValueError.  
Baris 8: Menampilkan pesan bahwa input tidak valid.  
Baris 9: Menghentikan program jika terjadi kesalahan input.  
Baris 11: Membuat list kosong inventory untuk menyimpan data item.  
Baris 13: Menampilkan pesan untuk memulai input data item.  
Baris 14: Melakukan perulangan sebanyak jumlah item (n) untuk input data.  
Baris 15: Meminta user memasukkan nama item.  
Baris 17: Membuat perulangan tak terbatas untuk validasi input attack.  
Baris 18: Menggunakan blok try untuk menangani error input attack.  
Baris 19: Meminta user memasukkan nilai attack dan mengubahnya menjadi integer.  
Baris 20: Keluar dari loop jika input valid.  
Baris 21: Menangani error jika input attack bukan angka.  
Baris 22: Menampilkan pesan error jika input tidak valid.  
Baris 24: Menambahkan data item ke dalam list inventory dalam bentuk dictionary (nama dan attack).  
Baris 29: Menampilkan judul untuk data sebelum dilakukan sorting.  
Baris 30: Melakukan perulangan untuk menampilkan setiap item dalam inventory.  
Baris 31: Menampilkan nama item dan nilai attack sebelum sorting.  
Baris 33: Memanggil fungsi insertion_sort untuk mengurutkan data.  
Baris 35: Menampilkan judul untuk data setelah sorting.  
Baris 36: Melakukan perulangan untuk menampilkan data yang sudah diurutkan.  
Baris 37: Menampilkan nama item dan nilai attack setelah sorting.  

