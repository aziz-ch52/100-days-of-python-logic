# Program to calculate the sum of all digits of an integer

# Step 1: Take integer input from user
num = int(input("Enter an integer: "))

# Step 2: Store the number in another variable (optional, for reference)
original_num = num

# Step 3: Convert a negative number to a positive number
# Because digit extraction works properly with positive numbers
if num < 0:
    num = -num

# Step 4: Initialize a variable to store the sum
digit_sum = 0

# Step 5: Use a while loop to extract digits one by one
while num > 0:
    digit = num % 10        # Get last digit
    digit_sum += digit      # Add digit to sum
    num = num // 10         # Remove last digit

# Step 6: Display result
print(f"Sum of digits of {original_num} is: {digit_sum}")
