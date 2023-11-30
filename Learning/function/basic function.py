# Function without parameters
def greet():
    # This function greets the user
    print("Hello!")

# Function with parameters
def add_numbers(a, b):
    # This function adds two numbers and returns the result
    return a + b

# Function with default parameter
def multiply_numbers(a, b=2):
    # This function multiplies two numbers and returns the result
    return a * b

# Function with variable number of arguments
def calculate_average(*args):
    # This function calculates the average of the given numbers
    total = sum(args)
    average = total / len(args)
    return average

# Function with keyword arguments
def print_info(name, age, **kwargs):
    # This function prints the information provided
    print("Name:", name)
    print("Age:", age)
    for key, value in kwargs.items():
        print(key + ":", value)

# Function as a parameter
def apply_operation(operation, a, b):
    # This function applies the given operation on two numbers
    return operation(a, b)

# Function as a return value
def get_operation():
    # This function returns another function
    return add_numbers

# Function as a decorator
def uppercase_decorator(func):
    # This function decorates another function by converting its output to uppercase
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

    # Variable Scoping

    # Global variable
    global_var = 10

    def function_with_local_var():
        # Local variable
        local_var = 20
        print("Local variable:", local_var)

    def function_with_global_var():
        print("Global variable:", global_var)

    # Recursive Looping

    def countdown(n):
        if n <= 0:
            return
        print(n)
        countdown(n-1)

    # Explanation comments

    # Variable Scoping
    # - We define a global variable `global_var` with a value of 10.
    # - We define a function `function_with_local_var` that has a local variable `local_var` with a value of 20.
    # - We print the value of the local variable.
    # - We define another function `function_with_global_var` that prints the value of the global variable.

    # Recursive Looping
    # - We define a function `countdown` that takes an integer `n` as input.
    # - If `n` is less than or equal to 0, we return from the function.
    # - Otherwise, we print the value of `n` and recursively call the `countdown` function with `n-1` as the input.

    # Note: The explanation comments are provided to explain the purpose and functionality of each line of code.
    # They are not necessary for the code to run correctly.

from functools import reduce

# Lambda function with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
# Explanation: We define a lambda function that takes a number `x` as input and returns its square.
# We use the `map()` function to apply the lambda function to each element in the `numbers` list.
# The result is a new list `squared_numbers` containing the squared values of the original numbers.

# Lambda function with filter()
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# Explanation: We define a lambda function that takes a number `x` as input and returns `True` if it is even, `False` otherwise.
# We use the `filter()` function to apply the lambda function to each element in the `numbers` list.
# The result is a new list `even_numbers` containing only the even numbers from the original list.

# Lambda function with reduce()
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
# Explanation: We import the `reduce()` function from the `functools` module.
# We define a lambda function that takes two numbers `x` and `y` as input and returns their product.
# We use the `reduce()` function to apply the lambda function to the elements in the `numbers` list, one pair at a time.
# The result is the product of all the numbers in the list.


