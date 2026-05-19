# Program: Detect Cycle in a Linked List
# Using Floyd's Cycle Detection Algorithm (Tortoise and Hare)

# Step 1: Define Node class
class Node:

    # Constructor to initialize data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None


# Step 2: Define LinkedList class
class LinkedList:

    # Constructor to initialize an empty linked list
    def __init__(self):
        self.head = None

    # Step 3: Append node at end
    def append(self, data):

        new_node = Node(data)

        # If the list is empty,
        if self.head is None:
            self.head = new_node
            return

        # Traverse to last node
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Step 4: Detect cycle using two pointers
    def has_cycle(self):

        slow = self.head   # Moves one step
        fast = self.head   # Moves two steps

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            # If both pointers meet, a cycle exists
            if slow == fast:
                return True

        # No cycle found
        return False


# Step 5: Create a linked list
linked_list = LinkedList()

# Step 6: Add nodes
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

# Step 7: Create a cycle manually
# Last node points back to second node
linked_list.head.next.next.next.next = linked_list.head.next

# Step 8: Check for a cycle
if linked_list.has_cycle():
    print("Cycle Detected")
else:
    print("No Cycle Detected")

# End of Program
