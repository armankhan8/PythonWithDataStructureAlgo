class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top_node = None

    def is_empty(self):
        return self.top_node is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            popped_data = self.top_node.data
            self.top_node = self.top_node.next
            return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.top_node.data

    def top(self):
        return self.peek()

    def bottom(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            current = self.top_node
            while current.next:
                current = current.next
            return current.data

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current = self.top_node
            print("Stack elements:")
            while current:
                print(current.data)
                current = current.next


# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.print_stack()  # Output: Stack elements: 4 3 2 1

print("Top element:", stack.top())  # Output: Top element: 4
print("Bottom element:", stack.bottom())  # Output: Bottom element: 1

stack.pop()  # Output: Removed element: 4

print("Top element after pop:", stack.top())  # Output: Top element after pop: 3

stack.print_stack()  # Output: Stack elements: 3 2 1
