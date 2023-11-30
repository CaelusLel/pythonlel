import math
# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Error: Division by zero is not allowed")

# Function to perform modulus operation
def modulus(num1, num2):
    return num1 % num2

# Function to perform exponentiation
def exponentiate(num1, num2):
    return num1 ** num2

# Function to perform floor division
def floor_divide(num1, num2):
    if num2 != 0:
        return num1 // num2
    else:
        print("Error: Division by zero is not allowed")

# Function to perform square root
def square_root(num):
    if num >= 0:
        return num ** 0.5
    else:
        print("Error: Square root of a negative number is not defined")

# Function to perform factorial
def factorial(num):
    if num >= 0:
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)
    else:
        print("Error: Factorial of a negative number is not defined")

# Function to perform absolute value
def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num

# Function to perform logarithm
def logarithm(num):
    if num > 0:
        return math.log10(num)
    else:
        print("Error: Logarithm of a non-positive number is not defined")

# Function to perform trigonometric sine
def sine(angle):
    return math.sin(math.radians(angle))

# Function to perform trigonometric cosine
def cosine(angle):
    return math.cos(math.radians(angle))

# Function to perform trigonometric tangent
def tangent(angle):
    return math.tan(math.radians(angle))

# Function to perform trigonometric inverse sine
def inverse_sine(value):
    return math.degrees(math.asin(value))

# Function to perform trigonometric inverse cosine
def inverse_cosine(value):
    return math.degrees(math.acos(value))

# Function to perform trigonometric inverse tangent
def inverse_tangent(value):
    return math.degrees(math.atan(value))
