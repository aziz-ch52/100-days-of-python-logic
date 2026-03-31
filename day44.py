# Program to Implement Bubble Sort

# Step 1: Take input from the user (space-separated numbers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Get the length of the list
n = len(numbers)

# Step 3: Apply Bubble Sort algorithm
# Outer loop for passes
for i in range(n):

    # Step 4: Inner loop for comparing adjacent elements
    # After each pass, the largest element moves to the end
    for j in range(0, n - i - 1):

        # Step 5: Swap if elements are in wrong order
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Step 6: Print sorted list
print("Sorted list:", numbers)

# End of Program