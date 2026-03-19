# Program to Find the Largest and Smallest Element in a List

# Step 1: Take input list from the user
# Input should be space-separated numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Initialize largest and smallest with the first element
largest = numbers[0]
smallest = numbers[0]

# Step 3: Traverse the list
for num in numbers:

    # Step 4: Check for largest
    if num > largest:
        largest = num

    # Step 5: Check for smallest
    if num < smallest:
        smallest = num

# Step 6: Print results
print("Largest element:", largest)
print("Smallest element:", smallest)

# End of Program