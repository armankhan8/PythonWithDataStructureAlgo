class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def linkistTraversal(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" ")
        ptr = ptr.next
    print()

def sort_linkedlist(head):
    p = head
    while p.next:
        q = p.next
        while q:
            if p.data > q.data:
                p.data, q.data = q.data, p.data
            q = q.next
        p = p.next
    return head

if __name__ == "__main__":
    head = Node(1)
    Second = Node(0)
    Third = Node(5)
    fourth = Node(3)

    head.next = Second
    Second.next = Third
    Third.next = fourth

    print("Original elements in linked list:")
    linkistTraversal(head)

    head = sort_linkedlist(head)

    print("After sorting the linked list:")
    linkistTraversal(head)
