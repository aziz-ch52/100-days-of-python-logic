# ---------------------------------------------------------
# Program: Find the factorial of a number using a for loop
# Definition:
# Factorial of N (written as N!) is:
# N! = N × (N-1) × (N-2) × ... × 2 × 1
# Special case:
# 0! = 1
# ---------------------------------------------------------

# Taking input from the user
n = int(input("Enter a non-negative integer: "))

# Check for negative numbers
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Initialize factorial variable to 1
    # We start with 1 because factorial is multiplication-based
    factorial = 1

    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        factorial = factorial * i  # Multiply current value

    # Output the result
    print(f"Factorial of {n} is: {factorial}")
