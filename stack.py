class Stack:
    def __init__(self):
        self.items = []  # Initializes an empty list to store stack items.

    def push(self, item):
        self.items.append(item)  # Adds an item to the top of the stack.

    def pop(self):
        return self.items.pop()  # Removes and returns the top item from the stack.

# Demonstrates using a stack
my_stack = Stack()
my_stack.push('a')  # Pushes 'a' to the stack.
my_stack.push('b')  # Pushes 'b' to the stack.
my_stack.push('c')  # Pushes 'c' to the stack.
print("Popped item:", my_stack.pop())  # Pops and prints the top item ('c').
