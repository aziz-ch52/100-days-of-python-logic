# Program to Find the Transpose of a Matrix

# Step 1: Take matrix input from the user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements row-wise:")

# Step 2: Build the matrix
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Initialize transpose matrix with swapped dimensions
transpose = []

for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])  # Swap row and column indices
    transpose.append(new_row)

# Step 4: Print original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Step 5: Print transpose matrix
print("Transpose Matrix:")
for row in transpose:
    print(row)

# End of Program
