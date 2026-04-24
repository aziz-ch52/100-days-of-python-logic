# Program to Generate Fibonacci Series Using Recursion

# Step 1: Define recursive function
def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion
    """

    # Step 2: Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Step 3: Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


# Step 4: Take input from the user
terms = int(input("Enter number of terms: "))

# Step 5: Handle invalid input
if terms <= 0:
    print("Please enter a positive integer.")
else:
    # Step 6: Generate and print Fibonacci series
    for i in range(terms):
        print(fibonacci(i), end=" ")

# End of Program
