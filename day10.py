def reverse_integer(n):
    """
    Reverses an integer without converting it to a string.
    
    Parameters:
        n (int): The integer to reverse
        
    Returns:
        int: Reversed integer
    """
    
    # Store the sign of the number
    sign = -1 if n < 0 else 1
    
    # Work with positive values for easier processing
    n = abs(n)
    
    reversed_number = 0
    
    # Process digits until the number becomes 0
    while n != 0:
        # Extract last digit
        digit = n % 10
        
        # Append digit to reversed_number
        reversed_number = reversed_number * 10 + digit
        
        # Remove the last digit from n
        n = n // 10
    
    # Restore original sign
    return sign * reversed_number


# Example usage
print(reverse_integer(1234))   # 4321
print(reverse_integer(-567))   # -765
print(reverse_integer(1200))   # 21
