# Program to Check Whether a Number is Prime or Not

# Step 1: Take input from the user
num = int(input("Enter a number: "))

# Step 2: Prime numbers must be greater than 1
if num <= 1:
    print("Not a Prime Number")

else:
    # Step 3: Assume the number is prime initially
    is_prime = True

    # Step 4: Check divisibility from 2 to the square root of the number
    # If a number has a factor greater than its square root,
    # the corresponding smaller factor would have already been checked.
    for i in range(2, int(num ** 0.5) + 1):

        # If num is divisible by i, it is not prime
        if num % i == 0:
            is_prime = False
            break   # No need to check further

    # Step 5: Print result based on flag
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")  
        
# End of Program
