def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        while j >= 0 and (-arr[j]["attack"], arr[j]["nama"]) > (-temp["attack"], temp["nama"]):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah item: "))
        if n <= 0:
            print("Jumlah item harus lebih dari 0!")
            return
    except ValueError:
        print("Input tidak valid!")
        return

    inventory = []

    print("\nMasukkan data item:")
    for i in range(n):
        nama = input(f"Nama item ke-{i+1}: ")

        while True:
            try:
                attack = int(input(f"Nilai attack item ke-{i+1}: "))
                break
            except ValueError:
                print("Nilai attack harus berupa angka!")

        inventory.append({
            "nama": nama,
            "attack": attack
        })

    print("\nSebelum sorting:")
    for item in inventory:
        print(f"{item['nama']} | Attack: {item['attack']} ATK")

    insertion_sort(inventory, n)

    print("\nSetelah sorting: ")
    for item in inventory:
        print(f"{item['nama']} | Attack: {item['attack']}")


if __name__ == "__main__":
    main()