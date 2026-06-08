class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nList ID Player:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"({self.table[i].key},{self.table[i].value})")


def main():
    hashmap = HashMapOpenAddressing()
    hashmap.insert(996745429, "MuradStein.")
    hashmap.insert(230922394, "Mitz")
    hashmap.insert(112233440, "Mixue")
    hashmap.insert(321654987, "Ranger Hitam")
    hashmap.insert(110100110, "Winatak")
    hashmap.insert(999999999, "somay lemon")
    
    pilih = 0
    while pilih != 5:
        print("\n=== Menu Searching ID Mobile Legends ===")
        print("1. Tampilkan list ID")
        print("2. Cari ID")
        print("3. Tambah ID")
        print("4. Hapus ID")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            hashmap.display()
        elif pilih == 2:
            try:
                cari_id = int(input("Masukkan nomor ID yang ingin dicari: "))    
                hasil = hashmap.search(cari_id)
                if hasil is not None:
                    print(f"ID dengan nomor {hasil.key} ditemukan dengan nickname {hasil.value}")
                else:
                     print("Nomor ID tidak ditemukan!")
            except ValueError:
                print("Input id harus angka!")
        elif pilih == 3:
            try:
                tambah_id = int(input("Masukkan nomor ID player: "))
                tambah_nick = input("Masukkan Nickname player: ")
                hashmap.insert(tambah_id, tambah_nick)
                print(f"ID {tambah_id} berhasil ditambahkan")
            except ValueError:
                print("Input id harus angka!")
        elif pilih == 4:
            try:
                hapus_id = int(input("Masukkan nomor ID yang ingin dihapus: "))
                hapus = hashmap.search(hapus_id)
                if hapus is not None:
                    hashmap.remove_key(hapus_id)
                    print(f"Nomor ID {hapus_id} berhasil dihapus")
                else:
                     print(f"Nomor ID {hapus_id} tidak ditemukan!")
            except ValueError:
                print("input ID harus angka")
        elif pilih == 5:
            print("Program selesai")
        else:
            print("Pilihan tidak valid")    


if __name__ == "__main__":
    main()
