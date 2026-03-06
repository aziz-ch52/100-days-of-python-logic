# Program to Find the Least Common Multiple (LCM) of Two Numbers

# Step 1: Take input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Step 2: Store original values (needed later for LCM formula)
x = a
y = b

# Step 3: Convert numbers to positive values
a = abs(a)
b = abs(b)

# Step 4: Find GCD using Euclidean Algorithm
while b != 0:
    temp = b
    b = a % b
    a = temp

gcd = a  # Final value of 'a' is the GCD

# Step 5: Use formula
# LCM(a, b) = |x * y| / GCD(a, b)
lcm = abs(x * y) // gcd

# Step 6: Print result
print("LCM is:", lcm)

# End of Program
