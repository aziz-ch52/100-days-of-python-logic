# Program to Find the Largest of Three Numbers Using Only Nested if Statements

# Step 1: Assign values to three numbers
num1 = 5
num2 = 25
num3 = 15

# Step 2: Compare num1 with num2
if num1 >= num2:
    
    # Step 3: If num1 is greater than or equal to num2,
    # compare num1 with num3
    if num1 >= num3:
        print(f"Number 1 is the largest: {num1}")
    else:
        print(f"Number 3 is the largest: {num3}")

else:
    
    # Step 4: If num2 is greater than num1,
    # compare num2 with num3
    if num2 >= num3:
        print(f"Number 2 is the largest: {num2}")
    else:
        print(f"Number 3 is the largest: {num3}")
