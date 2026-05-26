PROGRAM SISTEM INVENTORY DALAM GAME  
Program ini merupakan implementasi struktur data Binary Search Tree (BST) untuk mengelola inventory item dalam game. Setiap item memiliki nama dan nilai attack yang disimpan ke dalam node BST. Program menyediakan beberapa menu utama seperti menambahkan item, menghapus item, menampilkan urutan atk secara ascending, mencari nilai atk tertinggi dan terendah, serta menghitung jumlah item yang tersimpan.  


PENJELASAN KODE  
<img width="1510" height="5536" alt="Output tugas akhir" src="https://github.com/user-attachments/assets/566fe28b-719f-4d15-9e17-81305b464603" />  

baris 1: Mendefinisikan class Node untuk membuat node pada Binary Search Tree (BST).  
baris 2: Membuat constructor init yang otomatis dijalankan saat object dibuat.  
baris 3: Menyimpan nilai atk ke dalam node.  
baris 4: Menyimpan nama item ke dalam node.  
baris 5: Membuat child kiri dengan nilai awal None.  
baris 6: Membuat child kanan dengan nilai awal None.  
  
baris 8: Mendefinisikan class inventoryBST untuk mengatur BST inventory.  
baris 9: Constructor class inventoryBST.  
baris 10: Membuat root awal BST bernilai None karena tree masih kosong.  
  
baris 12: Membuat function insert_node untuk menambahkan node baru ke BST.  
baris 13: Mengecek apakah root kosong.  
baris 14: Jika kosong, membuat node baru berisi atk dan item.  
baris 15: Mengecek apakah nilai atk lebih kecil dari root.  
baris 16: Jika lebih kecil, data dimasukkan ke subtree kiri.  
baris 17: Mengecek apakah nilai atk lebih besar dari root.  
baris 18: Jika lebih besar, data dimasukkan ke subtree kanan.  
baris 19: Mengembalikan root setelah proses insert selesai.  
  
baris 21: Membuat function insert.  
baris 22: Memanggil function insert_node untuk menambahkan data ke BST.  
  
baris 24: Membuat function find_min_node untuk mencari node terkecil.  
baris 25: Menyimpan root ke variabel current.  
baris 26: Melakukan perulangan selama node kiri masih ada.  
baris 27: Berpindah ke node paling kiri.  
baris 28: Mengembalikan node dengan nilai terkecil.  
  
baris 30: Membuat function search_item untuk mencari item berdasarkan nama.  
baris 31: Mengecek apakah root kosong.  
baris 32: Jika kosong, mengembalikan None.  
baris 33: Mengecek apakah nama item sama dengan input user tanpa membedakan huruf besar dan kecil.  
baris 34: Jika ditemukan, mengembalikan node tersebut.  
baris 35: Mencari item di subtree kiri.  
baris 36: Mengecek apakah item ditemukan di kiri.  
baris 37: Jika ditemukan, mengembalikan hasil pencarian kiri.  
baris 38: Jika belum ditemukan, lanjut mencari di subtree kanan.  
  
baris 40: Membuat function delete_node untuk menghapus node.  
baris 41: Mengecek apakah root kosong.  
baris 42: Jika kosong, mengembalikan None.  
baris 43: Mengecek apakah atk lebih kecil dari root.  
baris 44: Jika lebih kecil, lanjut hapus di subtree kiri.  
baris 45: Mengecek apakah atk lebih besar dari root.  
baris 46: Jika lebih besar, lanjut hapus di subtree kanan.  
baris 47: Jika nilainya sama, berarti node ditemukan.  
baris 48: Mengecek apakah node tidak punya child kiri dan kanan.  
baris 49: Jika tidak punya child, node langsung dihapus.  
baris 50: Mengecek apakah child kiri kosong.  
baris 51: Jika kosong, node diganti dengan child kanan.  
baris 52: Mengecek apakah child kanan kosong.  
baris 53: Jika kosong, node diganti dengan child kiri.  
baris 54: Jika node punya dua child, masuk ke proses berikutnya.  
baris 55: Mencari successor atau nilai terkecil di subtree kanan.  
baris 56: Mengganti nilai atk node dengan successor.  
baris 57: Mengganti nama item node dengan successor.  
baris 58: Menghapus node successor yang tadi dipindahkan.  
baris 59: Mengembalikan root setelah proses delete selesai.  
  
baris 61: Membuat function delete.  
baris 62: Memanggil function delete_node untuk menghapus data dari BST.  
  
baris 64: Membuat traversal inorder untuk menampilkan data terurut.  
baris 65: Mengecek apakah root kosong.  
baris 66: Jika kosong, function berhenti.  
baris 67: Menampilkan subtree kiri terlebih dahulu.  
baris 68: Menampilkan nilai atk.  
baris 69: Menampilkan subtree kanan.  
  
baris 71: Membuat function find_min untuk mencari nilai terkecil.  
baris 72: Mengecek apakah tree kosong.  
baris 73: Jika kosong, mengembalikan -1.  
baris 74: Menyimpan root ke variabel current.  
baris 75: Bergerak terus ke node paling kiri.  
baris 76: Mengupdate posisi current ke child kiri.  
baris 77: Mengembalikan nilai atk terkecil.  
  
