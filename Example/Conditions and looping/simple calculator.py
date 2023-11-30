
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    return a / b

# Function to create a calculator with different looping types
def looping_calculator():
    while True:
        print("=== Looping Calculator ===")
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("0. Exit")

        choice = input("Enter your choice (0-4): ")

        if choice == "0":
            print("Thank you for using the looping calculator.")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = add(num1, num2)
            print("Addition result:", result)
        elif choice == "2":
            result = subtract(num1, num2)
            print("Subtraction result:", result)
        elif choice == "3":
            result = multiply(num1, num2)
            print("Multiplication result:", result)
        elif choice == "4":
            result = divide(num1, num2)
            print("Division result:", result)
        else:
            print("Invalid choice. Please try again.")

looping_calculator()
