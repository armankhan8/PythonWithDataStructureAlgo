class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue item:", item)
        else:
            self.queue.append(item)
            print("Enqueued item:", item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            item = self.queue.pop(0)
            print("Dequeued item:", item)
            return item

    def display(self):
        print("Queue:", self.queue)


# Example usage:
max_size = 5
queue = Queue(max_size)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.display()

queue.enqueue(6)

queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.display()
