# Program to Convert a Decimal Number to Binary Manually
# (Without using bin() or built-in conversion functions)

# Step 1: Take input from the user
decimal = int(input("Enter a non-negative decimal number: "))

# Step 2: Handle special case when number is 0
if decimal == 0:
    print("Binary:", 0)

# Step 3: Check for negative numbers (basic handling)
elif decimal < 0:
    print("This version handles only non-negative numbers.")

else:
    # Step 4: Initialize an empty string to store binary digits
    binary = ""

    # Step 5: Repeatedly divide by 2 and store the remainder
    # This is the manual conversion logic
    while decimal > 0:
        remainder = decimal % 2        # Get remainder (0 or 1)
        binary = str(remainder) + binary  # Add remainder to the left
        decimal = decimal // 2         # Reduce number by dividing by 2

    # Step 6: Print final binary result
    print("Binary:", binary)

# End of Program
