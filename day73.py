# Program: Random Password Generator

import random

# Step 1: Define character sets
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()"

# Step 2: Combine all characters
all_chars = lowercase + uppercase + digits + symbols

# Step 3: Take password length input from user
length = int(input("Enter desired password length: "))

# Step 4: Validate length
if length <= 0:
    print("Password length must be greater than 0.")

else:
    # Step 5: Initialize password variable
    password = ""

    # Step 6: Generate password by randomly selecting characters
    for i in range(length):
        password += random.choice(all_chars)

    # Step 7: Print generated password
    print("Generated Password:", password)

# End of Program