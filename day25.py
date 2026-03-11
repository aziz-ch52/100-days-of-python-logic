# Program to Print a Diamond Pattern of '*'

# Step 1: Define the number of rows for the upper half
rows = 5

# ----------------------------
# Upper Pyramid
# ----------------------------

# Step 2: Loop to print the upper pyramid
for i in range(1, rows + 1):

    # Step 3: Print spaces to center the stars
    for j in range(rows - i):
        print(" ", end="")

    # Step 4: Print stars (2*i - 1 pattern)
    for k in range(2 * i - 1):
        print("*", end="")

    # Step 5: Move to the next line
    print()

# ----------------------------
# Lower Inverted Pyramid
# ----------------------------

# Step 6: Loop to print the bottom half
for i in range(rows - 1, 0, -1):

    # Step 7: Print spaces
    for j in range(rows - i):
        print(" ", end="")

    # Step 8: Print stars
    for k in range(2 * i - 1):
        print("*", end="")

    # Step 9: Move to the next line
    print()

# End of Program