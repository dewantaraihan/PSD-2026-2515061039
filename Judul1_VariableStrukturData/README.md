

## IMPLEMENTASI STRUKTUR DATA LIST PADA PROGRAM JADWAL KULIAH
## DESKRIPSI SINGKAT
Program ini berfungsi sebagai sistem sederhana untuk mengelola jadwal kuliah. Pengguna dapat melihat,
menambah, dan menghapus jadwal berdasarkan hari dalam seminggu. Data hanya disimpan sementara selama
program berjalan.
Struktur data yang digunakan adalah nested list (list di dalam list). list_hari menyimpan nama hari, sedangkan
list_jadwal menyimpan daftar mata kuliah untuk tiap hari. Algoritmanya melibatkan iterasi, indexing, validasi
input, serta operasi append dan pop.

## SOURCE CODE
- Fungsi menu()
<img width="804" height="520" alt="fungsi menu" src="https://github.com/user-attachments/assets/c8582702-f450-43a3-913e-695b0ce9102c" />

def menu():  
Mendefinisikan fungsi untuk menampilkan menu utama.

print("\n=== MENU UTAMA ===")  
Menampilkan judul menu.

print("1. Lihat Jadwal")  
print("2. Tambah Jadwal")  
print("3. Hapus Jadwal")  
print("4. Keluar")  
Menampilkan opsi pilihan untuk user.


- Fungsi lihat_jadwal()
<img width="1110" height="710" alt="fungsi lihat jadwal" src="https://github.com/user-attachments/assets/97fcadf7-e68d-4d2d-8c5a-a2f19cce7322" />

def lihat_jadwal(list_hari, list_jadwal):  
Menerima dua parameter: list_hari dan list_jadwal.

kosong = True  
Untuk mengecek apakah semua jadwal kosong.

print("\n=== JADWAL KULIAH ===")  
Menampilkan judul.

for i in range(len(list_hari)):  
Loop untuk semua hari (indeks 0–6).

if list_jadwal[i] != []:  
Cek apakah hari tersebut punya jadwal.

kosong = False  
Jika ada isi, berarti tidak kosong.

print(f"{list_hari[i]}:")  
Tampilkan nama hari.

for j in range(len(list_jadwal[i])):  
Loop semua mata kuliah di hari tersebut.

print(f"  {j}. {list_jadwal[i][j]}")  
Tampilkan indeks dan nama mata kuliah.

if kosong:  
  print("Jadwal masih kosong.")  
Jika tidak ada jadwal sama sekali, program akan menampilkan “Jadwal masih kosong”.


- Fungsi tambah_jadwal()
<img width="1496" height="1052" alt="fungsi tambah jadwal" src="https://github.com/user-attachments/assets/437d0709-dc10-48d2-9435-a0aa4f467eb1" />

def tambah_jadwal(list_hari, list_jadwal):  
Fungsi untuk menambah data dari input ke list_jadwal.

print("\n=== PANDUAN INPUT HARI ===")  
for i in range(len(list_hari)):  
  print(f"{i} = {list_hari[i]}")  
Menampilkan panduan indeks hari.

try:  
index = int(input("Pilih hari (0-6): "))  
Meminta user memilih hari dalam bentuk angka.


except ValueError:  
  print("Input harus angka!")  
Menangani jika user input non-angka.

if index < 0 or index >= len(list_hari):  
  print("Indeks hari tidak valid!")  
Menangani agar indeks tidak keluar batas.

matkul = input("Masukkan mata kuliah: ")  
Input nama mata kuliah.

list_jadwal[index].append(matkul)  
Menambahkan input matkul dari user ke list sesuai hari.

print(f"Jadwal {matkul} berhasil ditambahkan ke hari {list_hari[index]}")  
Konfirmasi ke user.


- Fungsi hapus_jadwal()
<img width="1372" height="1622" alt="fungsi hapus jadwal" src="https://github.com/user-attachments/assets/a210df61-c263-47ed-b849-4a84cb6f889c" />


def hapus_jadwal(list_hari, list_jadwal):  
Fungsi untuk menghapus data.

print("\n=== PANDUAN INPUT HARI ===")  
for i in range(len(list_hari)):  

   print(f"{i} = {list_hari[i]}")  
Menampilkan panduan indeks hari.

try:  
  index = int(input("Pilih hari (0-6): "))  
Meminta user memilih hari dalam bentuk angka.

except ValueError:  
  print("Input harus angka!")  
Menangani jika user input non-angka.

if index < 0 or index >= len(list_hari):  
  print("Indeks hari tidak valid!")  
Menangani agar indeks tidak keluar batas.

if list_jadwal[index] == []:  
  print("Tidak ada jadwal di hari tersebut.")  
Cek apakah jadwal di hari tersebut kosong.

print(f"\nJadwal hari {list_hari[index]}:")  
for i in range(len(list_jadwal[index])):  
  print(f"{i}. {list_jadwal[index][i]}")  
Menampilkan jadwal pada hari tersebut

try:  
  hapus_index = int(input("Pilih indeks yang ingin dihapus: "))  
User memilih jadwal yang ingin dihapus.

except ValueError:  
  print("Input harus angka!")  
Menangani jika user input non angka

if hapus_index >= 0 and hapus_index < len(list_jadwal[index]):  
Menangani agar indeks tidak keluar batas

list_jadwal[index].pop(hapus_index)  
print("Jadwal berhasil dihapus!")  
Menghapus data berdasarkan indeks.

else:  
  print("Indeks tidak valid!")  
Validasi jika indeks salah.


