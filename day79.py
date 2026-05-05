# Program: Check Balanced Parentheses using Stack

# Step 1: Define function to check balance
def is_balanced(expression):
    """
    Returns True if parentheses are balanced, else False
    Supports: (), {}, []
    """

    # Step 2: Initialize empty stack
    stack = []

    # Step 3: Define matching pairs
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Step 4: Traverse each character in expression
    for char in expression:

        # If opening bracket, push to stack
        if char in "({[":
            stack.append(char)

        # If closing bracket, check for match
        elif char in ")}]":
            if len(stack) == 0:
                return False   # No matching opening bracket

            top = stack.pop()

            # Check if popped element matches
            if pairs[char] != top:
                return False

    # Step 5: If stack is empty, it's balanced
    return len(stack) == 0


# Step 6: Take input from user
expr = input("Enter expression: ")

# Step 7: Check and print result
if is_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")

# End of Program
