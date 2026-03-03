# Program to Convert a Binary Number to Decimal Manually
# (Without using int(binary, 2) or built-in conversion)

# Step 1: Take binary input as a string
binary = input("Enter a binary number: ")

# Step 2: Initialize decimal result
decimal = 0

# Step 3: Initialize power (position from right, starting at 0)
power = 0

# Step 4: Traverse the binary string from right to left
for digit in reversed(binary):

    # Validate binary digit
    if digit not in ('0', '1'):
        print("Invalid binary number.")
        break

    # Convert character to integer (0 or 1)
    bit = int(digit)

    # Apply manual conversion formula:
    # decimal += bit × (2^power)
    decimal += bit * (2 ** power)

    # Increase power for next position
    power += 1

else:
    # Step 5: Print final decimal value (only if no break occurred)
    print("Decimal:", decimal)

# End of Program