- Fungsi main()
<img width="1542" height="1394" alt="fungsi main" src="https://github.com/user-attachments/assets/3c749b09-4f83-4b7d-adc2-b027810fdf25" />


list_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]  
Inisialisasi hari.

list_jadwal = [[] for _ in range(7)]  
Membuat list kosong untuk tiap hari (nested list).

running = True  
Untuk kontrol loop program.


while running:  
  menu()  
Loop utama program untuk memanggil fungsi menu(menu terus berjalan).

try:  
  choice = int(input("Pilihan: "))  
Input pilihan menu.

except ValueError:  
  print("Masukkan angka yang valid!")  
Untuk menangani input non angka

if choice == 1:  
Menjalankan fungsi lihat_jadwal.
elif choice == 2:  
Menjalankan fungsi tambah_jadwal.
elif choice == 3:  
Menjalankan fungsi hapus_jadwal.
elif choice == 4:  
running = False  
Menghentikan program.
else:  
  print("Pilihan tidak valid!")  
Menangani input diluar panduan.


- Jalankan program
<img width="696" height="368" alt="main()" src="https://github.com/user-attachments/assets/adff8d8d-3c4f-4707-be2a-14b8daa07149" />


if __name__ == "__main__":  
  main()  
Menjalankan program hanya jika file dieksekusi langsung. Program akan memanggil fungsi main().



## OUTPUT PROGRAM


## === MENU UTAMA ===
## 1. Lihat Jadwal
## 2. Tambah Jadwal
## 3. Hapus Jadwal
## 4. Keluar
## Pilihan: 2

## Penjelasan:  
Program pertama kali menampilkan menu dari fungsi menu().  
User memasukkan 2, artinya memilih fitur Tambah Jadwal.  


## === PANDUAN INPUT HARI ===
## 0 = Senin
## 1 = Selasa
## 2 = Rabu
## 3 = Kamis
## 4 = Jumat
## 5 = Sabtu
## 6 = Minggu
## Pilih hari (0-6): 1
## Masukkan mata kuliah: RPL
## Jadwal RPL berhasil ditambahkan ke hari Selasa

## Penjelasan:  
Program menampilkan panduan indeks hari.  
User memilih:  
1  = Selasa  
Mata kuliah: RPL  
Data disimpan ke:  
list_jadwal[1] = ["RPL"]  


## === MENU UTAMA ===
## 1. Lihat Jadwal
## 2. Tambah Jadwal
## 3. Hapus Jadwal
## 4. Keluar
## Pilihan: 2

## Penjelasan:  
Program kembali ke menu utama (loop while).  
User memilih lagi 2 (Tambah Jadwal).  



## === PANDUAN INPUT HARI ===
## 0 = Senin
## 1 = Selasa
## 2 = Rabu
## 3 = Kamis
## 4 = Jumat
## 5 = Sabtu
## 6 = Minggu
## Pilih hari (0-6): 1
## Masukkan mata kuliah: Struktur Data
## Jadwal Struktur Data berhasil ditambahkan ke hari Selasa

## Penjelasan:
User kembali memilih:  
Hari: 1 (Selasa)  
Mata kuliah: Struktur Data  
Data sekarang:  
list_jadwal[1] = ["RPL", "Struktur Data"]  


## === MENU UTAMA ===
## 1. Lihat Jadwal
## 2. Tambah Jadwal
## 3. Hapus Jadwal
## 4. Keluar
## Pilihan: 1

## Penjelasan:
User memilih 1 (Lihat Jadwal).  


## === JADWAL KULIAH ===
## Selasa:
## 0. RPL
## 1. Struktur Data

## Penjelasan:
Program melakukan loop seluruh hari.  
Hanya Selasa yang memiliki isi.  
Indeks ditampilkan:  
0 = RPL
1 = Struktur Data


## === MENU UTAMA ===
## 1. Lihat Jadwal
## 2. Tambah Jadwal
## 3. Hapus Jadwal
## 4. Keluar
## Pilihan: 3

## Penjelasan:
User memilih 3 (Hapus Jadwal).  


## === PANDUAN INPUT HARI ===
## 0 = Senin
## 1 = Selasa
## 2 = Rabu
## 3 = Kamis
## 4 = Jumat
## 5 = Sabtu
## 6 = Minggu
## Pilih hari (0-6): 1

## Penjelasan:
User memilih Selasa (1).  


## Jadwal hari Selasa:
## 0. RPL
## 1. Struktur Data
## Pilih indeks yang ingin dihapus: 0
## Jadwal berhasil dihapus

## Penjelasan:
Program menampilkan semua jadwal di hari tersebut.  
User memilih:  
Index 0 = RPL  
Proses:  
list_jadwal[1].pop(0)  
Data sekarang:  
["Struktur Data"]  


## === MENU UTAMA ===
## 1. Lihat Jadwal
## 2. Tambah Jadwal
## 3. Hapus Jadwal
## 4. Keluar
## Pilihan: 1

## Penjelasan:
User memilih kembali Lihat Jadwal.  


## === JADWAL KULIAH ===
## Selasa:
## 0. Struktur Data

## Penjelasan:
Data sudah diperbarui.  
Indeks otomatis berubah.  
Struktur Data sekarang di index 0.  


## === MENU UTAMA ===
## 1. Lihat Jadwal
## 2. Tambah Jadwal
## 3. Hapus Jadwal
## 4. Keluar
## Pilihan: 4
## Program selesai.

## Penjelasan:
User memilih 4 (Keluar).  
running = False → loop berhenti.  
Program selesai.  
