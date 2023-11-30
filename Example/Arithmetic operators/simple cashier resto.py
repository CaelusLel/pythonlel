
# Prompt the user for the total bill and tip percentage
bill_amount = float(input("Enter the total bill amount: $"))
tip_percentage = float(input("Enter the tip percentage: "))

# Calculate the tip amount and total payment
tip_amount = bill_amount * (tip_percentage / 100)
total_payment = bill_amount + tip_amount

# Display the results
print("Bill amount: $", bill_amount)
print("Tip percentage: ", tip_percentage, "%")
print("Tip amount: $", tip_amount)
print("Total payment: $", total_payment)
