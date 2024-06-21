while True:
 # Get password from user
 password = input("Enter your password: ")
 # Condition 1: At least 12 characters
 if len(password) < 12:
    print("Password should be at least 12 characters long.")
    continue
 else:
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    has_space = False

 for char in password:
    if char.isalpha():
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
    elif char.isdigit():
        has_digit = True
    elif char.isspace():
        has_space = True
    else:
        has_special = True
 # Conditions 2, 3, and 4
 if has_uppercase and has_lowercase and has_digit and has_special and has_space:
    print("This is a strong password!")
    break
 else:
    print("This is not a strong password. Please try again.")
