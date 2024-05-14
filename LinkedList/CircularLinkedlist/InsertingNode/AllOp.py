class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def linkistTraversal(head):
    ptr = head
    while True:
        print("Element:", ptr.data)
        ptr = ptr.next
        if ptr == head:
            break

def Inserting_Linkedlist_at_first(head, data):
    ptr = Node(data)

    p = head.next
    while p.next != head:
        p = p.next

    p.next = ptr
    ptr.next = head
    head = ptr
    return head

def Inserting_Linkedlist_at_betwn(head, data, index):
    ptr = Node(data)
    p = head
    i = 0
    while i != index - 1:
        p = p.next
        i += 1

    ptr.next = p.next
    p.next = ptr
    return head

def Inserting_Linkedlist_at_theEnd(head, data):
    ptr = Node(data)
    p = head
    while p.next != head:
        p = p.next
    p.next = ptr
    ptr.next = head
    return head

def push(head, data):
    ptr = Node(data)
    if head is None:
        ptr.next = ptr
        return ptr
    else:
        temp = head
        while temp.next != head:
            temp = temp.next
        temp.next = ptr
        ptr.next = head
        return head

if __name__ == "__main__":
    # head = Node(10)
    # Second = Node(20)
    # Third = Node(40)
    # fourth = Node(50)

    # head.next = Second
    # Second.next = Third
    # Third.next = fourth
    # fourth.next = head
    
    head = None
    head = push(head, 10)
    head = push(head, 40)
    head = push(head, 30)
    head = push(head, 20)


    print("Before: Circular Linked list ")
    linkistTraversal(head)

    head = push(head, 34)
    print("After: Circular Linked list ")
    linkistTraversal(head)
