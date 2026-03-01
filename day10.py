# Program to Reverse an Integer WITHOUT converting it to a string

def reverse_integer(n):
    """
    Reverses an integer without using string conversion.

    Parameters:
        n (int): The integer to reverse

    Returns:
        int: The reversed integer
    """

    # Step 1: Store the sign of the number
    # If the number is negative, remember it and work with the positive version
    sign = -1 if n < 0 else 1

    # Step 2: Convert the number to positive for processing
    n = abs(n)

    # Step 3: Initialize reversed_number as 0
    reversed_number = 0

    # Step 4: Extract digits one by one using modulus and division
    while n != 0:
        digit = n % 10                 # Get last digit
        reversed_number = reversed_number * 10 + digit  # Append digit
        n = n // 10                    # Remove last digit

    # Step 5: Restore original sign
    return sign * reversed_number


# Example usage
print(reverse_integer(1234))   # Output: 4321
print(reverse_integer(-567))   # Output: -765
print(reverse_integer(1200))   # Output: 21
