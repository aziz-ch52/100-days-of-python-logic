"""
FizzBuzz for Multiples of 3, 5, and 7

Rules:
- If divisible by 3 → print "Fizz"
- If divisible by 5 → print "Buzz"
- If divisible by 7 → print "Boom"
- If divisible by more than one → combine the words
- Otherwise → print the number
"""

# Loop from 1 to 100 (inclusive)
for num in range(1, 101):

    # Create an empty string to store result
    result = ""

    # Check divisibility by 3
    if num % 3 == 0:
        result += "Fizz"

    # Check divisibility by 5
    if num % 5 == 0:
        result += "Buzz"

    # Check divisibility by 7
    if num % 7 == 0:
        result += "Boom"

    # If no condition matched, print the number
    if result == "":
        print(num)
    else:
        print(result)

# END
