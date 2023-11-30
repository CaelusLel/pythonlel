
# Prompt the user to enter weight in kilograms
weight = float(input("Enter your weight in kilograms: "))

# Prompt the user to enter height in meters
height = float(input("Enter your height in meters: "))

# Calculate BMI using the formula: weight / (height * height)
bmi = weight / (height * height)

# Determine the category based on the BMI value
category = ""
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Print the BMI value and category
print("Your BMI is:", bmi)
print("Category:", category)
