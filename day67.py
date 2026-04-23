# Program to Calculate Factorial Using Recursion

# Step 1: Define recursive function
def factorial(n):
    """
    Returns factorial of n using recursion
    """

    # Step 2: Base case
    # Factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1

    # Step 3: Recursive case
    # n! = n * (n-1)!
    return n * factorial(n - 1)


# Step 4: Take input from the user
num = int(input("Enter a non-negative integer: "))

# Step 5: Handle negative input
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Step 6: Call function and print result
    print("Factorial:", factorial(num))

# End of Program