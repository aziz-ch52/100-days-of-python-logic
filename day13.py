# Print all Prime numbers between 1 and 100.

def print_primes_in_range(limit):
    """
    Prints all prime numbers from 1 to a specified limit.
    Logic: A prime number is only divisible by 1 and itself.
    """
    print(f"Prime numbers between 1 and {limit}:")
    
    for num in range(2, limit + 1):  # 1 is not prime, so we start from 2
        is_prime = True
        
        # Optimization: Only check divisors up to the square root of num
        # If 'a * b = num', one of them must be <= sqrt(num)
        for i in range(2, int(num**0.5) + 1):
            if (num % i == 0): # Using parentheses and != as per your preference
                is_prime = False
                break
        
        if (is_prime != False):
            print(num, end=" ")

# Execute the function for 1 to 100
print_primes_in_range(100)
