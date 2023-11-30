# Define the lists
list1 = ["15 menu makanan"]
list2 = ["5 menu minuman"]
list3 = ["5 nama teman terdekat anda"]
list4 = ["5 bulan lahir teman tersebut"]
list5 = ["5 tanggal lahir teman tersebut"]

# Function to join two lists and display the result
def join_lists(list1, list2):
    result = list1 + list2
    print("Output 1:", result)

# Function to update list3 at index 3 and index 5
def update_list(list3):
    list3[2] = "Updated value at index 3"
    list3[4] = "Updated value at index 5"
    print("Output 2:", list3)

# Function to remove elements from list5 at index 1 and index 5
def remove_elements(list5):
    del list5[0]
    del list5[4]
    print("Output 3:", list5)

# Function to join list4 and list5, and find the maximum and minimum values
def find_max_min(list4, list5):
    combined_list = list4 + list5
    max_value = max(combined_list)
    min_value = min(combined_list)
    print("Output 4: Max =", max_value, "Min =", min_value)

# Call the functions
join_lists(list1, list4)
update_list(list3)
remove_elements(list5)
find_max_min(list4, list5)
