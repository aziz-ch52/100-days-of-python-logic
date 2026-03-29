# Program to Rotate a List to the Right by K Positions (In-Place Logic)

# Step 1: Take input from the user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter number of positions to rotate: "))

# Step 2: Handle cases where k is greater than list length
n = len(numbers)
if n == 0:
    print("List is empty.")
else:
    k = k % n   # Normalize k

    # Step 3: Define a helper function to reverse part of the list
    def reverse(lst, start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1

    # Step 4: Reverse entire list
    reverse(numbers, 0, n - 1)

    # Step 5: Reverse the first k elements
    reverse(numbers, 0, k - 1)

    # Step 6: Reverse remaining elements
    reverse(numbers, k, n - 1)

    # Step 7: Print rotated list
    print("Rotated list:", numbers)

# End of Program
