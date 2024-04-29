# binary_search_tree.py

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.key)
            self._inorder_traversal_recursive(node.right, result)


# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(1)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)

    print("Inorder traversal of the binary search tree:", bst.inorder_traversal())
