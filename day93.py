# Program: Find Intersection of Two Arrays using Dictionary

# Step 1: Take input for the first array
array1 = list(map(int, input("Enter elements of first array: ").split()))

# Step 2: Take input for the second array
array2 = list(map(int, input("Enter elements of second array: ").split()))

# Step 3: Create a dictionary for the elements of the first array
element_dict = {}

for num in array1:
    element_dict[num] = True

# Step 4: Find common elements
intersection = []

for num in array2:

    # Check if element exists in dictionary
    # Also, avoid duplicate entries in the result
    if num in element_dict and num not in intersection:
        intersection.append(num)

# Step 5: Print result
print("Intersection:", intersection)

# End of Program
