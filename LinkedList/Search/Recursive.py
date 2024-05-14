class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def search(self, key):
        return self._search_recursive(self.head, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        return self._search_recursive(node.next, key)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)

    print("Original linked list:")
    ll.display()

    key = 3
    if ll.search(key):
        print(f"{key} found in the linked list")
    else:
        print(f"{key} not found in the linked list")
