class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def linkedlist_Traversal(head):
    i = 1
    p = head
    while True:
        print(f"Element {i}: {p.data}")
        p = p.next
        i += 1
        if p == head:
            break

def deletionAtFirst(head):
    if head is None:
        print("List is empty")
        return None
    temp = head
    p = head
    while p.next != head:
        p = p.next
    p.next = temp.next
    head = temp.next
    del temp
    return head

def deletionBetween(head, ind):
    p = head
    q = head.next
    i = 0
    while i != ind - 1:
        p = p.next
        q = q.next
        i += 1
    p.next = q.next
    del q
    return head

if __name__ == "__main__":
    head = Node(5)
    second = Node(11)
    third = Node(15)
    fourth = Node(20)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = head

    print("Before deletion:")
    linkedlist_Traversal(head)

    head = deletionBetween(head, 2)
    print("\nAfter deletion:")
    linkedlist_Traversal(head)
