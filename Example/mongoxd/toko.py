from pymongo import MongoClient

# Koneksi ke database MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Fungsi untuk menampilkan menu
def show_menu():
    print("=== MENU ===")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Update data")
    print("4. Hapus data")
    print("5. Keluar")

# Fungsi untuk menambah data
def add_data():
    name = input("Masukkan nama: ")
    price = float(input("Masukkan harga: "))
    quantity = int(input("Masukkan jumlah: "))
    data = {"name": name, "price": price, "quantity": quantity}
    collection.insert_one(data)
    print("Data berhasil ditambahkan!")

# Fungsi untuk menampilkan data
def show_data():
    data = collection.find()
    for d in data:
        print(f"Nama: {d['name']}, Harga: {d['price']}, Jumlah: {d['quantity']}")

# Fungsi untuk mengupdate data
def update_data():
    name = input("Masukkan nama yang ingin diupdate: ")
    new_price = float(input("Masukkan harga baru: "))
    new_quantity = int(input("Masukkan jumlah baru: "))
    collection.update_one({"name": name}, {"$set": {"price": new_price, "quantity": new_quantity}})
    print("Data berhasil diupdate!")

# Fungsi untuk menghapus data
def delete_data():
    name = input("Masukkan nama yang ingin dihapus: ")
    collection.delete_one({"name": name})
    print("Data berhasil dihapus!")

# Fungsi utama
def main():
    while True:
        show_menu()
        choice = int(input("Pilih menu (1-5): "))

        if choice == 1:
            add_data()
        elif choice == 2:
            show_data()
        elif choice == 3:
            update_data()
        elif choice == 4:
            delete_data()
        elif choice == 5:
            print("Terima kasih!")
            break
        else:
            print("Menu tidak valid!")

if __name__ == "__main__":
    main()
