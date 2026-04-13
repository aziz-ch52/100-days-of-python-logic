# Program to Find the Row with Maximum Sum in a Matrix

# Step 1: Take matrix size input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Step 2: Take matrix input
matrix = []
print("Enter matrix elements row-wise:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Initialize variables
max_sum = float('-inf')
max_row_index = -1

# Step 4: Traverse each row to calculate the sum
for i in range(rows):
    row_sum = 0

    for j in range(cols):
        row_sum += matrix[i][j]

    # Step 5: Check if this row has the maximum sum so far
    if row_sum > max_sum:
        max_sum = row_sum
        max_row_index = i

# Step 6: Print result
print("Row with maximum sum is at index:", max_row_index)
print("Maximum sum:", max_sum)

# End of Program
