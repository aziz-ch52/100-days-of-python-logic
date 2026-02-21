# Print the first n terms of the Fibonacci sequence.


# Get user input
num = int(input("Enter how many numbers you want: "))

# Initialize the first two terms
a, b = 0, 1

# Loop to print the sequence
for i in range(num):
    print(a, end=" ")
    a, b = b, a + b  # Update: a becomes b, b becomes the sum

# -------------------------------------- #

print("\n")

# With Function:

# Define the function


def fibonacci_series(n):
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)  # Add current number to a list
        a, b = b, a + b
    return result         # Give the list back to the user


# Call the function
terms = int(input("Enter terms for functional version: "))
output = fibonacci_series(terms)

print("The sequence is:", output)
