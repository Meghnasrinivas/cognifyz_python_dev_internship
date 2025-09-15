import string

def check_password_strength(password):
    # conditions
    length = len(password) >= 8
    has_lower = any(ch.islower() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(ch in string.punctuation for ch in password)

    # check all
    if all([length, has_lower, has_upper, has_digit, has_special]):
        return "Strong Password ✅"
    else:
        return "Weak Password ❌"

print("Password Strength Checker 🔐")
user_password = input("Enter your password: ")
print(check_password_strength(user_password))
