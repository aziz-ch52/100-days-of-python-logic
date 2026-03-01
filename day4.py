"""
FizzBuzz for Multiples of 3, 5, and 7

Rules:
- If divisible by 3 → print "Fizz."
- If divisible by 5 → print "Buzz."
- If divisible by 7 → print "Boom."
- If divisible by more than one → combine the words
- Otherwise → print the number
"""

# Step 1: Loop through numbers from 1 to 100 (inclusive)
for num in range(1, 101):

    # Step 2: Initialize an empty string to build the result
    result = ""

    # Step 3: Check divisibility conditions independently

    # If divisible by 3, append "Fizz."
    if num % 3 == 0:
        result += "Fizz"

    # If divisible by 5, append "Buzz."
    if num % 5 == 0:
        result += "Buzz"

    # If divisible by 7, append "Boom."
    if num % 7 == 0:
        result += "Boom"

    # Step 4: If the result is still empty, no condition matched
    # So print the number itself
    if result == "":
        print(num)
    else:
        # Otherwise, print the combined result
        print(result)

# End of Program
