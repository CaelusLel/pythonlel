
# Prompt the user to enter their birth year
birth_year = int(input("Enter your birth year: "))

# Calculate the current year
current_year = 2022

# Calculate the age of the user
age = current_year - birth_year

# Check if the user is old enough (age >= 18)
if age >= 18:
    print("You are old enough.")
else:
    print("You are not old enough.")
