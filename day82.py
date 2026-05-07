# Program: Find Square Root using Babylonian Method

# Step 1: Take input from the user
number = float(input("Enter a positive number: "))

# Step 2: Handle invalid input
if number < 0:
    print("Square root of negative numbers is not supported.")

elif number == 0:
    print("Square Root: 0")

else:
    # Step 3: Choose an initial guess
    guess = number / 2

    # Step 4: Define acceptable error tolerance
    epsilon = 0.000001

    # Step 5: Apply Babylonian Method iteratively
    while abs(guess * guess - number) > epsilon:

        # Babylonian formula:
        # new_guess = (guess + number/guess) / 2
        guess = (guess + number/guess) / 2

    # Step 6: Print result
    print("Approximate Square Root:", guess)

# End of Program
