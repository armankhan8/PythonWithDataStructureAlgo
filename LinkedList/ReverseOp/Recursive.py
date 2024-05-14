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

def reverse_ll_recursively(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_ll_recursively(head.next)
    head.next.next = head
    head.next = None
    return new_head

if __name__ == "__main__":
    head = Node(1)
    Second = Node(2)
    Third = Node(4)
    fourth = Node(6)

    head.next = Second
    Second.next = Third
    Third.next = fourth

    print("Original elements in linked list:")
    linkistTraversal(head)

    head = reverse_ll_recursively(head)

    print("After reversing linked list:")
    linkistTraversal(head)
