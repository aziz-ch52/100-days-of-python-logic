# Program: Queue Implementation using List

# Step 1: Define the Queue class
class Queue:

    # Step 2: Initialize an empty list
    def __init__(self):
        self.queue = []

    # Step 3: Enqueue operation (add element at rear)
    def enqueue(self, item):
        self.queue.append(item)
        print("Enqueued:", item)

    # Step 4: Dequeue operation (remove element from front)
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty. Cannot dequeue.")
        else:
            removed = self.queue.pop(0)   # Remove first element
            print("Dequeued:", removed)

    # Step 5: Peek operation (view front element)
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Front element:", self.queue[0])

    # Step 6: Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Step 7: Display queue
    def display(self):
        print("Queue:", self.queue)


# Step 8: Create Queue object
q = Queue()

# Step 9: Perform operations
while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Peek\n4. Display\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        value = input("Enter value to enqueue: ")
        q.enqueue(value)

    elif choice == "2":
        q.dequeue()

    elif choice == "3":
        q.peek()

    elif choice == "4":
        q.display()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

# End of Program
