# Program to Check if a String is a Palindrome
# A palindrome reads the same forward and backward

# Step 1: Take input from the user
text = input("Enter a string: ")

# Step 2: Initialize variables for manual reversal
reversed_text = ""

# Step 3: Reverse the string using a loop (without slicing)
for char in text:
    reversed_text = char + reversed_text

# Step 4: Compare the original string with the reversed string
if text == reversed_text:
    print("The string is a Palindrome")
else:
    print("The string is NOT a Palindrome")

# End of Program
