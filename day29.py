# Program to Find the Frequency of a Specific Character in a String

# Step 1: Take input string from the user
text = input("Enter a string: ")

# Step 2: Take the character whose frequency we want to find
target = input("Enter the character to count: ")

# Step 3: Initialize counter
count = 0

# Step 4: Traverse the string character by character
for char in text:

    # Step 5: Compare each character with the target
    if char == target:
        count += 1

# Step 6: Print the result
print("Frequency of", target, "is:", count)

# End of Program
