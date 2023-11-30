
# Creating a tuple to store student information
student = ("John Doe", 20, "Computer Science")

# Accessing tuple elements
name = student[0]
age = student[1]
major = student[2]

# Printing student information
print("Name:", name)
print("Age:", age)
print("Major:", major)

# Updating tuple elements
# Tuples are immutable, so we need to create a new tuple with the updated values
student = student[:2] + ("Electrical Engineering",)

# Printing updated student information
print("Updated Major:", student[2])

# Unpacking a tuple
name, age, major = student

# Printing unpacked values
print("Unpacked Name:", name)
print("Unpacked Age:", age)
print("Unpacked Major:", major)
