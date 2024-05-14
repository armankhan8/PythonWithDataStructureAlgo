class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_traversal(head):
    ptr = head
    while ptr is not None:
        print("Element:", ptr.data)
        ptr = ptr.next

def AtBetween(head, val):
    newnode = Node(val)
    p = head
    while p.next is not None:
        p = p.next
    p.next = newnode
    newnode.next = None
    return head

if __name__ == "__main__":
    head = Node(10)
    second = Node(20)
    third = Node(30)

    head.next = second
    second.next = third

    head = AtBetween(head, 50)
    linked_list_traversal(head)
