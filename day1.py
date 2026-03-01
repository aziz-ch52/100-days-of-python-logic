# Program to Check Whether a Number is Even or Odd

# Step 1: Take integer input from the user
num = int(input("Enter a number: "))

# Step 2: Use the modulus operator to check the remainder when divided by 2
# If remainder is 0 → Even number
# If remainder is not 0 → Odd number
if num % 2 == 0:
    print("The number is EVEN")
else:
    print("The number is ODD")

# Step 3: Indicate program completion
print("Program Completed")
