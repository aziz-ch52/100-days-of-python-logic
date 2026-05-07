# Program: Find the Majority Element in a List
# Majority Element = element appearing more than n // 2 times

# Step 1: Take input from the user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Initialize variables for Boyer-Moore Voting Algorithm
candidate = None
count = 0

# Step 3: Find potential majority candidate
for num in numbers:

    if count == 0:
        candidate = num
        count = 1

    elif num == candidate:
        count += 1

    else:
        count -= 1

# Step 4: Verify if candidate is actually a majority element
frequency = 0

for num in numbers:
    if num == candidate:
        frequency += 1

# Step 5: Print result
if frequency > len(numbers) // 2:
    print("Majority Element:", candidate)
else:
    print("No Majority Element Found")

# End of Program
