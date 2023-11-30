
# Ask the user to enter the exam score
score = float(input("Enter the exam score: "))

# Using if-else statement
if score >= 70:
    print("Congratulations! You passed the exam.")
else:
    print("Sorry, you failed the exam.")

# Using if-elif-else statement
if score >= 90:
    print("Excellent! You achieved an A grade.")
elif score >= 80:
    print("Good job! You achieved a B grade.")
elif score >= 70:
    print("Well done! You achieved a C grade.")
else:
    print("Sorry, you failed the exam.")

# Using nested if-else statement
if score >= 70:
    if score >= 90:
        print("Excellent! You achieved an A grade.")
    elif score >= 80:
        print("Good job! You achieved a B grade.")
    else:
        print("Well done! You achieved a C grade.")
else:
    print("Sorry, you failed the exam.")
