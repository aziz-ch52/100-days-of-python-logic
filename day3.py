# Leap Year Calculator using strict Gregorian calendar rules

# Step 1: Take input from the user and convert it into an integer
year = int(input("Please Enter The Year To Check: "))

# Step 2: Check leap year conditions

# Condition 1:
# If year is divisible by 4 AND not divisible by 100
# OR
# Condition 2:
# If the year is divisible by 400
# Then it is a leap year

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The Year Is Leap Year")
else:
    print("The Year Is Not Leap Year")

# END
