"""
Question:
Find the quotient and remainder of a / b using ONLY subtraction.
Do NOT use division (/), floor division (//), or modulus (%).
"""

# Given values
a = 17
b = 5

# Step 1: Check for division by zero
# Division by 0 is undefined, so we must handle it.
if b == 0:
    print("Division by zero is not allowed")

else:
    # Step 2: Initialize variables
    
    quotient = 0        # This will count how many times we subtract 'b'
    remainder = a       # Start remainder as 'a'

    # Step 3: Repeated subtraction
    # Keep subtracting 'b' from remainder
    # as long as remainder is greater than or equal to 'b'
    while remainder >= b:
        remainder = remainder - b   # Subtract 'b'
        quotient += 1               # Increase count

    # Step 4: Print results
    print("Quotient:", quotient)
    print("Remainder:", remainder)