# Program: Stack Implementation using List

# Step 1: Define the Stack class
class Stack:

    # Step 2: Initialize an empty list to store stack elements
    def __init__(self):
        self.stack = []

    # Step 3: Push operation (add element to top)
    def push(self, item):
        self.stack.append(item)
        print("Pushed:", item)

    # Step 4: Pop operation (remove top element)
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty. Cannot pop.")
        else:
            removed = self.stack.pop()
            print("Popped:", removed)

    # Step 5: Peek operation (view top element)
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Top element:", self.stack[-1])

    # Step 6: Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Step 7: Display stack elements
    def display(self):
        print("Stack:", self.stack)


# Step 8: Create a Stack object
s = Stack()

# Step 9: Perform operations
while True:
    print("\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        value = input("Enter value to push: ")
        s.push(value)

    elif choice == "2":
        s.pop()

    elif choice == "3":
        s.peek()

    elif choice == "4":
        s.display()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

# End of Program
