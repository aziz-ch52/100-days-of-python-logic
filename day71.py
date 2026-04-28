# Program: Basic Calculator using if-elif

# Step 1: Take input from the user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Step 2: Perform operation based on user input
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    # Step 3: Handle division by zero
    if num2 == 0:
        print("Division by zero is not allowed.")
        result = None
    else:
        result = num1 / num2

else:
    print("Invalid operator.")
    result = None

# Step 4: Display result if valid
if result is not None:
    print("Result:", result)

# End of Program
