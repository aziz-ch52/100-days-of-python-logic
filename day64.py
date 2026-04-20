# Program to Find the First Non-Repeating Character in a String

# Step 1: Take input from the user
text = input("Enter a string: ")

# Step 2: Create a dictionary to store frequency of each character
frequency = {}

# Step 3: Count occurrences of each character
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Step 4: Traverse the string again to find first non-repeating character
for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    # Step 5: If no such character found
    print("No non-repeating character found")

# End of Program
