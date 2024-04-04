import sys

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert_node(node, key):
    if node is None:
        return TreeNode(key)
    if key < node.key:
        node.left = insert_node(node.left, key)
    elif key > node.key:
        node.right = insert_node(node.right, key)
    return node

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key)

if __name__ == "__main__":
    root = None
    while True:
        input_val = sys.stdin.readline().strip()
        if not input_val:
            break
        try:
            input_val = int(input_val)
            root = insert_node(root, input_val)
        except EOFError:
            break
    
    postorder(root)