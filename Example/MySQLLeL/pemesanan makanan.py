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

# Example usage
display_menu()
manage_pesanan(1, 2, 3, '2022-01-01')
calculate_total_pembayaran(1)
