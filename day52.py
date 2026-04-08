# Program to Add Two 3x3 Matrices

# Step 1: Initialize empty matrices
matrix1 = []
matrix2 = []
result = []

# Step 2: Take input for the first matrix
print("Enter elements for Matrix 1:")
for i in range(3):
    row = list(map(int, input(f"Enter 3 elements for row {i+1}: ").split()))
    matrix1.append(row)

# Step 3: Take input for the second matrix
print("Enter elements for Matrix 2:")
for i in range(3):
    row = list(map(int, input(f"Enter 3 elements for row {i+1}: ").split()))
    matrix2.append(row)

# Step 4: Add corresponding elements
for i in range(3):
    row = []
    for j in range(3):
        sum_value = matrix1[i][j] + matrix2[i][j]
        row.append(sum_value)
    result.append(row)

# Step 5: Print the result matrix
print("Resultant Matrix after Addition:")
for row in result:
    for element in row:
        print(element, end=" ")
    print()

# End of Program
