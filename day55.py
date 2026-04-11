# Program to Find the Sum of the Main Diagonal of a Matrix

# Step 1: Take the size of a square matrix from the user
n = int(input("Enter size of square matrix (n x n): "))

# Step 2: Take matrix input
matrix = []
print("Enter matrix elements row-wise:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Initialize sum variable
diagonal_sum = 0

# Step 4: Traverse and sum main diagonal elements
# Main diagonal elements are where row index == column index
for i in range(n):
    diagonal_sum += matrix[i][i]

# Step 5: Print result
print("Sum of main diagonal:", diagonal_sum)

# End of Program
