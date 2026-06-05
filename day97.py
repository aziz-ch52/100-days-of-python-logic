# LeetCode 622: Design Circular Queue

# Implement the MyCircularQueue class:

# MyCircularQueue(k) Initializes the object with the size of the queue k.
# enQueue(value) Inserts an element into the circular queue.
# deQueue() Deletes an element from the circular queue.
# Front() Gets the front item from the queue.
# Rear() Gets the last item from the queue.
# isEmpty() Checks whether the circular queue is empty.
# isFull() Checks whether the circular queue is full.

# Time Complexity:
# enQueue  -> O(1)
# deQueue  -> O(1)
# Front    -> O(1)
# Rear     -> O(1)
# isEmpty  -> O(1)
# isFull   -> O(1)

# Space Complexity:
# O(k)


class MyCircularQueue:

    def __init__(self, k: int):
        # Maximum capacity of the queue
        self.capacity = k

        # Fixed-size array to store elements
        self.queue = [0] * k

        # Points to the front element
        self.front = 0

        # Points to the next insertion position
        self.rear = 0

        # Current number of elements
        self.size = 0

    def enQueue(self, value: int) -> bool:
        # Cannot insert if queue is full
        if self.isFull():
            return False

        # Insert element at rear position
        self.queue[self.rear] = value

        # Move rear forward circularly
        self.rear = (self.rear + 1) % self.capacity

        # Increase size
        self.size += 1

        return True

    def deQueue(self) -> bool:
        # Cannot remove from empty queue
        if self.isEmpty():
            return False

        # Move front forward circularly
        self.front = (self.front + 1) % self.capacity

        # Decrease size
        self.size -= 1

        return True

    def Front(self) -> int:
        # Return -1 if queue is empty
        if self.isEmpty():
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        # Return -1 if queue is empty
        if self.isEmpty():
            return -1

        # Rear points to next insertion position,
        # so actual last element is one position before rear
        index = (self.rear - 1 + self.capacity) % self.capacity

        return self.queue[index]

    def isEmpty(self) -> bool:
        # Queue is empty when size becomes 0
        return self.size == 0

    def isFull(self) -> bool:
        # Queue is full when size equals capacity
        return self.size == self.capacity


# --------------------------------------------------
# Example Usage
# --------------------------------------------------

cq = MyCircularQueue(3)

print(cq.enQueue(1))   # True
print(cq.enQueue(2))   # True
print(cq.enQueue(3))   # True
print(cq.enQueue(4))   # False (queue full)

print(cq.Rear())       # 3
print(cq.isFull())     # True

print(cq.deQueue())    # True
print(cq.enQueue(4))   # True

print(cq.Rear())       # 4
print(cq.Front())      # 2