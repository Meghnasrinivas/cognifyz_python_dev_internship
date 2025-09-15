def validate_email(email):
    email = email.strip()

    if email.count('@') != 1:
        return False

    local, domain = email.split('@')
    
    if not local or not domain:
        return False

    if '.' not in domain:
        return False

    return True


# ---- Main Program ----
email = input("Enter an email address: ")

if validate_email(email):
    print("Valid Email ✅")
else:
    print("Invalid Email ❌")
