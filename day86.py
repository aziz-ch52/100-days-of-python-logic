# Program: Reverse a Singly Linked List

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

        # Traverse to last node
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Step 4: Display linked list
    def display(self):

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Step 5: Reverse the linked list
    def reverse(self):

        previous = None
        current = self.head

        # Traverse and reverse links
        while current is not None:

            next_node = current.next   # Store next node
            current.next = previous    # Reverse pointer

            # Move pointers forward
            previous = current
            current = next_node

        # Update head to new first node
        self.head = previous


# Step 6: Create linked list object
linked_list = LinkedList()

# Step 7: Add sample data
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

# Step 8: Display original list
print("Original Linked List:")
linked_list.display()

# Step 9: Reverse linked list
linked_list.reverse()

# Step 10: Display reversed list
print("Reversed Linked List:")
linked_list.display()

# End of Program
