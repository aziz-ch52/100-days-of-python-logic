# Program to Print a Pyramid of '*.'

# Step 1: Define the height of the pyramid
rows = 5

# Step 2: Loop through each row
for i in range(1, rows + 1):

    # Step 3: Print spaces to center the pyramid
    for j in range(rows - i):
        print(" ", end="")

    # Step 4: Print stars for the current row
    # Number of stars follows pattern: (2*i - 1)
    for k in range(2 * i - 1):
        print("*", end="")

    # Step 5: Move to the next line after printing each row
    print()

# End of Program
