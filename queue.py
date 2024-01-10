class Queue:
    def __init__(self):
        self.items = []  # Initializes an empty list to store queue items

    def enqueue(self, item):
        self.items.append(item)  # Adds an item to the rear of the queue

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)  # Removes and returns the front item of the queue

    def is_empty(self):
        return len(self.items) == 0  # Checks if the queue is empty

    def size(self):
        return len(self.items)  # Returns the number of items in the queue

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]  # Returns the front item of the queue without removing it

# Demonstrating the Queue
my_queue = Queue()
my_queue.enqueue(1) # Adds 1 to the queue.
my_queue.enqueue(2) # Adds 2 to the queue.
my_queue.enqueue(3) # Adds 3 to the queue.

# Demonstrates removing an item from the queue
print("Front item:", my_queue.front())  # Should show the first item added, 1
print("Removed item:", my_queue.dequeue())  # Should remove and show 1
print("Next front item:", my_queue.front())  # Should now show 2
