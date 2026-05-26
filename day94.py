#Topic:
# Dynamic Programming

# Idea:
# To reach the current stair, we can come from:

# 1. Previous stair (1 step jump)
# 2. Two stairs before (2-step jump)

# Therefore:

# dp[i] = dp[i - 1] + dp[i - 2]

# This is exactly the Fibonacci pattern.


class Solution:

    def climbStairs(self, n: int) -> int:

        # -----------------------------------------
        # BASE CASES
        # -----------------------------------------

        # Only 1 way to reach stair 1
        if n == 1:
            return 1

        # Two ways to reach stair 2:
        # 1+1
        # 2
        if n == 2:
            return 2

        # -----------------------------------------
        # INITIAL VALUES
        # -----------------------------------------

        # Ways to reach stair 1
        prev2 = 1

        # Ways to reach stair 2
        prev1 = 2

        # -----------------------------------------
        # BUILD ANSWER ITERATIVELY
        # -----------------------------------------

        # Start from stair 3 up to n
        for stair in range(3, n + 1):

            # Current stair ways
            current = prev1 + prev2

            # Shift values forward
            prev2 = prev1
            prev1 = current

        # prev1 now contains answer for stair n
        return prev1


# -----------------------------------------
# DRIVER CODE / TESTING
# -----------------------------------------

solution = Solution()

print(solution.climbStairs(1))   # 1
print(solution.climbStairs(2))   # 2
print(solution.climbStairs(3))   # 3
print(solution.climbStairs(4))   # 5
print(solution.climbStairs(5))   # 8
