# Program: Solve the Two Sum Problem

# Problem:
# Find two indices such that their corresponding values add up to the target.

# Step 1: Take input list from the user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Take target value
target = int(input("Enter target sum: "))

# Step 3: Create dictionary to store visited numbers and their indices
seen = {}

# Step 4: Traverse the list
for index in range(len(numbers)):

    current = numbers[index]

    # Step 5: Calculate required complement
    complement = target - current

    # Step 6: Check if complement already exists
    if complement in seen:
        print("Indices:", seen[complement], "and", index)
        print("Values:", complement, "and", current)
        break

    # Step 7: Store current number with its index
    seen[current] = index

else:
    # Executes if no pair is found
    print("No two numbers add up to the target.")

# End of Program