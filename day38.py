# Program to Merge Two Sorted Lists (Without Using Built-in Merge Functions)

# Step 1: Take input for two sorted lists
list1 = list(map(int, input("Enter sorted list 1: ").split()))
list2 = list(map(int, input("Enter sorted list 2: ").split()))

# Step 2: Initialize pointers and result list
i = 0   # Pointer for list1
j = 0   # Pointer for list2
merged_list = []

# Step 3: Traverse both lists and compare elements
while i < len(list1) and j < len(list2):

    # Step 4: Append the smaller element
    if list1[i] <= list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1

# Step 5: Add remaining elements (if any) from list1
while i < len(list1):
    merged_list.append(list1[i])
    i += 1

# Step 6: Add remaining elements (if any) from list2
while j < len(list2):
    merged_list.append(list2[j])
    j += 1

# Step 7: Print merged sorted list
print("Merged sorted list:", merged_list)

# End of Program