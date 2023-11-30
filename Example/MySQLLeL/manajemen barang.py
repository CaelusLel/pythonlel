import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="manajemen_barang"
)

# Function to display all items in a table
def display_table(table_name):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    items = cursor.fetchall()
    for item in items:
        print(item)

# Function to add a new item to a table
def add_item(table_name, *args):
    cursor = mydb.cursor()
    placeholders = ', '.join(['%s'] * len(args))
    sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cursor.execute(sql, args)
    mydb.commit()
    print("Item added successfully")

# Function to delete an item from a table
def delete_item(table_name, id_column, item_id):
    cursor = mydb.cursor()
    sql = f"DELETE FROM {table_name} WHERE {id_column} = %s"
    val = (item_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Item deleted successfully")

# Function to update an item in a table
def update_item(table_name, id_column, item_id, *args):
    cursor = mydb.cursor()
    placeholders = ', '.join([f"{column} = %s" for column in args])
    sql = f"UPDATE {table_name} SET {placeholders} WHERE {id_column} = %s"
    val = (*args, item_id)
    cursor.execute(sql, val)
    mydb.commit()
    print("Item updated successfully")

# Main program loop
while True:
    print("1. Display barang")
    print("2. Add barang")
    print("3. Delete barang")
    print("4. Update barang")
    print("5. Display pelanggan")
    print("6. Add pelanggan")
    print("7. Delete pelanggan")
    print("8. Update pelanggan")
    print("9. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        display_table("barang")
    elif choice == "2":
        nama_barang = input("Enter item name: ")
        harga = float(input("Enter item price: "))
        stok = int(input("Enter item stock: "))
        add_item("barang", nama_barang, harga, stok)
    elif choice == "3":
        id_barang = int(input("Enter item ID: "))
        delete_item("barang", "id_barang", id_barang)
    elif choice == "4":
        id_barang = int(input("Enter item ID: "))
        nama_barang = input("Enter new item name: ")
        harga = float(input("Enter new item price: "))
        stok = int(input("Enter new item stock: "))
        update_item("barang", "id_barang", id_barang, nama_barang, harga, stok)
    elif choice == "5":
        display_table("pelanggan")
    elif choice == "6":
        nama_pelanggan = input("Enter pelanggan name: ")
        alamat = input("Enter pelanggan address: ")
        add_item("pelanggan", nama_pelanggan, alamat)
    elif choice == "7":
        id_pelanggan = int(input("Enter pelanggan ID: "))
        delete_item("pelanggan", "id_pelanggan", id_pelanggan)
    elif choice == "8":
        id_pelanggan = int(input("Enter pelanggan ID: "))
        nama_pelanggan = input("Enter new pelanggan name: ")
        alamat = input("Enter new pelanggan address: ")
        update_item("pelanggan", "id_pelanggan", id_pelanggan, nama_pelanggan, alamat)
    elif choice == "9":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
mydb.close()
