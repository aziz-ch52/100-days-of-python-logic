# 92. Count lines, words, and characters in a file

# Open the file in read mode
file = open("sample.txt", "r")

# Read file content
content = file.read()

# Count lines
lines = content.split('\n')
line_count = len(lines)

# Count words
words = content.split()
word_count = len(words)

# Count characters
char_count = len(content)

# Display results
print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Number of characters:", char_count)

# Close the file
file.close()
