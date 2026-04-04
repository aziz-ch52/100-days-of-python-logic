# Program to Extract All Even Numbers from a List

# Step 1: Take input from the user (space-separated numbers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Initialize an empty list to store even numbers
even_numbers = []

# Step 3: Traverse the list
for num in numbers:

    # Step 4: Check if the number is even
    if num % 2 == 0:
        even_numbers.append(num)

# Step 5: Print the result
print("Even numbers:", even_numbers)

# End of Program
