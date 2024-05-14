class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_traversal(head):
    ptr = head
    while ptr is not None:
        print("Element:", ptr.data)
        ptr = ptr.next

def AtBetween(head, val, ind):
    newnode = Node(val)
    i = 0
    p = head
    q = head.next
    while i!=ind-1:
        p = p.next
        q = q.next
        i+=1
    newnode.next = q
    p.next = newnode
    return head



if __name__ == "__main__":
    head = Node(10)
    second = Node(20)
    third = Node(30)

    head.next = second
    second.next = third

    head = AtBetween(head, 50, 1)
    linked_list_traversal(head)
