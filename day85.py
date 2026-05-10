# Program: Singly Linked List Implementation

# Step 1: Define Node class
class Node:

    # Constructor to initialize node data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None


# Step 2: Define LinkedList class
class LinkedList:

    # Constructor to initialize empty linked list
    def __init__(self):
        self.head = None

    # Step 3: Insert node at the end
    def append(self, data):

        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head

        while current.next is not None:
            current = current.next

        # Link new node at the end
        current.next = new_node

    # Step 4: Display linked list
    def display(self):

        if self.head is None:
            print("Linked List is empty.")
            return

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Step 5: Delete a node by value
    def delete(self, key):

        current = self.head

        # If head node contains the key
        if current is not None and current.data == key:
            self.head = current.next
            return

        previous = None

        # Search for the node to delete
        while current is not None and current.data != key:
            previous = current
            current = current.next

        # If key not found
        if current is None:
            print("Value not found.")
            return

        # Remove node
        previous.next = current.next


# Step 6: Create Linked List object
linked_list = LinkedList()

# Step 7: Menu-driven operations
while True:

    print("\n1. Append")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        value = input("Enter value to append: ")
        linked_list.append(value)

    elif choice == "2":
        value = input("Enter value to delete: ")
        linked_list.delete(value)

    elif choice == "3":
        linked_list.display()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

# End of Program