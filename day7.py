# Program to Print the First n Terms of the Fibonacci Sequence

# ---------------------- #
# Part 1: Without Function
# ---------------------- #

# Step 1: Take input from the user
num = int(input("Enter how many numbers you want: "))

# Step 2: Initialize the first two Fibonacci numbers
a, b = 0, 1

# Step 3: Loop to generate and print the Fibonacci sequence
for i in range(num):
    print(a, end=" ")   # Print current term
    a, b = b, a + b     # Update values for next iteration

print("\n")  # Move to next line


# ---------------------- #
# Part 2: Using Function
# ---------------------- #

# Step 1: Define a function to generate the Fibonacci series
def fibonacci_series(n):
    result = []          # Create an empty list to store the sequence
    a, b = 0, 1          # Initialize first two terms

    # Step 2: Generate sequence using loop
    for i in range(n):
        result.append(a) # Add current term to list
        a, b = b, a + b  # Update values

    return result        # Return complete sequence


# Step 3: Take input for functional version
terms = int(input("Enter terms for functional version: "))

# Step 4: Call the function and store the result
output = fibonacci_series(terms)

# Step 5: Print final sequence
print("The sequence is:", output)

# End of Program
