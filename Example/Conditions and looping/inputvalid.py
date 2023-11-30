# Prompt the user to enter a number
while True:
    try:
        number = int(input("Enter a number: "))  # Get user input as an integer
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Perform arithmetic operations using the input number
square = number ** 2
cube = number ** 3

# Print the results
print("Square of", number, "is", square)
print("Cube of", number, "is", cube)
