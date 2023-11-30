
# Initialize an empty dictionary to store customer orders
customer_orders = {}

# Function to add a new order
def add_order():
    table_number = input("Enter table number: ")
    food_items = input("Enter food items (comma-separated): ").split(",")
    food_prices = input("Enter food prices (comma-separated): ").split(",")
    total_payment = sum(float(price) for price in food_prices)
    
    # Store the order details in a dictionary
    order_details = {
        "table_number": table_number,
        "food_items": food_items,
        "food_prices": food_prices,
        "total_payment": total_payment
    }
    
    # Add the order to the customer_orders dictionary
    customer_orders[table_number] = order_details

# Function to display all orders
def display_orders():
    for table_number, order_details in customer_orders.items():
        print(f"Table Number: {table_number}")
        print(f"Food Items: {', '.join(order_details['food_items'])}")
        print(f"Food Prices: {', '.join(order_details['food_prices'])}")
        print(f"Total Payment: {order_details['total_payment']}")
        print()

# Function to update an order
def update_order():
    table_number = input("Enter table number to update: ")
    if table_number in customer_orders:
        food_items = input("Enter updated food items (comma-separated): ").split(",")
        food_prices = input("Enter updated food prices (comma-separated): ").split(",")
        total_payment = sum(float(price) for price in food_prices)
        
        # Update the order details in the dictionary
        order_details = customer_orders[table_number]
        order_details["food_items"] = food_items
        order_details["food_prices"] = food_prices
        order_details["total_payment"] = total_payment
        
        print("Order updated successfully!")
    else:
        print("Table number not found!")

# Main program loop
while True:
    print("1. Add Order")
    print("2. Display Orders")
    print("3. Update Order")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_order()
    elif choice == "2":
        display_orders()
    elif choice == "3":
        update_order()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
