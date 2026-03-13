# Program to Reverse a String Without Using Slicing

# Step 1: Take input string from the user
text = input("Enter a string: ")

# Step 2: Initialize an empty string to store the reversed result
reversed_text = ""

# Step 3: Traverse the original string character by character
for char in text:
    
    # Step 4: Add each character to the front of reversed_text
    reversed_text = char + reversed_text

# Step 5: Print the reversed string
print("Reversed string:", reversed_text)

# End of Program
