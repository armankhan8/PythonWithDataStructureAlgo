class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)

# Example usage:
# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder traversal:")
preorder(root)
