# Program to Print an Inverted Right-Angled Triangle of '*'

# Step 1: Define the number of rows (height of triangle)
rows = 5

# Step 2: Use an outer loop to control rows
# It starts from 'rows' and decreases to 1
for i in range(rows, 0, -1):

    # Step 3: Inner loop prints '*' for each column in the current row
    for j in range(i):
        print("*", end=" ")

    # Step 4: Move to the next line after each row
    print()

# End of Program