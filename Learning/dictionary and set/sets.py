
# Creating an empty set
empty_set = set()
# Explanation: The set() function creates an empty set.

# Creating a set with elements
fruits = {'apple', 'banana', 'orange'}
# Explanation: Curly braces {} are used to create a set with elements.

# Accessing elements in a set
for fruit in fruits:
    print(fruit)
# Explanation: We can access elements in a set using a loop or by converting it to a list.

# Adding elements to a set
fruits.add('grape')
# Explanation: The add() method is used to add a single element to a set.

# Removing elements from a set
fruits.remove('banana')
# Explanation: The remove() method is used to remove a specific element from a set.

# Checking if an element exists in a set
if 'apple' in fruits:
    print("Apple exists in the set")
# Explanation: We can use the 'in' keyword to check if an element exists in a set.

# Combining sets
more_fruits = {'kiwi', 'pineapple'}
all_fruits = fruits.union(more_fruits)
# Explanation: The union() method combines two sets and returns a new set with all the elements.

# Finding the intersection of sets
common_fruits = fruits.intersection(more_fruits)
# Explanation: The intersection() method returns a new set with the common elements between two sets.

# Finding the difference between sets
unique_fruits = fruits.difference(more_fruits)
# Explanation: The difference() method returns a new set with the elements that are in the first set but not in the second set.

# Checking if a set is a subset of another set
if fruits.issubset(all_fruits):
    print("Fruits is a subset of all_fruits")
# Explanation: The issubset() method checks if a set is a subset of another set.

# Checking if a set is a superset of another set
if all_fruits.issuperset(fruits):
    print("all_fruits is a superset of fruits")
# Explanation: The issuperset() method checks if a set is a superset of another set.

# Clearing a set
fruits.clear()
# Explanation: The clear() method removes all elements from a set.

# Deleting a set
del all_fruits
# Explanation: The del keyword is used to delete a set.

