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

# Close database connection
mydb.close()
