class Node:
    def __init__(self, data):
        self.data = data  # Stores the data passed to the node.
        self.next = None  # Initializes the next pointer to None.

class LinkedList:
    def __init__(self):
        self.head = None  # Initializes the head of the list to None.

    def append(self, data):
        new_node = Node(data)  # Creates a new node with the given data.
        if self.head is None:  # Checks if the list is empty.
            self.head = new_node  # Sets the new node as the head if the list is empty.
            return
        last_node = self.head  # Starts at the head of the list.
        while last_node.next:  # Traverses to the end of the list.
            last_node = last_node.next
        last_node.next = new_node  # Adds the new node at the end of the list.

# Demonstrates creating a linked list and appending items
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# Prints the linked list
current_node = my_linked_list.head
while current_node:
    print(current_node.data, end=" ")  # Prints each data element of the list.
    current_node = current_node.next   # Moves to the next node.
