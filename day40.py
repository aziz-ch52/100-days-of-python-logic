# Program to Count Occurrences of Each Element in a List
# (Without using collections.Counter)

# Step 1: Take input from the user (space-separated numbers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Initialize an empty dictionary to store counts
frequency = {}

# Step 3: Traverse the list
for num in numbers:

    # Step 4: If element already exists, increment its count
    if num in frequency:
        frequency[num] += 1
    else:
        # If element is seen for the first time, set count to 1
        frequency[num] = 1

# Step 5: Print occurrences
print("Element frequencies:")
for key in frequency:
    print(key, "->", frequency[key])

# End of Program