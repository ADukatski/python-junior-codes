password = input()

def length(p):

    if 6 <= len(p) <= 10:
        return True
    print(f"Password must be between 6 and 10 characters")
    return False

def letters_digits(p):

    if p.isalnum():
        return True
    print(f"Password must consist only of letters and digits")
    return False

def digits(p):
    digits = 0

    for d in p:
        if d.isdigit():
            digits += 1

    if digits >= 2:
        return True
    print(f"Password must have at least 2 digits")
    return False

valid = [length(password), letters_digits(password), digits(password)]

if all(valid):
    print("Password is valid")