class Node:
    def __init__(self, atk, item):
        self.atk = atk
        self.item = item
        self.left = None
        self.right = None

class inventoryBST:
    def __init__(self):
        self.root = None

    def insert_node(self, root, atk, item):
        if root is None:
            return Node(atk, item)

        if atk < root.atk:
            root.left = self.insert_node(root.left, atk, item)

        elif atk > root.atk:
            root.right = self.insert_node(root.right, atk, item)

        return root

    def insert(self, atk, item):
        self.root = self.insert_node(self.root, atk, item)

    def find_min_node(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current

    def search_item(self, root, nama_item):
        if root is None:
            return None
        if root.item.lower() == nama_item.lower():
            return root
        left_search = self.search_item(root.left,nama_item)
        if left_search is not None:
            return left_search
        return self.search_item(root.right,nama_item)
    
    def delete_node(self, root, atk):
        if root is None:
            return None
        if atk < root.atk:
            root.left = self.delete_node(root.left, atk)
        elif atk > root.atk:
            root.right = self.delete_node(root.right, atk)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min_node(root.right)
                root.atk = successor.atk
                root.item = successor.item
                root.right = self.delete_node(root.right, successor.atk)
        return root

    def delete(self, atk):
        self.root = self.delete_node(self.root, atk)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.atk, end=" ")
        self.inorder(root.right)

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.atk

    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.atk
    
    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
    
def main():
    inventory = inventoryBST()
    pilih = 0
    while pilih != 6:
        print("\n=== inventory ===")
        print("1. Tambah item.")
        print("2. Hapus item.")
        print("3. Urutkan Atk item.")
        print("4. Tampilkan item Atk terendah dan tertinggi.")
        print("5. Hitung jumlah item")
        print("6. Keluar")
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            nama_item = input("Masukkan nama item: ")
            try:
                atk = int(input("Masukkan nilai Atk: "))
                inventory.insert(atk, nama_item)
                print(f"Item '{nama_item}' berhasil ditambahkan!")
            except ValueError:
                print("Atk harus angka!")
        elif pilih == 2:
            nama_item = input("Masukkan nama item yang ingin dihapus: ")
            target = inventory.search_item(inventory.root,nama_item)
            if target is not None:
                inventory.delete(target.atk)
                print(f"Item '{nama_item}' berhasil dihapus")
            else:
                print("Item tidak ditemukan!")
        elif pilih == 3:
            print("Urutan Atk: ", end="")
            inventory.inorder(inventory.root)
        elif pilih == 4:
            print(f"Atk paling kecil: {inventory.find_min(inventory.root)}")
            print(f"Atk paling besar: {inventory.find_max(inventory.root)}")
        elif pilih == 5:
            print(f"Jumlah item: {inventory.count_nodes(inventory.root)}")
        elif pilih == 6:
            print("Program selesai")
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()