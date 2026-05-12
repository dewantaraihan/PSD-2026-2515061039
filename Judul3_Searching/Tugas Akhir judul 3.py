def sequential_search_sentinel(data, n, target): 
    data.append(target) 
    i = 0 
    while data[i] != target: 
        i += 1 
    data.pop() 
    if i < n: 
        return True, i 
    else: 
        return False, -1
    

def main(): 
    data = [] 
    try:
        n = int(input("Masukkan jumlah mobil pada parkiran: "))
        if n <= 0:
            print("Jumlah mobil harus lebih dari 0!")
            return       
    except ValueError:
            print("Masukkan angka yang valid!")
            return
    print("\nMasukkan nomor plat mobil:")
    plat = []
    for i in range(n):
        plat = input(f"Nomor plat ke-{i+1}: ")
        data.append(plat)
    print(f"Data nomor plat mobil pada parkiran: {data}") 
    while True:
        try: 
            target = input("Masukkan nomor plat mobil yang ingin dicari: ") 
            break 
        except ValueError: 
            print("Input tidak valid, silakan masukkan angka!") 
    found, index = sequential_search_sentinel(data, n, target) 
    if found: 
        print(f"Plat mobil nomor {target} ditemukan pada indeks ke-{index}") 
    else: 
        print(f"Plat mobil nomor {target} tidak ditemukan") 
 
 
if __name__ == "__main__": 
    main() 