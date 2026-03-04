# Program to Find the Greatest Common Divisor (GCD)
# Using the Euclidean Algorithm

# Step 1: Take two integer inputs from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Step 2: Convert numbers to positive values (GCD is always positive)
a = abs(a)
b = abs(b)

# Step 3: Apply Euclidean Algorithm
# Repeat until b becomes 0
while b != 0:
    temp = b        # Store current value of b
    b = a % b       # Update b with the remainder of a divided by b
    a = temp        # Update a with the previous value of b

# Step 4: When b becomes 0, 'a' contains the GCD
print("GCD is:", a)

# End of Program
