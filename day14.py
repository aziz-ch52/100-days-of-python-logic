# Program to check whether a number is an Armstrong number

# Take input from user
num = int(input("Enter a number: "))

# Store the original number
original_num = num

# Step 1: Count the number of digits
# Convert number to string and calculate length
num_digits = len(str(num))

# Variable to store the sum of powered digits
sum_of_powers = 0

# Step 2: Extract digits one by one
while num > 0:
    
    # Get last digit using modulus operator
    digit = num % 10
    
    # Raise digit to the power of total digits
    sum_of_powers += digit ** num_digits
    
    # Remove the last digit from the number
    num = num // 10

# Step 3: Compare the result with the original number
if sum_of_powers == original_num:
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is NOT an Armstrong number")

# End
