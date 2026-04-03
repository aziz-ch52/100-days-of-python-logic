# Program to Find the Union of Two Lists Without Duplicates

# Step 1: Take input for two lists (space-separated numbers)
list1 = list(map(int, input("Enter list 1: ").split()))
list2 = list(map(int, input("Enter list 2: ").split()))

# Step 2: Initialize result list for union
union_list = []

# Step 3: Add elements from list1 (avoid duplicates)
for num in list1:
    if num not in union_list:
        union_list.append(num)

# Step 4: Add elements from list2 (avoid duplicates)
for num in list2:
    if num not in union_list:
        union_list.append(num)

# Step 5: Print the union result
print("Union of lists:", union_list)

# End of Program
