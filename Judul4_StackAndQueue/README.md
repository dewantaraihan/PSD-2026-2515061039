PROGRAM SISTEM PRE-MOVE DALAM GAME CATUR  

Program ini merupakan program yang menerapkan struktur data queue menggunakan Linked List untuk sistem pre-move pada game catur digital. Program bekerja dengan konsep FIFO (First In First Out), sehingga langkah yang pertama dimasukkan akan dijalankan lebih dulu. Class Node digunakan untuk menyimpan data langkah catur, sedangkan class QueueLinkedList mengatur operasi queue seperti menambah langkah (enqueue), menjalankan langkah terdepan (dequeue), melihat langkah terdepan (peek), dan menampilkan seluruh antrean (display).  

PENJELASAN KODE  
<img width="1356" height="3522" alt="Kode" src="https://github.com/user-attachments/assets/702491ae-c856-4c2a-9a1e-3c4b8627dc84" />
Baris 1: Mendefinisikan class Node untuk membuat node pada linked list.  
Baris 2: Membuat constructor __init__ saat objek node dibuat.  
Baris 3: Menyimpan data ke dalam node.  
Baris 4: Mengatur pointer next menjadi None karena belum terhubung ke node lain.  
Baris 5: Baris kosong untuk merapikan kode.  
Baris 6: Baris kosong.  
Baris 7: Mendefinisikan class QueueLinkedList untuk membuat queue menggunakan linked list.  
Baris 8: Membuat constructor class queue.  
Baris 9: front_ptr menunjuk elemen paling depan queue, awalnya kosong (None).  
Baris 10: rear_ptr menunjuk elemen paling belakang queue, awalnya kosong (None).  
Baris 11: Baris kosong.  
Baris 12: Mendefinisikan fungsi is_empty() untuk mengecek apakah queue kosong.  
Baris 13: Mengembalikan nilai True jika front_ptr kosong.  
Baris 14: Baris kosong.  
Baris 15: Mendefinisikan fungsi enqueue() untuk menambah data ke queue.  
Baris 16: Membuat node baru dari data move.  
Baris 17: Mengecek apakah queue kosong.  
Baris 18: Jika kosong, front_ptr diarahkan ke node baru.  
Baris 19: rear_ptr juga diarahkan ke node baru.  
Baris 20: Jika queue tidak kosong.  
Baris 21: Node terakhir dihubungkan ke node baru.  
Baris 22: rear_ptr dipindahkan ke node baru.  
Baris 23: Menampilkan pesan bahwa pre-move berhasil ditambahkan.  
Baris 24: Baris kosong.  
Baris 25: Mendefinisikan fungsi dequeue() untuk menghapus data paling depan.  
Baris 26: Mengecek apakah queue kosong.  
Baris 27: Menampilkan pesan jika antrean kosong.  
Baris 28: Menghentikan fungsi dengan return.  
Baris 29: Menyimpan node paling depan ke variabel sementara temp.  
Baris 30: Menampilkan data pre-move yang dijalankan.  
Baris 31: front_ptr dipindahkan ke node berikutnya.  
Baris 32: Mengecek apakah queue menjadi kosong setelah dequeue.  
Baris 33: Jika kosong, rear_ptr diubah menjadi None.  
Baris 34: Baris kosong.  
Baris 35: Mendefinisikan fungsi peek() untuk melihat data paling depan.  
Baris 36: Mengecek apakah queue kosong.  
Baris 37: Menampilkan pesan jika queue kosong.  
Baris 38: Menghentikan fungsi.  
Baris 39: Menampilkan data paling depan queue tanpa menghapusnya.  
Baris 40: Baris kosong.  
Baris 41: Mendefinisikan fungsi display() untuk menampilkan seluruh isi queue.  
Baris 42: Mengecek apakah queue kosong.  
Baris 43: Menampilkan pesan jika queue kosong.  
Baris 44: Menghentikan fungsi.  
Baris 45: Menampilkan judul daftar antrean pre-move.  
Baris 46: Variabel current mulai dari node paling depan.  
Baris 47: Variabel nomor untuk penomoran antrean.  
Baris 48: Perulangan selama masih ada node.  
Baris 49: Menampilkan nomor dan isi data node saat ini.  
Baris 50: current dipindahkan ke node berikutnya.  
Baris 51: Menambah nomor antrean.  
Baris 52: Baris kosong.  
Baris 53: Baris kosong.  
Baris 54: Mendefinisikan fungsi utama main().  
Baris 55: Membuat objek queue dari class QueueLinkedList.  
Baris 56: Variabel pilih diisi 0 sebagai nilai awal.  
Baris 57: Perulangan menu selama pilihan bukan 5.  
Baris 58: Menampilkan judul menu program.  
Baris 59: Menampilkan menu input pre-move baru.  
Baris 60: Menampilkan menu menjalankan pre-move terdepan.  
Baris 61: Menampilkan menu melihat pre-move paling depan.  
Baris 62: Menampilkan menu melihat seluruh antrean.  
Baris 63: Menampilkan menu keluar program.  
Baris 64: Memulai blok try untuk menangani error input.  
Baris 65: Meminta user memasukkan pilihan menu.  
Baris 66: Menangani error jika input bukan angka.  
Baris 67: Menampilkan pesan error input.  
Baris 68: Mengulang kembali ke menu utama.  
Baris 69: Mengecek jika user memilih menu 1.  
Baris 70: Meminta user memasukkan langkah catur.  
Baris 71: Memasukkan langkah ke queue dengan enqueue().  
Baris 72: Jika user memilih menu 2.  
Baris 73: Menjalankan dequeue() untuk mengambil move paling depan.  
Baris 74: Jika user memilih menu 3.  
Baris 75: Menjalankan peek() untuk melihat move paling depan.  
Baris 76: Jika user memilih menu 4.  
Baris 77: Menampilkan seluruh antrean dengan display().  
Baris 78: Jika user memilih menu 5.  
Baris 79: Menampilkan pesan program selesai.  
Baris 80: Jika pilihan menu tidak sesuai.  
Baris 81: Menampilkan pesan pilihan tidak valid.  
Baris 82: Baris kosong.  
Baris 83: Baris kosong.  
Baris 84: Mengecek apakah file dijalankan langsung sebagai program utama.  
Baris 85: Menjalankan fungsi main().  

