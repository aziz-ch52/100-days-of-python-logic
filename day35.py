# Program to Check if a List is Sorted (Ascending Order)

# Step 1: Take input from the user (space-separated numbers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Assume the list is sorted initially
is_sorted = True

# Step 3: Traverse the list and compare adjacent elements
for i in range(len(numbers) - 1):

    # If any element is greater than the next one, the list is not sorted
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break

# Step 4: Print result
if is_sorted:
    print("The list is sorted in ascending order.")
else:
    print("The list is NOT sorted.")

# End of Program
