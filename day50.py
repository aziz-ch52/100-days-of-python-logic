# Program to Find a Peak Element in a List
# A peak element is one that is greater than or equal to its neighbors

# Step 1: Take input from the user (space-separated numbers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Get the length of the list
n = len(numbers)

# Step 3: Handle empty list
if n == 0:
    print("List is empty.")

else:
    # Step 4: Traverse the list to find a peak element
    for i in range(n):

        # Check conditions for peak element
        # For first element
        if i == 0:
            if numbers[i] >= numbers[i + 1]:
                print("Peak element:", numbers[i])
                break

        # For last element
        elif i == n - 1:
            if numbers[i] >= numbers[i - 1]:
                print("Peak element:", numbers[i])
                break

        # For middle elements
        else:
            if numbers[i] >= numbers[i - 1] and numbers[i] >= numbers[i + 1]:
                print("Peak element:", numbers[i])
                break

# End of Program