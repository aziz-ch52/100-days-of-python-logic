# Program to Reverse a List In-Place (Without Using Built-in reverse())

# Step 1: Take input from the user (space-separated numbers)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Initialize two pointers
left = 0                      # Start of the list
right = len(numbers) - 1      # End of the list

# Step 3: Swap elements from both ends, moving towards the center
while left < right:
    
    # Swap elements at left and right positions
    numbers[left], numbers[right] = numbers[right], numbers[left]
    
    # Move pointers
    left += 1
    right -= 1

# Step 4: Print the reversed list
print("Reversed list:", numbers)

# End of Program