baris 79: Membuat function find_max untuk mencari nilai terbesar.  
baris 80: Mengecek apakah tree kosong.  
baris 81: Jika kosong, mengembalikan -1.  
baris 82: Menyimpan root ke variabel current.  
baris 83: Bergerak terus ke node paling kanan.  
baris 84: Mengupdate posisi current ke child kanan.  
baris 85: Mengembalikan nilai atk terbesar.  
  
baris 87: Membuat function count_nodes untuk menghitung jumlah node.  
baris 88: Mengecek apakah root kosong.  
baris 89: Jika kosong, mengembalikan 0.  
baris 90: Menghitung total node dengan rekursi kiri dan kanan lalu ditambah 1.  
  
baris 92: Membuat function utama main.  
baris 93: Membuat object inventory dari class inventoryBST.  
baris 94: Membuat variabel pilih dengan nilai awal 0.  
baris 95: Perulangan menu selama user belum memilih keluar.  
baris 96: Menampilkan judul menu inventory.  
baris 97: Menampilkan menu tambah item.  
baris 98: Menampilkan menu hapus item.  
baris 99: Menampilkan menu urutkan item.  
baris 100: Menampilkan menu item atk terendah dan tertinggi.  
baris 101: Menampilkan menu hitung jumlah item.  
baris 102: Menampilkan menu keluar.  
baris 103: Memulai blok try untuk menangani error input.  
baris 104: Meminta user memilih menu lalu diubah menjadi integer.  
baris 105: Menangkap error jika input bukan angka.  
baris 106: Menampilkan pesan input tidak valid.  
baris 107: Mengulang ke awal menu.  
  
baris 108: Mengecek apakah user memilih menu 1.  
baris 109: Meminta input nama item.  
baris 110: Memulai blok try.  
baris 111: Meminta input nilai atk.  
baris 112: Menambahkan item ke BST.  
baris 113: Menampilkan pesan berhasil tambah item.  
baris 114: Menangkap error jika atk bukan angka.  
baris 115: Menampilkan pesan bahwa atk harus angka.  
  
baris 116: Mengecek apakah user memilih menu 2.  
baris 117: Meminta nama item yang ingin dihapus.  
baris 118: Mencari item berdasarkan nama.  
baris 119: Mengecek apakah item ditemukan.  
baris 120: Menghapus item berdasarkan nilai atk.  
baris 121: Menampilkan pesan item berhasil dihapus.  
baris 122: Jika item tidak ditemukan.  
baris 123: Menampilkan pesan item tidak ditemukan.  
  
baris 124: Mengecek apakah user memilih menu 3.  
baris 125: Menampilkan tulisan “Urutan Atk”.  
baris 126: Menjalankan traversal inorder agar atk tampil terurut.  
  
baris 127: Mengecek apakah user memilih menu 4.  
baris 128: Menampilkan nilai atk terkecil.  
baris 129: Menampilkan nilai atk terbesar.  
  
baris 130: Mengecek apakah user memilih menu 5.  
baris 131: Menampilkan jumlah item dalam BST.  
  
baris 132: Mengecek apakah user memilih menu 6.  
baris 133: Menampilkan pesan program selesai.  
  
baris 134: Jika pilihan menu tidak tersedia.  
baris 135: Menampilkan pesan pilihan tidak valid.  
  
baris 137: Mengecek apakah file dijalankan langsung.  
baris 138: Menjalankan function main().  


PENJELASAN OUTPUT  
<img width="342" height="433" alt="output 1 tgs akhir" src="https://github.com/user-attachments/assets/9f1e2d23-c644-4e52-89d9-231514494703" />  
<img width="256" height="487" alt="output 2 tgs akhir" src="https://github.com/user-attachments/assets/f7abe330-800b-46c0-9f8d-0fec78e56b99" />  
Output pertama menunjukkan proses penambahan item ke dalam BST inventory. User menambahkan tiga item, yaitu Netherite Sword dengan atk 8, Trident dengan atk 7, dan Crossbow dengan atk 10. Program menyimpan data tersebut ke dalam BST berdasarkan nilai atk.Nilai yang pertama diinput menjadi root. Nilai yang lebih kecil akan masuk ke kiri, sedangkan nilai yang lebih besar masuk ke kanan.  
Saat memilih menu urutkan, program menampilkan nilai atk menggunakan traversal inorder sehingga hasilnya 7, 8, dan 10. Kemudian program menampilkan nilai atk terkecil yaitu 7 dan atk terbesar yaitu 10. Setelah itu program menghitung jumlah item dalam inventory dan menemukan total 3 item. Kemudian item Trident berhasil dihapus dari BST karena ditemukan berdasarkan nama item yang dimasukkan user.  


LINK YOUTUBE: https://youtu.be/v-G41Q1VSJ8?si=_oFqfjAJNkW1GM8o
