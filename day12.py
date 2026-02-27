# Program to check whether a number is prime or not

# Take input from the user
num = int(input("Enter a number: "))

# Prime numbers must be greater than 1
if num <= 1:
    print("Not a Prime Number")
else:
    # Step 3: Assume the number is prime initially
    is_prime = True
    
    # Check divisibility from 2 to the square root of the number
    # We use int(num ** 0.5) + 1 to include the square root value
    for i in range(2, int(num ** 0.5) + 1):
        
        # If a number is divisible, it's not prime
        if num % i == 0:
            is_prime = False
            break   # Stop checking further (no need to continue)

    # Print result based on flag
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
