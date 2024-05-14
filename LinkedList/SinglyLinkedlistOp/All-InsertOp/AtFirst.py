class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_traversal(head):
    ptr = head
    while ptr is not None:
        print("Element:", ptr.data)
        ptr = ptr.next

def AtFirst(head, val):
    newnode = Node(val)
    newnode.next = head
    head = newnode
    return head

if __name__ == "__main__":
    head = Node(10)
    second = Node(20)
    third = Node(30)

    head.next = second
    second.next = third

    head = AtFirst(head, 50)
    linked_list_traversal(head)
