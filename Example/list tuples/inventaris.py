# Inventory list to store items
inventory = []

# Function to add an item to the inventory
def add_item(item_name, quantity, price):
    item = (item_name, quantity, price)
    inventory.append(item)

# Function to remove an item from the inventory
def remove_item(item_name):
    for item in inventory:
        if item[0] == item_name:
            inventory.remove(item)
            break

# Function to update the quantity of an item in the inventory
def update_quantity(item_name, new_quantity):
    for item in inventory:
        if item[0] == item_name:
            item = (item[0], new_quantity, item[2])
            break

# Function to calculate the total value of the inventory
def calculate_total_value():
    total_value = 0
    for item in inventory:
        total_value += item[1] * item[2]
    return total_value

# Function to display the inventory
def display_inventory():
    for item in inventory:
        print(f"Item: {item[0]}, Quantity: {item[1]}, Price: {item[2]}")

# Example usage
add_item("Apple", 10, 1.5)
add_item("Banana", 5, 0.75)
add_item("Orange", 8, 1.25)

display_inventory()

remove_item("Banana")

update_quantity("Apple", 15)

total_value = calculate_total_value()
print(f"Total value of inventory: {total_value}")
