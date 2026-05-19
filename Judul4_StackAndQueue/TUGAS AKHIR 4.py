class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, move):
        new_node = Node(move)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node
        print(f"Pre-move '{move}' berhasil ditambahkan ke antrean.")

    def dequeue(self):
        if self.is_empty():
            print("Antrean pre-move kosong.")
            return
        temp = self.front_ptr
        print(f"Menjalankan pre-move: {temp.data}")
        self.front_ptr = self.front_ptr.next
        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Antrean pre-move kosong.")
            return
        print(f"Pre-move paling depan: {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Antrean pre-move kosong.")
            return
        print("Daftar antrean pre-move:")
        current = self.front_ptr
        nomor = 1
        while current is not None:
            print(f"{nomor}. {current.data}")
            current = current.next
            nomor += 1


def main():
    queue = QueueLinkedList()
    pilih = 0
    while pilih != 5:
        print("\n===SISTEM PRE-MOVE CATUR===")
        print("1. Input pre-move baru")
        print("2. Jalankan pre-move terdepan")
        print("3. Lihat pre-move paling depan")
        print("4. Tampilkan antrian pre-move")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue
        if pilih == 1:
            move = input("Masukkan langkah catur: ")
            queue.enqueue(move)
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            print("Program sistem pre-move selesai.")
        else:
            print("Pilihan menu tidak valid!")


if __name__ == "__main__":
    main()