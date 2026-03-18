# Program to Find the Frequency of a Specific Character in a String

# Step 1: Take the main string input from the user
text = input("Enter a string: ")

# Step 2: Take the character whose frequency needs to be counted
target = input("Enter the character to find frequency: ")

# Step 3: Initialize a counter variable
count = 0

# Step 4: Loop through each character in the string
for char in text:

    # Step 5: Compare each character with the target character
    if char == target:
        count += 1   # Increase count if match is found

# Step 6: Print the final frequency
print("Frequency of", target, "is:", count)

# End of Program
