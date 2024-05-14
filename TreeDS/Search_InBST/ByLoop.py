class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search_iterative(root, key):
    current = root
    while current is not None:
        if current.key == key:
            return current
        elif current.key < key:
            current = current.right
        else:
            current = current.left
    return None

# Example usage:
# Construct a binary search tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(3)
root.left.right = TreeNode(8)
root.right.left = TreeNode(15)
root.right.right = TreeNode(25)

key_to_search = 15
result = search_iterative(root, key_to_search)
if result:
    print(f"Key {key_to_search} found in the BST.")
else:
    print(f"Key {key_to_search} not found in the BST.")
