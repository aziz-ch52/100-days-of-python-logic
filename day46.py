# Program to Find the Intersection of Two Lists
# (Common elements between both lists, without using set())

# Step 1: Take input for two lists (space-separated numbers)
list1 = list(map(int, input("Enter list 1: ").split()))
list2 = list(map(int, input("Enter list 2: ").split()))

# Step 2: Initialize an empty list to store intersection
intersection = []

# Step 3: Traverse elements of list1
for num in list1:

    # Step 4: Check if element exists in list2 and not already added
    if num in list2 and num not in intersection:
        intersection.append(num)

# Step 5: Print the intersection result
print("Intersection of lists:", intersection)

# End of Program