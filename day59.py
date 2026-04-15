# Program to Sort a Dictionary by Values (Ascending Order)

# Step 1: Take the number of key-value pairs from the user
n = int(input("Enter number of elements: "))

# Step 2: Create a dictionary
data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

# Step 3: Convert dictionary items to a list of tuples
items = list(data.items())

# Step 4: Apply simple sorting (Selection Sort based on values)
for i in range(len(items)):
    min_index = i

    for j in range(i + 1, len(items)):
        if items[j][1] < items[min_index][1]:
            min_index = j

    # Swap elements
    items[i], items[min_index] = items[min_index], items[i]

# Step 5: Convert sorted list back to dictionary
sorted_dict = {}

for key, value in items:
    sorted_dict[key] = value

# Step 6: Print sorted dictionary
print("Dictionary sorted by values:")
for key in sorted_dict:
    print(key, ":", sorted_dict[key])

# End of Program
