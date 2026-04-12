# Program to Check if a Matrix is an Identity Matrix

# Step 1: Take the size of a square matrix from the user
n = int(input("Enter size of square matrix (n x n): "))

# Step 2: Take matrix input
matrix = []
print("Enter matrix elements row-wise:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Assume matrix is identity
is_identity = True

# Step 4: Check conditions
for i in range(n):
    for j in range(n):

        # Diagonal elements must be 1
        if i == j:
            if matrix[i][j] != 1:
                is_identity = False
                break

        # Non-diagonal elements must be 0
        else:
            if matrix[i][j] != 0:
                is_identity = False
                break

    # Step 5: Exit outer loop early if condition fails
    if not is_identity:
        break

# Step 6: Print result
if is_identity:
    print("The matrix is an Identity Matrix")
else:
    print("The matrix is NOT an Identity Matrix")

# End of Program
