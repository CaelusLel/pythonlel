
# Prompt the user to enter the number of working hours and the hourly rate
hours_worked = float(input("Enter the number of working hours: "))
hourly_rate = float(input("Enter the hourly rate: "))

# Calculate the salary
if hours_worked <= 40:
    # If the number of working hours is less than or equal to 40, no overtime
    salary = hours_worked * hourly_rate
else:
    # If the number of working hours is more than 40, calculate overtime
    overtime_hours = hours_worked - 40
    overtime_rate = hourly_rate * 1.5
    salary = (40 * hourly_rate) + (overtime_hours * overtime_rate)

# Display the calculated salary
print("The employee's salary is:", salary)
