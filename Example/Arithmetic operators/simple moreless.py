
# Step 1: Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Swap the values if num1 is greater than num2
if num1 > num2:
    num1, num2 = num2, num1

# Step 3: Display the values of the variables
print("First number:", num1)
print("Second number:", num2)
