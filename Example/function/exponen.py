# Recursive power calculator

def power(base, exponent):
    # Base case: if exponent is 0, return 1
    if exponent == 0:
        return 1
    # Recursive case: multiply base with power(base, exponent-1)
    else:
        return base * power(base, exponent-1)

# Get input from the user
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Calculate the power using the recursive function
result = power(base, exponent)

# Print the result
print(f"{base} raised to the power of {exponent} is {result}")
