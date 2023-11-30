import pymongo

# Koneksi ke database MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["toko_makanan"]
collection = db["menu_makanan"]

# Fungsi untuk menampilkan menu makanan
def tampilkan_menu():
    print("Menu Makanan:")
    for menu in collection.find():
        print(f"{menu['nama']} - Rp {menu['harga']}")

# Fungsi untuk menambahkan menu makanan
def tambahkan_menu():
    nama = input("Masukkan nama makanan: ")
    harga = int(input("Masukkan harga makanan: "))

    menu = {"nama": nama, "harga": harga}
    collection.insert_one(menu)
    print("Menu makanan berhasil ditambahkan.")

# Fungsi untuk menghapus menu makanan
def hapus_menu():
    nama = input("Masukkan nama makanan yang ingin dihapus: ")

    query = {"nama": nama}
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        print("Menu makanan berhasil dihapus.")
    else:
        print("Menu makanan tidak ditemukan.")

# Fungsi untuk mengupdate harga menu makanan
def update_harga():
    nama = input("Masukkan nama makanan yang ingin diupdate harganya: ")
    harga_baru = int(input("Masukkan harga baru: "))

    query = {"nama": nama}
    new_values = {"$set": {"harga": harga_baru}}
    result = collection.update_one(query, new_values)
    if result.modified_count > 0:
        print("Harga menu makanan berhasil diupdate.")
    else:
        print("Menu makanan tidak ditemukan.")

# Fungsi untuk mencari menu makanan berdasarkan harga
def cari_menu():
    harga_min = int(input("Masukkan harga minimum: "))
    harga_max = int(input("Masukkan harga maksimum: "))

    query = {"harga": {"$gte": harga_min, "$lte": harga_max}}
    menus = collection.find(query)
    if menus.count() > 0:
        print("Menu Makanan:")
        for menu in menus:
            print(f"{menu['nama']} - Rp {menu['harga']}")
    else:
        print("Menu makanan tidak ditemukan.")

# Fungsi untuk menghitung total harga pesanan
def hitung_total_harga(pesanan):
    total_harga = 0
    for item in pesanan:
        menu = collection.find_one({"nama": item})
        if menu:
            total_harga += menu["harga"]
    return total_harga

# Contoh penggunaan fungsi-fungsi di atas
while True:
    print("\n=== Toko Makanan ===")
    print("1. Tampilkan Menu")
    print("2. Tambahkan Menu")
    print("3. Hapus Menu")
    print("4. Update Harga")
    print("5. Cari Menu Berdasarkan Harga")
    print("6. Hitung Total Harga Pesanan")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        tampilkan_menu()
    elif pilihan == "2":
        tambahkan_menu()
    elif pilihan == "3":
        hapus_menu()
    elif pilihan == "4":
        update_harga()
    elif pilihan == "5":
        cari_menu()
    elif pilihan == "6":
        pesanan = input("Masukkan pesanan (pisahkan dengan koma): ").split(",")
        total_harga = hitung_total_harga(pesanan)
        print(f"Total harga pesanan: Rp {total_harga}")
    elif pilihan == "0":
        break
    else:
        print("Pilihan tidak valid.")

print("Terima kasih telah menggunakan program toko makanan.")
