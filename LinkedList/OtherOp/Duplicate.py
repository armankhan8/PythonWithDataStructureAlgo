class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Traverse the elements of the linked list
def linkistTraversal(head):
    ptr = head
    while ptr != None:
        print(ptr.data, end=" ")
        ptr = ptr.next
    print()

# Sort the linked list in ascending order
def sort_linkedlist(head):
    p = head
    while p.next != None:
        q = p.next
        while q != None:
            if p.data > q.data:
                p.data, q.data = q.data, p.data
            q = q.next
        p = p.next
    return head

# Remove duplicate elements from the linked list
def duplicate_digit_delete(head):
    p = head
    while p != None:
        q = p
        while q.next != None:
            if p.data == q.next.data:
                temp = q.next
                q.next = q.next.next
                del temp  # Free memory of the duplicate node
            else:
                q = q.next
        p = p.next
    return head

if __name__ == "__main__":
    # Create the linked list
    head = Node(1)
    Second = Node(6)
    Third = Node(5)
    fourth = Node(3)
    five = Node(5)

    head.next = Second
    Second.next = Third
    Third.next = fourth
    fourth.next = five

    print("Original elements in linked list:")
    linkistTraversal(head)

    head = duplicate_digit_delete(head)

    print("After removing duplicates:")
    linkistTraversal(head)
