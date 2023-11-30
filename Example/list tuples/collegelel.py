
# Function to add a new student to the list
def add_student(students, name, age, ipk):
    student = (name, age, ipk)
    students.append(student)

# Function to display all student data
def display_students(students):
    for student in students:
        name, age, ipk = student
        print(f"Name: {name}, Age: {age}, IPK: {ipk}")

# Function to search for a student by name
def search_student(students, name):
    for student in students:
        if student[0] == name:
            return student
    return None

# Function to update a student's IPK
def update_ipk(students, name, new_ipk):
    for i, student in enumerate(students):
        if student[0] == name:
            students[i] = (student[0], student[1], new_ipk)
            break

# Function to delete a student from the list
def delete_student(students, name):
    for student in students:
        if student[0] == name:
            students.remove(student)
            break

# Main program
students = []

while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update IPK")
    print("5. Delete Student")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        ipk = float(input("Enter student IPK: "))
        add_student(students, name, age, ipk)
    elif choice == 2:
        display_students(students)
    elif choice == 3:
        name = input("Enter student name to search: ")
        student = search_student(students, name)
        if student:
            print(f"Student found - Name: {student[0]}, Age: {student[1]}, IPK: {student[2]}")
        else:
            print("Student not found")
    elif choice == 4:
        name = input("Enter student name to update IPK: ")
        new_ipk = float(input("Enter new IPK: "))
        update_ipk(students, name, new_ipk)
    elif choice == 5:
        name = input("Enter student name to delete: ")
        delete_student(students, name)
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")
