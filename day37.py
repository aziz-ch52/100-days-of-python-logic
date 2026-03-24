# Program to Remove Duplicates from a List WITHOUT using set()

# Step 1: Take input from the user (space-separated numbers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Initialize an empty list to store unique elements
unique_list = []

# Step 3: Traverse the original list
for num in numbers:

    # Step 4: Check if the element is NOT already in unique_list
    if num not in unique_list:
        unique_list.append(num)   # Add unique element

# Step 5: Print the list without duplicates
print("List after removing duplicates:", unique_list)

# End of Program