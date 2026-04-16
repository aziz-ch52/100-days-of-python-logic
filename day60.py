# Program to Merge Two Dictionaries (Sum Overlapping Keys)

# Step 1: Take the number of elements for the first dictionary
n1 = int(input("Enter number of elements in first dictionary: "))
dict1 = {}

# Step 2: Input key-value pairs for the first dictionary
for i in range(n1):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

# Step 3: Take the number of elements for the second dictionary
n2 = int(input("Enter number of elements in second dictionary: "))
dict2 = {}

# Step 4: Input key-value pairs for the second dictionary
for i in range(n2):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict2[key] = value

# Step 5: Initialize merged dictionary
merged_dict = {}

# Step 6: Add elements from the first dictionary
for key in dict1:
    merged_dict[key] = dict1[key]

# Step 7: Merge the second dictionary
for key in dict2:
    if key in merged_dict:
        merged_dict[key] += dict2[key]   # Sum values for overlapping keys
    else:
        merged_dict[key] = dict2[key]

# Step 8: Print merged dictionary
print("Merged Dictionary:")
for key in merged_dict:
    print(key, ":", merged_dict[key])

# End of Program
