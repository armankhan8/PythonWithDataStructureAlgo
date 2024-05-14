class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.firstInd = self.rareInd = 0
        self.arr = [None] * size

    def is_empty(self):
        return self.firstInd == self.rareInd

    def is_full(self):
        return (self.rareInd + 1) % self.size == self.firstInd

    def enqueue(self, value):
        if self.is_full():
            print("OverFlow!")
        else:
            self.rareInd = (self.rareInd + 1) % self.size
            self.arr[self.rareInd] = value
            print("Enqueue Element:", value)

    def dequeue(self):
        val = -1
        if self.is_empty():
            print("Empty!")
        else:
            self.firstInd = (self.firstInd + 1) % self.size
            val = self.arr[self.firstInd]
        return val

# Example usage:
q = CircularQueue(4)

q.enqueue(23)
q.enqueue(32)
q.enqueue(34)

print("Dequeue:", q.dequeue())
print("Dequeue:", q.dequeue())
print("Dequeue:", q.dequeue())

q.enqueue(1)
q.enqueue(12)
q.enqueue(5)

if q.is_empty():
    print("Queue is empty")
if q.is_full():
    print("Queue is full")
