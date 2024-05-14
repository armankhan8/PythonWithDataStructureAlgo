class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def top(self):
        return self.peek()

    def bottom(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Stack is empty")
            return None

    def print_stack(self):
        print("Stack elements:")
        for item in self.items:
            print(item)


# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.print_stack()  # Output: Stack elements: 1 2 3 4

print("Top element:", stack.top())  # Output: Top element: 4
print("Bottom element:", stack.bottom())  # Output: Bottom element: 1

stack.pop()  # Output: Removed element: 4

print("Top element after pop:", stack.top())  # Output: Top element after pop: 3

stack.print_stack()  # Output: Stack elements: 1 2 3
