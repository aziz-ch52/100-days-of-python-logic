# Program to Implement Linear Search

# Step 1: Take input list from the user (space-separated numbers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Take the target element to search
target = int(input("Enter the element to search: "))

# Step 3: Initialize a variable to track if the element is found
found = False

# Step 4: Traverse the list
for index in range(len(numbers)):

    # Step 5: Compare each element with the target
    if numbers[index] == target:
        print("Element found at index:", index)
        found = True
        break   # Stop after finding the first occurrence

# Step 6: If element not found after loop
if not found:
    print("Element not found in the list")

# End of Program
