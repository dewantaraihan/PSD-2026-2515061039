def menu():
    print("\n=== MENU UTAMA ===")
    print("1. Lihat Jadwal")
    print("2. Tambah Jadwal")
    print("3. Hapus Jadwal")
    print("4. Keluar")


def lihat_jadwal(list_hari, list_jadwal):
    kosong = True
    print("\n=== JADWAL KULIAH ===")
    for i in range(len(list_hari)):
        if list_jadwal[i] != []:
            kosong = False
            print(f"{list_hari[i]}:")
            for j in range(len(list_jadwal[i])):
                print(f"  {j}. {list_jadwal[i][j]}")
    if kosong:
        print("Jadwal masih kosong.")


def tambah_jadwal(list_hari, list_jadwal):
    print("\n=== PANDUAN INPUT HARI ===")
    for i in range(len(list_hari)):
        print(f"{i} = {list_hari[i]}")

    try:
        index = int(input("Pilih hari (0-6): "))
    except ValueError:
        print("Input harus angka!")
        return

    if index < 0 or index >= len(list_hari):
        print("Indeks hari tidak valid!")
        return

    matkul = input("Masukkan mata kuliah: ")
    list_jadwal[index].append(matkul)

    print(f"Jadwal {matkul} berhasil ditambahkan ke hari {list_hari[index]}!")


def hapus_jadwal(list_hari, list_jadwal):
    print("\n=== PANDUAN INPUT HARI ===")
    for i in range(len(list_hari)):
        print(f"{i} = {list_hari[i]}")

    try:
        index = int(input("Pilih hari (0-6): "))
    except ValueError:
        print("Input harus angka!")
        return

    if index < 0 or index >= len(list_hari):
        print("Indeks hari tidak valid!")
        return

    if list_jadwal[index] == []:
        print("Tidak ada jadwal di hari tersebut.")
        return

    print(f"\nJadwal hari {list_hari[index]}:")
    for i in range(len(list_jadwal[index])):
        print(f"{i}. {list_jadwal[index][i]}")

    try:
        hapus_index = int(input("Pilih indeks yang ingin dihapus: "))
    except ValueError:
        print("Input harus angka!")
        return

    if hapus_index >= 0 and hapus_index < len(list_jadwal[index]):
        list_jadwal[index].pop(hapus_index)
        print("Jadwal berhasil dihapus!")
    else:
        print("Indeks tidak valid!")


def main():
    list_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    list_jadwal = [[] for _ in range(7)]

    running = True

    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            lihat_jadwal(list_hari, list_jadwal)

        elif choice == 2:
            tambah_jadwal(list_hari, list_jadwal)

        elif choice == 3:
            hapus_jadwal(list_hari, list_jadwal)

        elif choice == 4:
            print("Program selesai.")
            running = False

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()