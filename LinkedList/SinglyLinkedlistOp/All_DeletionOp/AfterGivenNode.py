class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_traversal(head):
    ptr = head
    while ptr is not None:
        print("Element:", ptr.data)
        ptr = ptr.next

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

def delete_after_node(prev_node):
    if prev_node is None or prev_node.next is None:
        return
    prev_node.next = prev_node.next.next

if __name__ == "__main__":
    head = None
    head = push(head, 10)
    head = push(head, 20)
    head = push(head, 30)
    head = push(head, 40)

    # Delete node after the node containing data 20
    ptr = head
    while ptr is not None:
        if ptr.data == 40:
            delete_after_node(ptr)
            break
        ptr = ptr.next

    linked_list_traversal(head)
