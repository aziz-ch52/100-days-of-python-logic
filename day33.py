# Program to Find the Second Largest Element in a List Without Sorting

# Step 1: Take input list from the user (space-separated integers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Check if the list has at least 2 elements
if len(numbers) < 2:
    print("List must contain at least two elements.")

else:
    # Step 3: Initialize largest and second largest to very small values
    largest = float('-inf')
    second_largest = float('-inf')

    # Step 4: Traverse the list
    for num in numbers:

        # If current number is greater than largest
        if num > largest:
            second_largest = largest   # Update second largest
            largest = num              # Update largest

        # If current number is between largest and second largest
        elif num > second_largest and num != largest:
            second_largest = num

    # Step 5: Check if second largest exists
    if second_largest == float('-inf'):
        print("No second largest element found (all elements may be equal).")
    else:
        print("Second largest element:", second_largest)

# End of Program