# Program to Swap Two Variables Without Using a Third Variable

# Step 1: Assign initial values
a = 10
b = 25

print("Before Swapping:")
print("a =", a)
print("b =", b)

# -------------------------------
# Method 1: Using Arithmetic Operators
# -------------------------------

# Step 2: Add both numbers and store in 'a'
a = a + b

# Step 3: Subtract new 'b' from 'a' to get original 'a'
b = a - b

# Step 4: Subtract new 'b' from 'a' to get original 'b'
a = a - b

print("\nAfter Swapping (Arithmetic Method):")
print("a =", a)
print("b =", b)

# -------------------------------
# Method 2: Using Python Tuple Unpacking (Recommended)
# -------------------------------

# Reassign original values
a = 10
b = 25

# Step 5: Swap in a single line (no third variable used)
a, b = b, a

print("\nAfter Swapping (Tuple Unpacking Method):")
print("a =", a)
print("b =", b)

# End of Program