
# Ask the user to enter the base and exponent
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Initialize the result variable
result = 1

# Calculate the power using a for loop
for _ in range(exponent):
    result *= base

# Print the result
print(f"The result of {base} raised to the power of {exponent} is: {result}")
