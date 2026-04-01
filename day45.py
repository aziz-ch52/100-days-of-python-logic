# Program to Implement Selection Sort

# Step 1: Take input from the user (space-separated numbers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Get the length of the list
n = len(numbers)

# Step 3: Apply Selection Sort algorithm
# Outer loop to iterate over each position
for i in range(n):

    # Step 4: Assume the current index has the minimum value
    min_index = i

    # Step 5: Find the actual minimum element in the remaining list
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j

    # Step 6: Swap the found minimum element with the current element
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# Step 7: Print the sorted list
print("Sorted list:", numbers)

# End of Program
