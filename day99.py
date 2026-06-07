# LeetCode 118: Pascal's Triangle

# Problem:
# Given an integer numRows, return the first numRows
# of Pascal's Triangle.

# Pascal's Triangle Rule:
# - First and last element of every row is 1.
# - Every middle element is the sum of the two
#   elements directly above it.

# Example:
# Input: numRows = 5

# Output:
# [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1]
# ]


class Solution:

    def generate(self, numRows: int) -> list[list[int]]:

        # Store the complete Pascal's Triangle
        triangle = []

        # Generate each row one by one
        for row in range(numRows):

            # Create a row filled with 1s
            current_row = [1] * (row + 1)

            # Fill middle elements
            # First and last elements remain 1
            for col in range(1, row):

                current_row[col] = (
                    triangle[row - 1][col - 1]
                    + triangle[row - 1][col]
                )

            # Add current row to triangle
            triangle.append(current_row)

        return triangle


# --------------------------------------------------
# DRIVER CODE / TESTING
# --------------------------------------------------

solution = Solution()

numRows = 5

result = solution.generate(numRows)

# Print Pascal's Triangle row by row
for row in result:
    print(row)

# Output:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
