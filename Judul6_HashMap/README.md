PROGRAM SISTEM ID DALAM GAME  
Program ini merupakan aplikasi pencarian dan pengelolaan ID pemain Mobile Legends menggunakan struktur data Hash Map dengan metode Open Addressing. Data pemain disimpan dalam bentuk pasangan ID (key) dan nickname (value). Hash Map ini menggunakan metode linear probing untuk menangani collision agar proses penyimpanan dan pencarian data tetap berjalan dengan baik.  

PENJELASAN KODE  
<img width="1816" height="5498" alt="output tugas akhir" src="https://github.com/user-attachments/assets/6629dcca-df49-41aa-b6ed-6df5617ea9e7" />  
Baris 1: Mendefinisikan class SlotState untuk menyimpan status setiap slot pada Hash Map.  
Baris 2: Membuat konstanta EMPTY bernilai 0 yang menandakan slot kosong.  
Baris 3: Membuat konstanta OCCUPIED bernilai 1 yang menandakan slot berisi data.  
Baris 4: Membuat konstanta DELETED bernilai 2 yang menandakan data sudah dihapus tetapi slot masih dipertahankan.  
Baris 7: Mendefinisikan class Entry yang digunakan untuk menyimpan pasangan data key dan value.  
Baris 8: Membuat constructor __init__() yang dijalankan otomatis saat objek Entry dibuat.  
Baris 9: Menginisialisasi atribut key dengan nilai awal None.  
Baris 10: Menginisialisasi atribut value dengan nilai awal None.  
Baris 11: Menginisialisasi atribut state dengan nilai SlotState.EMPTY.  
Baris 14: Mendefinisikan class HashMapOpenAddressing sebagai implementasi Hash Map menggunakan metode Open Addressing.  
Baris 15: Membuat constructor __init__(self, size=10) dengan ukuran default tabel sebesar 10 slot.  
Baris 16: Menyimpan ukuran tabel ke atribut SIZE.  
Baris 17: Membuat list table yang berisi 10 objek Entry.  
Baris 19: Mendefinisikan method hash_function() untuk menghitung indeks penyimpanan berdasarkan key.  
Baris 20: Mengembalikan hasil hash menggunakan rumus (key % self.SIZE + self.SIZE) % self.SIZE  
Baris 22: Mendefinisikan method insert(key, value) untuk menambahkan data ke Hash Map.  
Baris 23: Menyimpan hasil hash_function(key) ke variabel idx.  
Baris 24: Membuat variabel first_deleted dengan nilai awal -1.  
Baris 25: Melakukan perulangan probing sebanyak ukuran tabel menggunakan variabel step.  
Baris 26: Menghitung indeks probing dan menyimpannya pada variabel i.  
Baris 27: Memeriksa apakah slot pada self.table[i] berstatus OCCUPIED.  
Baris 28: Memeriksa apakah key pada slot sama dengan key yang akan dimasukkan.  
Baris 29: Memperbarui nilai value jika key sudah ada.  
Baris 30: Mengembalikan nilai True.  
Baris 31: Memeriksa apakah slot berstatus DELETED.  
Baris 32: Memastikan belum ada slot DELETED yang disimpan.  
Baris 33: Menyimpan indeks slot DELETED pertama ke variabel first_deleted.  
Baris 35: Menangani kondisi jika ditemukan slot kosong (EMPTY).  
Baris 36: Memeriksa apakah sebelumnya ditemukan slot DELETED.  
Baris 37: Menggunakan slot DELETED sebagai tempat penyimpanan baru.  
Baris 38: Menyimpan parameter key ke atribut self.table[i].key.  
Baris 39: Menyimpan parameter value ke atribut self.table[i].value.  
Baris 40: Mengubah status slot menjadi SlotState.OCCUPIED.  
Baris 41: Mengembalikan nilai True.  
Baris 42: Memeriksa apakah terdapat slot DELETED setelah probing selesai.  
Baris 43: Menyimpan key ke slot first_deleted.  
Baris 44: Menyimpan value ke slot first_deleted.  
Baris 45: Mengubah status slot menjadi OCCUPIED.  
Baris 46: Mengembalikan nilai True.  
Baris 47: Mengembalikan nilai False jika tabel penuh.  
Baris 49: Mendefinisikan method search(key) untuk mencari data berdasarkan key.  
Baris 50: Menghitung indeks awal dan menyimpannya ke variabel idx.  
Baris 51: Melakukan probing menggunakan variabel step.  
Baris 52: Menghitung indeks probing dan menyimpannya ke variabel i.  
Baris 53: Memeriksa apakah slot berstatus EMPTY.  
Baris 54: Mengembalikan None karena data tidak ditemukan.  
Baris 55: Memeriksa apakah slot berstatus OCCUPIED dan key sesuai.  
Baris 56: Mengembalikan objek Entry yang ditemukan.  
Baris 57: Mengembalikan None jika data tidak ditemukan setelah seluruh probing selesai.  
Baris 59: Mendefinisikan method remove_key(key) untuk menghapus data berdasarkan key.  
Baris 60: Mencari data menggunakan method search(key) dan menyimpannya ke variabel entry.  
Baris 61: Memeriksa apakah data tidak ditemukan.  
Baris 62: Mengembalikan nilai False.  
Baris 63: Mengubah status data menjadi SlotState.DELETED.  
Baris 64: Mengembalikan nilai True.  
Baris 66: Mendefinisikan method display() untuk menampilkan seluruh isi Hash Map.  
Baris 67: Menampilkan judul "List ID Player".  
Baris 68: Melakukan perulangan dari indeks 0 sampai 9 menggunakan variabel i.  
Baris 69: Menampilkan nomor indeks slot.  
Baris 70: Memeriksa apakah slot berstatus EMPTY.  
Baris 71: Menampilkan tulisan "EMPTY".  
Baris 72: Memeriksa apakah slot berstatus DELETED.  
Baris 73: Menampilkan tulisan "DELETED".  
Baris 75: Menampilkan pasangan data key dan value yang tersimpan pada slot.  
Baris 78: Mendefinisikan fungsi utama program bernama main().  
Baris 79: Membuat objek hashmap dari class HashMapOpenAddressing.  
Baris 80: Menambahkan data player dengan ID 996745429 dan nickname "MuradStein.".  
Baris 81: Menambahkan data player dengan ID 230922394 dan nickname "Mitz".  
Baris 82: Menambahkan data player dengan ID 112233440 dan nickname "Mixue".  
Baris 83: Menambahkan data player dengan ID 321654987 dan nickname "Ranger Hitam".  
Baris 84: Menambahkan data player dengan ID 110100110 dan nickname "Winatak".  
Baris 85: Menambahkan data player dengan ID 999999999 dan nickname "somay lemon".  
Baris 87: Membuat variabel pilih dengan nilai awal 0.  
Baris 88: Membuat perulangan selama nilai pilih tidak sama dengan 5.  
Baris 89: Menampilkan judul menu "=== Menu Searching ID Mobile Legends ===".  
Baris 90: Menampilkan pilihan menu "1. Tampilkan list ID".  
Baris 91: Menampilkan pilihan menu "2. Cari ID".  
Baris 92: Menampilkan pilihan menu "3. Tambah ID".  
Baris 93: Menampilkan pilihan menu "4. Hapus ID".  
Baris 94: Menampilkan pilihan menu "5. Keluar".  
Baris 95: Memulai blok try.  
Baris 96: Meminta pengguna memasukkan pilihan menu dan menyimpannya ke variabel pilih.  
Baris 97: Menangkap kesalahan ValueError.  
Baris 98: Menampilkan pesan "Input tidak valid!".  
Baris 99: Kembali ke awal perulangan.  
Baris 100: Memeriksa apakah pengguna memilih menu 1.  
Baris 101: Memanggil method hashmap.display() untuk menampilkan seluruh isi Hash Map.  
Baris 102: Memeriksa apakah pengguna memilih menu 2.  
Baris 103: Memulai blok try.  
Baris 104: Meminta input nomor ID dan menyimpannya ke variabel cari_id.  
Baris 105: Mencari data menggunakan hashmap.search(cari_id) dan menyimpan hasilnya ke variabel hasil.  
Baris 106: Memeriksa apakah data ditemukan.  
Baris 107: Menampilkan ID menggunakan hasil.key dan nickname menggunakan hasil.value.  
Baris 108: Menangani kondisi jika data tidak ditemukan.  
Baris 109: Menampilkan pesan "Nomor ID tidak ditemukan!".  
Baris 110: Menangkap kesalahan ValueError.  
Baris 111: Menampilkan pesan "Input id harus angka!".  
Baris 112: Memeriksa apakah pengguna memilih menu 3.  
Baris 113: Memulai blok try.  
Baris 114: Meminta input nomor ID player dan menyimpannya ke variabel tambah_id.  
Baris 115: Meminta input nickname player dan menyimpannya ke variabel tambah_nick.  
Baris 116: Menambahkan data menggunakan hashmap.insert(tambah_id, tambah_nick).  
Baris 117: Menampilkan pesan bahwa ID berhasil ditambahkan.  
Baris 118: Menangkap kesalahan ValueError.  
Baris 119: Menampilkan pesan "Input id harus angka!".  
Baris 120: Memeriksa apakah pengguna memilih menu 4.  
Baris 121: Memulai blok try.  
Baris 122: Meminta nomor ID yang akan dihapus dan menyimpannya ke variabel hapus_id.  
Baris 123: Mencari data menggunakan hashmap.search(hapus_id) dan menyimpannya ke variabel hapus.  
Baris 124: Memeriksa apakah data ditemukan.  
Baris 125: Memanggil method hashmap.remove_key(hapus_id) untuk menghapus data.  
Baris 126: Menampilkan pesan bahwa ID berhasil dihapus.  
Baris 127: Menangani kondisi jika data tidak ditemukan.  
Baris 128: Menampilkan pesan bahwa nomor ID tidak ditemukan.  
Baris 129: Menangkap kesalahan ValueError.  
Baris 130: Menampilkan pesan "input ID harus angka".  
Baris 131: Memeriksa apakah pengguna memilih menu 5.  
Baris 132: Menampilkan pesan "Program selesai".  
Baris 133: Menangani pilihan selain 1, 2, 3, 4, dan 5.  
Baris 134: Menampilkan pesan "Pilihan tidak valid".  
Baris 137: Memeriksa apakah file dijalankan secara langsung menggunakan kondisi if __name__ == "__main__".  
Baris 138: Memanggil fungsi main() sehingga program mulai dijalankan.  


PENJELASAN OUTPUT  
<img width="329" height="604" alt="output tugas akhir png" src="https://github.com/user-attachments/assets/7dd0a1df-cb04-4a6f-a5d8-ad12745eeb2b" />  
Berdasarkan output yang ditampilkan, saat user memilih menu Tampilkan List ID, program menampilkan seluruh data pemain beserta posisi penyimpanannya di dalam tabel Hash Map. Beberapa data berada pada indeks yang berbeda dari hasil hash awal karena terjadi collision, sehingga program perlu menggunakan linear probing untuk mencari slot kosong berikutnya. Pada menu Cari ID, pengguna memasukkan ID 996745429 dan program berhasil menemukan nickname MuradStein. Pada menu Tambah ID, data baru dengan ID 123456 dan nickname cyo berhasil disimpan ke dalam Hash Map. Kemudian pada menu Hapus ID, data dengan ID 123456 berhasil dihapus dan mengubah status slot menjadi DELETED.
