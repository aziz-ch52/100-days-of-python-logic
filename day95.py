
# Problem:
# Given a list of strings, find the longest common prefix string
# among all strings.

# Example:
# Input:
# strs = ["flower", "flow", "flight"]

# Output:
# "fl"

# Explanation:
# All strings start with "fl"


class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:

        # -----------------------------------------
        # EDGE CASE:
        # If the list is empty, return an empty string
        # -----------------------------------------
        if not strs:
            return ""

        # -----------------------------------------
        # Start by assuming the first string
        # is the common prefix
        # -----------------------------------------
        prefix = strs[0]

        # -----------------------------------------
        # Compare prefix with every other string
        # -----------------------------------------
        for word in strs[1:]:

            # Keep reducing prefix until:
            # current word starts with prefix
            while not word.startswith(prefix):

                # Remove last character from prefix
                prefix = prefix[:-1]

                # If prefix becomes empty,
                # there is no common prefix
                if prefix == "":
                    return ""

        # Final common prefix
        return prefix


# -----------------------------------------
# DRIVER CODE / TESTING
# -----------------------------------------

solution = Solution()

print(solution.longestCommonPrefix(
    ["flower", "flow", "flight"]
))
# Output: fl

print(solution.longestCommonPrefix(
    ["dog", "racecar", "car"]
))
# Output:

print(solution.longestCommonPrefix(
    ["interview", "internet", "internal"]
))
# Output: inte

print(solution.longestCommonPrefix(
    ["apple"]
))
# Output: apple
