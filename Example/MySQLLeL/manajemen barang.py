import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="manajemen_barang"
)

# Function to display all items in the database
def display_items():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM barang")
    items = cursor.fetchall()
    for item in items:
        print(item)

# Function to add a new item to the database
def add_item(nama_barang, harga, stok):
    cursor = mydb.cursor()
    sql = "INSERT INTO barang (nama_barang, harga, stok) VALUES (%s, %s, %s)"
    val = (nama_barang, harga, stok)
    cursor.execute(sql, val)
    mydb.commit()
    print("Item added successfully")

# Function to delete an item from the database
def delete_item(id_barang):
    cursor = mydb.cursor()
    sql = "DELETE FROM barang WHERE id_barang = %s"
    val = (id_barang,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Item deleted successfully")

# Main program loop
while True:
    print("1. Display items")
    print("2. Add item")
    print("3. Delete item")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        display_items()
    elif choice == "2":
        nama_barang = input("Enter item name: ")
        harga = float(input("Enter item price: "))
        stok = int(input("Enter item stock: "))
        add_item(nama_barang, harga, stok)
    elif choice == "3":
        id_barang = int(input("Enter item ID: "))
        delete_item(id_barang)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
mydb.close()
