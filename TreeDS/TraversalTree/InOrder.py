class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

# Example usage:
# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder traversal:")
inorder(root)
