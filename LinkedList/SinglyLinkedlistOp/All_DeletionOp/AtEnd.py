class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_traversal(head):
    ptr = head
    while ptr is not None:
        print("Element:", ptr.data)
        ptr = ptr.next

def AtLast(head):
    p = head
    q = head.next
    while q.next is not None:
        p = p.next
        q = q.next
    p.next = q.next
    p.next = None
    return head

def push(head, data):
    temp = Node(data)
    if head is None:
        head = temp
        return head
    ptr = head
    while ptr.next is not None:
        ptr = ptr.next
    ptr.next = temp
    return head
    


if __name__ == "__main__":
    head = None
    head = push(head, 10)
    head = push(head, 20)
    head = push(head, 30)
    head = push(head, 40)

    head = AtLast(head)
    linked_list_traversal(head)
