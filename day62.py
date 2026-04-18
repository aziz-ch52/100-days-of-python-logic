# Program to Find the Longest Word in a Sentence

# Step 1: Take input sentence from the user
sentence = input("Enter a sentence: ")

# Step 2: Split the sentence into words
words = sentence.split()

# Step 3: Initialize variables
longest_word = ""
max_length = 0

# Step 4: Traverse each word
for word in words:

    # Step 5: Check length of current word
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

# Step 6: Print the result
print("Longest word:", longest_word)
print("Length:", max_length)

# End of Program
