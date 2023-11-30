# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements in a list
print(my_list[0])  # Output: 1

# Modifying elements in a list
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

# Appending elements to a list
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Removing elements from a list
my_list.remove(2)
print(my_list)  # Output: [10, 3, 4, 5, 6]

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1

# Modifying elements in a tuple is not allowed
# my_tuple[0] = 10  # Raises TypeError

# Concatenating tuples
new_tuple = my_tuple + (6, 7)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)

# Counting occurrences of an element in a tuple
count = my_tuple.count(3)
print(count)  # Output: 1

# Finding the index of an element in a tuple
index = my_tuple.index(4)
print(index)  # Output: 3

# Indexing
print(my_list[0])  # Output: 1

# Slicing
print(my_list[1:4])  # Output: [2, 3, 4]

# Matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6

# Length
print(len(my_list))  # Output: 5

# Maximum and minimum
print(max(my_list))  # Output: 5
print(min(my_list))  # Output: 1

# Inserting elements
my_list.insert(2, 10)
print(my_list)  # Output: [1, 2, 10, 3, 4, 5]

# Popping elements
popped_element = my_list.pop(3)
print(popped_element)  # Output: 3
print(my_list)  # Output: [1, 2, 10, 4, 5]

# Removing elements
my_list.remove(10)
print(my_list)  # Output: [1, 2, 4, 5]

# Reversing
my_list.reverse()
print(my_list)  # Output: [5, 4, 2, 1]

# Sorting
my_list.sort()
print(my_list)  # Output: [1, 2, 4, 5]

# Counting occurrences
count = my_list.count(2)
print(count)  # Output: 1

# Extending list
my_list.extend([6, 7, 8])
print(my_list)  # Output: [1, 2, 4, 5, 6, 7, 8]

# Appending elements
my_list.append(9)
print(my_list)  # Output: [1, 2, 4, 5, 6, 7, 8, 9]

