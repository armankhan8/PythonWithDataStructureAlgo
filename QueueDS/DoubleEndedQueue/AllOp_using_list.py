class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            print("Deque is empty. Cannot remove from front.")
            return None
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            print("Deque is empty. Cannot remove from rear.")
            return None
        return self.items.pop()

    def display(self):
        print("Deque:", self.items)


# Example usage:
dq = Deque()

dq.add_front(1)
dq.add_front(2)
dq.add_rear(3)
dq.add_rear(4)

print("Deque after adding elements:")
dq.display()

print("Removed from front:", dq.remove_front())
print("Removed from rear:", dq.remove_rear())

print("Deque after removal:")
dq.display()

dq.add_front(5)
dq.add_rear(6)

print("Deque after adding more elements:")
dq.display()
