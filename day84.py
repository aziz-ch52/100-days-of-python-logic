# Program: Maximum Subarray Sum using Kadane's Algorithm

# Step 1: Take input list from the user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Handle empty list
if len(numbers) == 0:
    print("List is empty.")

else:
    # Step 3: Initialize current_sum and max_sum
    current_sum = numbers[0]
    max_sum = numbers[0]

    # Step 4: Traverse the list starting from second element
    for i in range(1, len(numbers)):

        # Either extend current subarray or start new subarray
        current_sum = max(numbers[i], current_sum + numbers[i])

        # Update maximum sum if needed
        max_sum = max(max_sum, current_sum)

    # Step 5: Print result
    print("Maximum Subarray Sum:", max_sum)

# End of Program