# Program to Print a 5x5 Square of '*'

# Step 1: Define the size of the square
size = 5

# Step 2: Use an outer loop for rows
for i in range(size):

    # Step 3: Use an inner loop for columns
    for j in range(size):
        print("*", end=" ")   # Print star without moving to next line

    # Step 4: Move to the next line after each row
    print()

# End of Program