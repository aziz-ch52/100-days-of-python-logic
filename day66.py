# Program: Function using *args to return the product of all arguments

# Step 1: Define function with *args (accepts variable number of arguments)
def product_of_numbers(*args):
    """
    Returns the product of all given numbers.
    """

    # Step 2: Initialize product as 1 (multiplicative identity)
    product = 1

    # Step 3: Multiply all values in args
    for num in args:
        product *= num

    # Step 4: Return final product
    return product


# Step 5: Example usage
result = product_of_numbers(2, 3, 4, 5)

# Step 6: Print result
print("Product:", result)

# End of Program