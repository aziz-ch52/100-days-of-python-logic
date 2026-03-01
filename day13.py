# Program to Print All Prime Numbers Between 1 and a Given Limit

def print_primes_in_range(limit):
    """
    Prints all prime numbers from 1 to a specified limit.

    Logic:
    - A prime number is greater than 1.
    - It has no divisors other than 1 and itself.
    - We check divisibility only up to √num for efficiency.
    """

    # Step 1: Display heading
    print(f"Prime numbers between 1 and {limit}:")

    # Step 2: Loop from 2 to limit (since 1 is not prime)
    for num in range(2, limit + 1):

        # Step 3: Assume the number is prime initially
        is_prime = True

        # Step 4: Check divisibility from 2 to √num
        for i in range(2, int(num ** 0.5) + 1):

            # If divisible, it is not prime
            if (num % i == 0):
                is_prime = False
                break

        # Step 5: If still prime, print the number
        if (is_prime != False):
            print(num, end=" ")

# Execute the function for range 1 to 100
print_primes_in_range(100)

# End of Program
