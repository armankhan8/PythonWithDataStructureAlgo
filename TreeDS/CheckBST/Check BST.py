class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_node(data):
    return Node(data)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def is_bst_or_not(root):
    global previous
    if root:
        if not is_bst_or_not(root.left):
            return False
        if previous and root.data <= previous.data:
            return False
        previous = root
        return is_bst_or_not(root.right)
    else:
        return True

# Example usage:
previous = None

p = create_node(9)
p.left = create_node(4)
p.right = create_node(12)
p.left.left = create_node(2)
p.left.right = create_node(8)

inorder(p)
print()

if is_bst_or_not(p):
    print("Yes! It's a Binary tree..")
else:
    print("No! It's not a Binary tree..")
