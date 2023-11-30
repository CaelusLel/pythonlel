
# Prompt the user to enter the upper limit
upper_limit = int(input("Enter the upper limit: "))

# Iterate through each number in the range
for num in range(2, upper_limit + 1):
    # Check if the number is prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # Print the prime numbers
    if is_prime:
        print(num, "is a prime number")
