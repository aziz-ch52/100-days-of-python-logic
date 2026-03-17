# Program to Remove All Whitespace from a String Manually
# (Without using replace(), strip(), or other built-in whitespace removal methods)

# Step 1: Take input from the user
text = input("Enter a string: ")

# Step 2: Initialize an empty string to store the result
result = ""

# Step 3: Traverse each character in the string
for char in text:

    # Step 4: Check if the character is NOT a whitespace
    # Whitespace includes: space, tab, newline
    if char != " " and char != "\t" and char != "\n":
        result += char   # Add character to result

# Step 5: Print the final string without whitespace
print("String without whitespace:", result)

# End of Program