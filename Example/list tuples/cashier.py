
# Initialize sales data
sales = [
    ("Product A", 10, 100),  # (product name, quantity, price)
    ("Product B", 5, 200),
    ("Product C", 3, 150),
]

# Calculate total sales and discounts
total_sales = 0
total_discount = 0

for product in sales:
    product_name, quantity, price = product

    # Calculate subtotal for each product
    subtotal = quantity * price

    # Apply discount based on quantity
    if quantity >= 10:
        discount = subtotal * 0.1
    elif quantity >= 5:
        discount = subtotal * 0.05
    else:
        discount = 0

    # Update total sales and discounts
    total_sales += subtotal
    total_discount += discount

# Print the results
print("Total Sales:", total_sales)
print("Total Discount:", total_discount)
