# Calculate `a^b` using a while loop

# Input values
a = 2   # Base
b = 5   # Exponent

# If exponent is negative, handle separately (basic handling)
if b < 0:
    print("This simple version does not handle negative exponents.")
else:
    result = 1      # Start with 1 (multiplicative identity)
    counter = 0     # This will track how many times we multiply

    # Loop runs until counter becomes equal to exponent (b)
    while counter < b:
        result = result * a   # Multiply result by base
        counter += 1          # Increase counter by 1

    # Final output
    print("Result:", result)
