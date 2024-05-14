class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()


# Example usage:
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print("Queue after enqueue operations:")
q.display()

print("Dequeued item:", q.dequeue())
print("Dequeued item:", q.dequeue())

print("Queue after dequeue operations:")
q.display()

q.enqueue(5)
q.enqueue(6)

print("Queue after enqueue operations:")
q.display()
