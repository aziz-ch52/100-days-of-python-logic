# Program to Create and Print a 3x3 Matrix

# Step 1: Initialize an empty list to store the matrix
matrix = []

# Step 2: Take input for 3 rows
for i in range(3):
    row = list(map(int, input(f"Enter 3 elements for row {i+1}: ").split()))
    
    # Step 3: Ensure exactly 3 elements are entered
    if len(row) != 3:
        print("Please enter exactly 3 elements.")
        exit()
    
    matrix.append(row)

# Step 4: Print the matrix row by row
print("3x3 Matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Move to next line after each row

# End of Program
