import random

# Generate a random list of numbers
numbers = [random.randint(1, 100) for _ in range(10)]

# Print the generated list
print("Generated list:", numbers)

# Ask the user for a number to search
target = int(input("Enter a number to search: "))

# Initialize a flag variable to track if the number is found
found = False

# Loop through the list to search for the number
for num in numbers:
    if num == target:
        print("Number found!")
        found = True
        break

# If the number is not found, print a message
if not found:
    print("Number not found!")
