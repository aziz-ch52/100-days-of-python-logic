# Program to Count Vowels and Consonants in a String

# Step 1: Take input from the user
text = input("Enter a string: ")

# Step 2: Initialize counters
vowels = 0
consonants = 0

# Step 3: Define vowel characters
vowel_letters = "aeiouAEIOU"

# Step 4: Traverse each character in the string
for char in text:

    # Check if the character is an alphabet letter
    if char.isalpha():

        # Step 5: Check if it is a vowel
        if char in vowel_letters:
            vowels += 1
        else:
            # Otherwise it is a consonant
            consonants += 1

# Step 6: Print results
print("Vowels:", vowels)
print("Consonants:", consonants)

# End of Program