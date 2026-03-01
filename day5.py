"""
Question:
Find the quotient and remainder of a / b using ONLY subtraction.
Do NOT use division (/), floor division (//), or modulus (%).
"""

# Step 1: Assign values
a = 17
b = 5

# Step 2: Check for division by zero
# Division by zero is undefined
if b == 0:
    print("Division by zero is not allowed")

else:
    # Step 3: Initialize quotient and remainder
    quotient = 0          # Counts how many times 'b' is subtracted
    remainder = a         # Start remainder as 'a'

    # Step 4: Perform repeated subtraction
    # Keep subtracting 'b' from the remainder
    # until remainder becomes less than 'b.'
    while remainder >= b:
        remainder -= b    # Subtract 'b' from remainder
        quotient += 1     # Increment quotient by 1

    # Step 5: Display final results
    print("Quotient:", quotient)
    print("Remainder:", remainder)

# End of Program
