
# Initialize an empty list to store employee data
employees = []

# Function to add an employee to the list
def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    salary = float(input("Enter employee salary: "))

    # Create a dictionary to store employee data
    employee = {
        "name": name,
        "age": age,
        "salary": salary
    }

    # Add the employee dictionary to the list
    employees.append(employee)

    print("Employee added successfully!")

# Function to display all employees
def display_employees():
    if len(employees) == 0:
        print("No employees found.")
    else:
        print("Employee data:")
        for employee in employees:
            print(f"Name: {employee['name']}")
            print(f"Age: {employee['age']}")
            print(f"Salary: {employee['salary']}")
            print()

# Function to remove an employee from the list
def remove_employee():
    name = input("Enter employee name to remove: ")

    for employee in employees:
        if employee["name"] == name:
            employees.remove(employee)
            print("Employee removed successfully!")
            break
    else:
        print("Employee not found.")

# Main program loop
while True:
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Remove Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        remove_employee()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Program exited.")
