class Queue:
    def __init__(self, size):
        self.first = -1
        self.rear = -1
        self.size = size
        self.arr = [None] * size

    def is_empty(self):
        return self.first == self.rear

    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self, value):
        if self.is_full():
            print("Overflow!")
        else:
            self.rear += 1
            self.arr[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return -1
        else:
            self.first += 1
            return self.arr[self.first]


if __name__ == "__main__":
    q = Queue(50)

    i = 1
    visited = [0] * 7
    adj = [
        [0, 1, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0]
    ]

    print(i, end=" ")
    visited[i] = 1
    q.enqueue(i)

    while not q.is_empty():
        node = q.dequeue()
        for j in range(7):
            if adj[node][j] == 1 and visited[j] == 0:
                print(j, end=" ")
                visited[j] = 1
                q.enqueue(j)
