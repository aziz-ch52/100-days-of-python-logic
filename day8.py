# ---------------------------------------------------------
# Program: Find the factorial of a number using a for loop
# Definition:
# Factorial of N (written as N!) is:
# N! = N × (N-1) × (N-2) × ... × 2 × 1
# Special case:
# 0! = 1
# ---------------------------------------------------------

# Step 1: Take input from the user
n = int(input("Enter a non-negative integer: "))

# Step 2: Check if the number is negative
# Factorial is not defined for negative numbers
if n < 0:
    print("Factorial is not defined for negative numbers.")

else:
    # Step 3: Initialize factorial variable
    # Start with 1 because the multiplication identity is 1
    factorial = 1

    # Step 4: Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Multiply factorial by current number
        factorial *= i

    # Step 5: Print the final result
    print(f"Factorial of {n} is: {factorial}")

# End of Program
