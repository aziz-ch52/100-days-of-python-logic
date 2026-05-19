# Program: Implement Insertion Sort

# Step 1: Take input from the user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Traverse the list starting from index 1
for i in range(1, len(numbers)):

    # Step 3: Store current element
    key = numbers[i]

    # Step 4: Compare with previous elements
    j = i - 1

    # Shift elements greater than key to one position ahead
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1

    # Step 5: Insert the key at the correct position
    numbers[j + 1] = key

# Step 6: Print sorted list
print("Sorted list:", numbers)

# End of Program
