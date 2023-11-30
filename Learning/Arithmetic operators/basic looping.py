
# 1. For Loop
# The for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. While Loop
# The while loop is used to repeatedly execute a block of code as long as the specified condition is true.
count = 0
while count < 5:
    print(count)
    count += 1

# 3. Nested Loop
# A nested loop is a loop inside another loop. It allows you to perform repetitive tasks within repetitive tasks.
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# 4. Break Statement
# The break statement is used to exit the loop prematurely, regardless of the loop condition.
for num in range(1, 6):
    if num == 3:
        break
    print(num)

# 5. Continue Statement
# The continue statement is used to skip the rest of the code inside the loop for the current iteration and move to the next iteration.
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# 6. Else Statement with Loop
# The else statement in a loop is executed when the loop has exhausted all the items in the iterable or when the condition becomes false.
for num in range(1, 6):
    print(num)
else:
    print("Loop completed!")

# 7. Range Function
# The range() function is used to generate a sequence of numbers that can be used in a loop.
for num in range(1, 6):
    print(num)
