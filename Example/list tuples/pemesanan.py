# Menu items and their prices
menu = [("Burger", 10), ("Pizza", 15), ("Fries", 5), ("Soda", 2)]

# Function to display the menu
def display_menu():
    print("Menu:")
    for item in menu:
        print(f"{item[0]} - ${item[1]}")

# Function to process the order
def process_order():
    order = []
    total = 0

    while True:
        display_menu()
        choice = input("Enter the item you want to order (or 'q' to quit): ")

        if choice == 'q':
            break

        for item in menu:
            if item[0].lower() == choice.lower():
                order.append(item)
                total += item[1]
                break
        else:
            print("Invalid choice. Please try again.")

    print("Your order:")
    for item in order:
        print(f"{item[0]} - ${item[1]}")

    print(f"Total payment: ${total}")

# Main program
if __name__ == "__main__":
    process_order()
