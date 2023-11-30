
# Prompt the user to create a password
password = input("Create a password: ")

# Check if the password meets the security requirements
if len(password) >= 8:  # Check if the password has at least 8 characters
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if has_uppercase and has_lowercase and has_digit:
        print("Password meets the security requirements.")
    else:
        print("Password does not meet the security requirements.")
else:
    print("Password must have at least 8 characters.")
