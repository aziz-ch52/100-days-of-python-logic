# Program: Merge Sort Implementation

# Step 1: Define Merge Sort function
def merge_sort(arr):

    # Step 2: Base case
    # If array has 1 or fewer elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Step 3: Find middle index
    mid = len(arr) // 2

    # Step 4: Divide array into left and right halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Step 5: Merge sorted halves
    return merge(left_half, right_half)


# Step 6: Define merge function
def merge(left, right):

    merged = []   # Final merged sorted list

    i = 0   # Pointer for left list
    j = 0   # Pointer for right list

    # Step 7: Compare elements and merge in sorted order
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Step 8: Add remaining elements from left list
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Step 9: Add remaining elements from right list
    while j < len(right):
        merged.append(right[j])
        j += 1

    # Step 10: Return merged sorted list
    return merged


# Step 11: Take input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 12: Call Merge Sort
sorted_numbers = merge_sort(numbers)

# Step 13: Print sorted result
print("Sorted list:", sorted_numbers)

# End of Program
