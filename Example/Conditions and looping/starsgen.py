
# Ask the user for the height of the pattern
height = int(input("Enter the height of the pattern: "))

# Outer loop for rows
for i in range(height):
    # Inner loop for columns
    for j in range(i + 1):
        print("*", end=" ")
    print()  # Move to the next line after each row
