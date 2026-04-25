# Program to Find the Sum of a List Using Recursion

# Step 1: Define a recursive function
def recursive_sum(lst):
    """
    Returns the sum of elements in a list using recursion
    """

    # Step 2: Base case
    # If the list is empty, the sum is 0
    if len(lst) == 0:
        return 0

    # Step 3: Recursive case
    # First element + sum of remaining list
    return lst[0] + recursive_sum(lst[1:])


# Step 4: Take input from the user (space-separated numbers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 5: Call the function and print the result
print("Sum of list:", recursive_sum(numbers))

# End of Program
