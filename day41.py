# Program to Find the Missing Number in a List (from 1 to N)

# Step 1: Take input for the list (numbers between 1 and N with one missing)
numbers = list(map(int, input("Enter numbers separated by space (from 1 to N, one missing): ").split()))

# Step 2: Calculate N (the length of the complete list + 1)
N = len(numbers) + 1

# Step 3: Calculate the expected sum of numbers from 1 to N using the formula for sum of an arithmetic series
expected_sum = N * (N + 1) // 2

# Step 4: Calculate the actual sum of the numbers in the list
actual_sum = sum(numbers)

# Step 5: The missing number is the difference between expected and actual sum
missing_number = expected_sum - actual_sum

# Step 6: Print the missing number
print("The missing number is:", missing_number)

# End of Program