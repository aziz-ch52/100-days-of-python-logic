# Program: Find the Shortest and Longest Word in a File

# Step 1: Take file name input from the user
file_name = input("Enter file name: ")

try:
    # Step 2: Open the file in read mode
    with open(file_name, "r") as file:

        # Step 3: Read all content from the file
        content = file.read()

    # Step 4: Split content into words
    words = content.split()

    # Step 5: Check if file contains words
    if len(words) == 0:
        print("File is empty.")

    else:
        # Step 6: Initialize shortest and longest with the first word
        shortest_word = words[0]
        longest_word = words[0]

        # Step 7: Traverse all words
        for word in words:

            # Check for the shortest word
            if len(word) < len(shortest_word):
                shortest_word = word

            # Check for the longest word
            if len(word) > len(longest_word):
                longest_word = word

        # Step 8: Print results
        print("Shortest word:", shortest_word)
        print("Longest word:", longest_word)

# Step 9: Handle file not found error
except FileNotFoundError:
    print("File not found.")

# End of Program
