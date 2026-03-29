# Program to Capitalize the First Letter of Every Word Manually
# (Without using title() or capitalize())

# Step 1: Take input from the user
text = input("Enter a sentence: ")

# Step 2: Initialize result string and a flag
result = ""
capitalize_next = True   # Indicates when the next character should be capitalized

# Step 3: Traverse each character in the string
for char in text:

    # Step 4: If flag is True and character is alphabetic, capitalize it
    if capitalize_next and char.isalpha():
        result += char.upper()
        capitalize_next = False

    else:
        result += char

    # Step 5: If space is found, the next character should be capitalized
    if char == " ":
        capitalize_next = True

# Step 6: Print the modified string
print("Capitalized Sentence:", result)

# End of Program
