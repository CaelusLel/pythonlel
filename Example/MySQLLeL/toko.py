import mysql.connector

# Establish database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="sistem_penjualan"
)

# Create a cursor object to execute SQL queries
cursor = mydb.cursor()

# Function to calculate total sales
def calculate_total_sales():
    query = "SELECT SUM(total_harga) FROM penjualan"
    cursor.execute(query)
    result = cursor.fetchone()
    total_sales = result[0]
    return total_sales

# Function to apply discount to total sales
def apply_discount(total_sales, discount_percentage):
    discounted_amount = total_sales * (discount_percentage / 100)
    final_amount = total_sales - discounted_amount
    return final_amount

# Function to manage stock
def manage_stock(barcode, quantity):
    query = "SELECT stok FROM barang WHERE barcode = %s"
    cursor.execute(query, (barcode,))
    result = cursor.fetchone()
    current_stock = result[0]
    
    if current_stock >= quantity:
        new_stock = current_stock - quantity
        update_query = "UPDATE barang SET stok = %s WHERE barcode = %s"
        cursor.execute(update_query, (new_stock, barcode))
        mydb.commit()
        return True
    else:
        return False

# Function to create a new record in a table
def create_record(table_name, data):
    columns = ', '.join(data.keys())
    values = tuple(data.values())
    placeholders = ', '.join(['%s'] * len(data))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(query, values)
    mydb.commit()

# Function to read records from a table
def read_records(table_name):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    records = cursor.fetchall()
    return records

# Function to update a record in a table
def update_record(table_name, record_id, data):
    set_values = ', '.join([f"{column} = %s" for column in data.keys()])
    values = tuple(data.values()) + (record_id,)
    query = f"UPDATE {table_name} SET {set_values} WHERE id = %s"
    cursor.execute(query, values)
    mydb.commit()

# Function to delete a record from a table
def delete_record(table_name, record_id):
    query = f"DELETE FROM {table_name} WHERE id = %s"
    cursor.execute(query, (record_id,))
    mydb.commit()

# Function to display a dynamic menu
def display_menu():
    print("1. Create a new record")
    print("2. Read records")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Exit")

# Function to handle user input and execute corresponding functions
def handle_menu_choice(choice):
    if choice == 1:
        table_name = input("Enter the table name: ")
        data = {}
        columns = input("Enter the column names (separated by comma): ").split(",")
        for column in columns:
            value = input(f"Enter the value for {column}: ")
            data[column] = value
        create_record(table_name, data)
    elif choice == 2:
        table_name = input("Enter the table name: ")
        records = read_records(table_name)
        for record in records:
            print(record)
    elif choice == 3:
        table_name = input("Enter the table name: ")
        record_id = input("Enter the record ID: ")
        data = {}
        columns = input("Enter the column names (separated by comma): ").split(",")
        for column in columns:
            value = input(f"Enter the new value for {column}: ")
            data[column] = value
        update_record(table_name, record_id, data)
    elif choice == 4:
        table_name = input("Enter the table name: ")
        record_id = input("Enter the record ID: ")
        delete_record(table_name, record_id)
    elif choice == 5:
        exit()
    else:
        print("Invalid choice!")

# Main program loop
while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    handle_menu_choice(choice)

# Close database connection
mydb.close()
