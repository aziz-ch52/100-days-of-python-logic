# Program to count the number of digits in an integer

# Step 1: Take integer input from user
num = int(input("Enter an integer: "))

# Step 2: Handle special case when number is 0
# Because the while loop won't run for 0
if num == 0:
    digit_count = 1
else:
    # Step 3: Convert a negative number to a positive number
    # Digits are counted without considering the minus sign
    num = abs(num)
    
    digit_count = 0
    
    # Step 4: Remove digits one by one using floor division
    while num > 0:
        num = num // 10      # Remove last digit
        digit_count += 1     # Increase counter

# Step 5: Print result
print("Number of digits:", digit_count)
