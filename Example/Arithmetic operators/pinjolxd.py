# Loan Program
# This program calculates the total payment for a loan

# Input the loan amount
loan_amount = float(input("Enter the loan amount: "))

# Input the interest rate
interest_rate = float(input("Enter the interest rate: "))

# Input the loan term
loan_term = int(input("Enter the loan term (in months): "))

# Calculate the total payment
total_payment = loan_amount + (loan_amount * interest_rate * loan_term)

# Print the total payment
print("Total payment:", total_payment)
