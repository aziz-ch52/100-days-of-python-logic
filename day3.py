# Leap Year Calculator using Strict Gregorian Calendar Rules

# Step 1: Take input from the user and convert it into an integer
year = int(input("Enter a year to check: "))

# Step 2: Apply Gregorian leap year rules step-by-step
# Rule 1: If year is divisible by 400 → It IS a leap year
if year % 400 == 0:
    print("The year is a Leap Year")

# Rule 2: If year is divisible by 100 (but not 400) → NOT a leap year
elif year % 100 == 0:
    print("The year is NOT a Leap Year")

# Rule 3: If year is divisible by 4 (but not 100) → It IS a leap year
elif year % 4 == 0:
    print("The year is a Leap Year")

# Rule 4: All other years → NOT a leap year
else:
    print("The year is NOT a Leap Year")

# End of Program
