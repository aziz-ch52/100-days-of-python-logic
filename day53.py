# Program to Multiply Two 3x3 Matrices

# Step 1: Define two 3x3 matrices
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Step 2: Initialize result matrix with zeros
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Step 3: Perform matrix multiplication
# Formula: result[i][j] = sum of A[i][k] * B[k][j]

for i in range(3):              # Rows of A
    for j in range(3):          # Columns of B
        for k in range(3):      # Columns of A / Rows of B
            result[i][j] += A[i][k] * B[k][j]

# Step 4: Print the result matrix
print("Resultant Matrix:")
for row in result:
    print(row)

# End of Program