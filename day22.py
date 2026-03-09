
# Program to Print a Right-Angled Triangle of '*'

# Step 1: Define the height of the triangle
rows = 5

# Step 2: Use outer loop for each row
for i in range(1, rows + 1):

    # Step 3: Inner loop prints stars equal to current row number
    for j in range(i):
        print("*", end=" ")

    # Step 4: Move to next line after printing stars in the row
    print()

# End of Program