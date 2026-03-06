# Program to Generate a Multiplication Table for a Number (Without using f-strings)

# Step 1: Take input from the user
n = int(input("Enter a number: "))

# Step 2: Loop from 1 to 10 to generate the table
for i in range(1, 11):

    # Step 3: Calculate the multiplication result
    result = n * i

    # Step 4: Print the table line without using f-strings
    print(n, "x", i, "=", result)

# End of Program