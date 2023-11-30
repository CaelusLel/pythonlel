
# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary with initial values
fruits = {'apple': 5, 'banana': 3, 'orange': 2}

# Accessing values using keys
apple_count = fruits['apple']
print(f"Number of apples: {apple_count}")

# Modifying values using keys
fruits['banana'] = 6
print(f"Fruit dictionary after modifying banana count: {fruits}")

# Adding a new key-value pair
fruits['grape'] = 4
print(f"Fruit dictionary after adding grape: {fruits}")

# Removing a key-value pair
del fruits['orange']
print(f"Fruit dictionary after removing orange: {fruits}")

# Checking if a key exists in the dictionary
if 'apple' in fruits:
    print("Apple is present in the dictionary")

# Getting the number of key-value pairs in the dictionary
num_fruits = len(fruits)
print(f"Number of fruits in the dictionary: {num_fruits}")

# Getting a list of all keys in the dictionary
fruit_names = fruits.keys()
print(f"All fruit names: {fruit_names}")

# Getting a list of all values in the dictionary
fruit_counts = fruits.values()
print(f"All fruit counts: {fruit_counts}")

# Getting a list of key-value pairs as tuples
fruit_items = fruits.items()
print(f"All fruit items: {fruit_items}")
