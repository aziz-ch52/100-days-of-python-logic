# Program to Implement Binary Search (on a sorted list)

# Step 1: Take input from the user (must be sorted)
numbers = list(map(int, input("Enter sorted numbers separated by space: ").split()))

# Step 2: Take the target element to search
target = int(input("Enter the element to search: "))

# Step 3: Initialize low and high pointers
low = 0
high = len(numbers) - 1

# Step 4: Perform Binary Search
found = False

while low <= high:
    
    # Step 5: Find middle index
    mid = (low + high) // 2

    # Step 6: Compare middle element with target
    if numbers[mid] == target:
        print("Element found at index:", mid)
        found = True
        break

    # Step 7: If target is smaller, search left half
    elif target < numbers[mid]:
        high = mid - 1

    # Step 8: If target is greater, search right half
    else:
        low = mid + 1

# Step 9: If element not found
if not found:
    print("Element not found in the list")

# End of Program
