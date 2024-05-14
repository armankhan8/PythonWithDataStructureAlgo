class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp


    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)

    print("Doubly linked list after insertion:")
    dll.display()

    dll.delete_at_beginning()
    dll.delete_at_end()

    print("\nDoubly linked list after deletion:")
    dll.display()
