# Program to Flatten a 2D Matrix into a 1D List

# Step 1: Take matrix size input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Step 2: Take matrix input
matrix = []
print("Enter matrix elements row-wise:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Initialize an empty list for the flattened result
flattened = []

# Step 4: Traverse the matrix row by row
for i in range(rows):
    for j in range(cols):
        flattened.append(matrix[i][j])

# Step 5: Print the flattened list
print("Flattened list:", flattened)

# End of Program
