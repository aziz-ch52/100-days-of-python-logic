# Validate Sudoku Sub-grid

# Problem:
# Given a 3x3 Sudoku sub-grid,
# check whether it is valid or not.

# Rules:
# - Numbers must be from 1 to 9
# - No duplicate numbers allowed
# - Empty cells can be represented using '.'

# Example Valid Grid:
#
# [
#     ["5", "3", "."],
#     ["6", ".", "1"],
#     [".", "9", "8"]
# ]

# Example Invalid Grid:

# [
#     ["5", "3", "5"],   # Duplicate 5
#     ["6", ".", "1"],
#     [".", "9", "8"]
# ]


class Solution:

    def isValidSubGrid(self, grid: list[list[str]]) -> bool:

        # -----------------------------------------
        # Set is used to track already seen numbers
        # -----------------------------------------
        seen = set()

        # -----------------------------------------
        # Traverse all rows and columns
        # -----------------------------------------
        for row in range(3):

            for col in range(3):

                # Current cell value
                value = grid[row][col]

                # Ignore empty cells
                if value == ".":
                    continue

                # ---------------------------------
                # Check for duplicate
                # ---------------------------------
                if value in seen:
                    return False

                # Add value into set
                seen.add(value)

        # If no duplicates found
        return True


# -----------------------------------------
# DRIVER CODE / TESTING
# -----------------------------------------

solution = Solution()

# Valid sub-grid
grid1 = [
    ["5", "3", "."],
    ["6", ".", "1"],
    [".", "9", "8"]
]

# Invalid sub-grid (duplicate 5)
grid2 = [
    ["5", "3", "5"],
    ["6", ".", "1"],
    [".", "9", "8"]
]

print(solution.isValidSubGrid(grid1))
# Output: True

print(solution.isValidSubGrid(grid2))
# Output: False