
# 1. For Loop
# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# 2. While Loop
# Print numbers from 1 to 5 using a while loop
j = 1
while j <= 5:
    print(j)
    j += 1

# 3. Nested Loop
# Print a pattern using nested loops
for row in range(1, 5):
    for col in range(1, row + 1):
        print("*", end=" ")
    print()

# 4. Break Statement
# Print numbers from 1 to 10, but stop when the number is 5
for num in range(1, 11):
    if num == 5:
        break
    print(num)

# 5. Continue Statement
# Print even numbers from 1 to 10 using the continue statement
for num in range(1, 11):
    if num % 2 != 0:
        continue
    print(num)

# 6. Else Statement with Loop
# Print "Loop ended" after the loop completes
for i in range(1, 6):
    print(i)
else:
    print("Loop ended")
    # 1. For Loop
    # Print each character in a string
    name = "John Doe"
    for char in name:
        print(char)

    # 2. While Loop
    # Calculate the factorial of a number
    num = 5
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 1
    print("Factorial:", factorial)

    # 3. Nested Loop
    # Print a multiplication table
    for i in range(1, 6):
        for j in range(1, 11):
            print(i, "*", j, "=", i * j)

    # 4. Break Statement
    # Find the first even number in a list
    numbers = [1, 3, 5, 7, 8, 9, 10]
    for num in numbers:
        if num % 2 == 0:
            print("First even number:", num)
            break

    # 5. Continue Statement
    # Print all odd numbers in a list
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in numbers:
        if num % 2 == 0:
            continue
        print("Odd number:", num)

    # 6. Else Statement with Loop
    # Check if a number is prime
    num = 7
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not prime")
            break
    else:
        print(num, "is prime")
