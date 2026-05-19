# Program: Quick Sort Implementation using Recursion

# Step 1: Define Quick Sort function
def quick_sort(arr):

    # Step 2: Base case
    # If list has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Step 3: Choose pivot element
    pivot = arr[len(arr) // 2]

    # Step 4: Create three lists
    left = []     # Elements smaller than pivot
    middle = []   # Elements equal to pivot
    right = []    # Elements greater than pivot

    # Step 5: Partition elements
    for num in arr:

        if num < pivot:
            left.append(num)

        elif num > pivot:
            right.append(num)

        else:
            middle.append(num)

    # Step 6: Recursively sort left and right parts
    return quick_sort(left) + middle + quick_sort(right)


# Step 7: Take input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 8: Call Quick Sort
sorted_numbers = quick_sort(numbers)

# Step 9: Print sorted result
print("Sorted list:", sorted_numbers)

# End of Program
