import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="pemesanan_makanan"
)

# Function to display menu
def display_menu():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM menu")
    result = cursor.fetchall()
    for row in result:
        print(f"ID: {row[0]}, Nama: {row[1]}, Harga: {row[2]}")

# Function to manage pesanan
def manage_pesanan(id_pelanggan, id_menu, jumlah, tanggal):
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO pesanan (id_pelanggan, id_menu, jumlah, tanggal_pemesanan) VALUES (%s, %s, %s, %s)", (id_pelanggan, id_menu, jumlah, tanggal))
    mydb.commit()
    print("Pesanan berhasil ditambahkan")

# Function to calculate total pembayaran
def calculate_total_pembayaran(id_pelanggan):
    cursor = mydb.cursor()
    cursor.execute("SELECT SUM(menu.harga * detail_pesanan.jumlah) FROM pesanan INNER JOIN detail_pesanan ON pesanan.id_pesanan = detail_pesanan.id_pesanan INNER JOIN menu ON detail_pesanan.id_menu = menu.id_menu WHERE pesanan.id_pelanggan = %s", (id_pelanggan,))
    result = cursor.fetchone()
    total_pembayaran = result[0]
    print(f"Total pembayaran untuk pelanggan dengan ID {id_pelanggan}: {total_pembayaran}")

# Function to create a new menu item
def create_menu(nama, harga):
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO menu (nama, harga) VALUES (%s, %s)", (nama, harga))
    mydb.commit()
    print("Menu berhasil ditambahkan")

# Function to read menu items
def read_menu():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM menu")
    result = cursor.fetchall()
    for row in result:
        print(f"ID: {row[0]}, Nama: {row[1]}, Harga: {row[2]}")

# Function to update a menu item
def update_menu(id_menu, nama, harga):
    cursor = mydb.cursor()
    cursor.execute("UPDATE menu SET nama = %s, harga = %s WHERE id_menu = %s", (nama, harga, id_menu))
    mydb.commit()
    print("Menu berhasil diperbarui")

# Function to delete a menu item
def delete_menu(id_menu):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM menu WHERE id_menu = %s", (id_menu,))
    mydb.commit()
    print("Menu berhasil dihapus")

# Dynamic menu for user input
def main_menu():
    while True:
        print("=== Main Menu ===")
        print("1. Display Menu")
        print("2. Manage Pesanan")
        print("3. Calculate Total Pembayaran")
        print("4. Create Menu")
        print("5. Read Menu")
        print("6. Update Menu")
        print("7. Delete Menu")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            id_pelanggan = int(input("Enter ID Pelanggan: "))
            id_menu = int(input("Enter ID Menu: "))
            jumlah = int(input("Enter Jumlah: "))
            tanggal = input("Enter Tanggal Pemesanan: ")
            manage_pesanan(id_pelanggan, id_menu, jumlah, tanggal)
        elif choice == "3":
            id_pelanggan = int(input("Enter ID Pelanggan: "))
            calculate_total_pembayaran(id_pelanggan)
        elif choice == "4":
            nama = input("Enter Nama Menu: ")
            harga = float(input("Enter Harga Menu: "))
            create_menu(nama, harga)
        elif choice == "5":
            read_menu()
        elif choice == "6":
            id_menu = int(input("Enter ID Menu: "))
            nama = input("Enter Nama Menu: ")
            harga = float(input("Enter Harga Menu: "))
            update_menu(id_menu, nama, harga)
        elif choice == "7":
            id_menu = int(input("Enter ID Menu: "))
            delete_menu(id_menu)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
main_menu()
