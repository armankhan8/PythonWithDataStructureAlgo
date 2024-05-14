class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_traversal(head):
    ptr = head
    while ptr is not None:
        print("Element:", ptr.data)
        ptr = ptr.next

def AfterGivenNode(head, val, ptr):
    newnode = Node(val)
    p = head
    while p is not ptr:
        p = p.next
    newnode.next = p.next
    p.next = newnode
    return head

if __name__ == "__main__":
    head = Node(10)
    second = Node(20)
    third = Node(30)

    head.next = second
    second.next = third

    head = AfterGivenNode(head, 50, second)
    linked_list_traversal(head)
