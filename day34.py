# Program to Calculate the Average of a List

# Step 1: Take input from the user (space-separated numbers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Check if the list is not empty
if len(numbers) == 0:
    print("List is empty. Cannot calculate average.")

else:
    # Step 3: Initialize sum variable
    total = 0

    # Step 4: Traverse the list and calculate sum
    for num in numbers:
        total += num

    # Step 5: Calculate average
    average = total / len(numbers)

    # Step 6: Print result
    print("Average:", average)

# End of Program