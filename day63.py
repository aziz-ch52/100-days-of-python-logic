# Program to Check if Two Strings are Anagrams
# (Without using built-in sorting functions)

# Step 1: Take input from the user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Step 2: Remove spaces and convert to lowercase for uniform comparison
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Step 3: If lengths are different, they cannot be anagrams
if len(str1) != len(str2):
    print("Not Anagrams")

else:
    # Step 4: Initialize frequency dictionaries
    freq1 = {}
    freq2 = {}

    # Step 5: Count frequency of characters in str1
    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    # Step 6: Count frequency of characters in str2
    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    # Step 7: Compare both frequency dictionaries
    if freq1 == freq2:
        print("Anagrams")
    else:
        print("Not Anagrams")

# End of Program
