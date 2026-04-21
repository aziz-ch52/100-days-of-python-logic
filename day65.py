# Program to Replace a Word in a Sentence WITHOUT using .replace()

# Step 1: Take input from the user
sentence = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

# Step 2: Split the sentence into words
words = sentence.split()

# Step 3: Traverse and replace manually
for i in range(len(words)):
    if words[i] == old_word:
        words[i] = new_word

# Step 4: Reconstruct the sentence manually
result = ""

for i in range(len(words)):
    result += words[i]
    
    # Add space between words (except after last word)
    if i != len(words) - 1:
        result += " "

# Step 5: Print updated sentence
print("Updated sentence:", result)

# End of Program
