# Program: Basic Email Validation (Manual Checks)

# Step 1: Take input from the user
email = input("Enter an email address: ")

# Step 2: Initialize validation flag
is_valid = True

# Step 3: Check for exactly one '@'
if email.count('@') != 1:
    is_valid = False
else:
    local, domain = email.split('@')

    # Step 4: Local and domain parts must not be empty
    if len(local) == 0 or len(domain) == 0:
        is_valid = False

    # Step 5: Domain must contain at least one '.'
    elif '.' not in domain:
        is_valid = False

    else:
        # Step 6: Split domain into parts by '.'
        domain_parts = domain.split('.')

        # Each part must be non-empty
        for part in domain_parts:
            if len(part) == 0:
                is_valid = False
                break

# Step 7: Print result
if is_valid:
    print("Valid Email")
else:
    print("Invalid Email")

# End of Program