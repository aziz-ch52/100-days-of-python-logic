# Program to Calculate a^b using a while loop

# Step 1: Assign base and exponent values
a = 2   # Base
b = 5   # Exponent

# Step 2: Handle negative exponent case (not supported in this basic version)
if b < 0:
    print("Negative exponents are not handled in this version.")

else:
    # Step 3: Initialize result as 1 (multiplicative identity)
    result = 1

    # Step 4: Initialize counter to track number of multiplications
    counter = 0

    # Step 5: Repeat multiplication until the counter equals the exponent
    while counter < b:
        result *= a      # Multiply result by base
        counter += 1     # Increment counter

    # Step 6: Display final result
    print("Result:", result)

# End of Program
