# Program to Map Two Lists into a Dictionary

# Step 1: Take input for keys and values (space-separated)
keys = input("Enter keys separated by space: ").split()
values = list(map(int, input("Enter values separated by space: ").split()))

# Step 2: Check if both lists have the same length
if len(keys) != len(values):
    print("Error: Number of keys and values must be equal.")

else:
    # Step 3: Initialize empty dictionary
    mapped_dict = {}

    # Step 4: Map keys to values
    for i in range(len(keys)):
        mapped_dict[keys[i]] = values[i]

    # Step 5: Print the resulting dictionary
    print("Mapped Dictionary:")
    for key in mapped_dict:
        print(key, ":", mapped_dict[key])

# End of Program
