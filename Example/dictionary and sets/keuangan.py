# Define the sets for income and expenses categories
income_categories = {"Salary", "Bonus", "Investments"}
expense_categories = {"Rent", "Utilities", "Food", "Transportation"}

# Recursive function to calculate total income
def calculate_total_income(income_set):
    if not income_set:
        return 0
    else:
        return income_set.pop() + calculate_total_income(income_set)

# Recursive function to calculate total expenses
def calculate_total_expenses(expense_set):
    if not expense_set:
        return 0
    else:
        return expense_set.pop() + calculate_total_expenses(expense_set)

# Test the functions
total_income = calculate_total_income(income_categories)
total_expenses = calculate_total_expenses(expense_categories)

# Print the results
print("Total Income:", total_income)
print("Total Expenses:", total_expenses)
