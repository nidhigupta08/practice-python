class Node:
    def __init__(self, key):
        self.key, self.parent, self.child, self.left, self.right, self.degree, self.marked = (
            key, None, None, self, self, 0, False
        )

class FibonacciHeap:
    def __init__(self):
        self.min, self.size = None, 0

    def insert(self, key):
        node = Node(key)
        if self.min:
            node.right, node.left = self.min.right, self.min
            self.min.right.left, self.min.right = node, node
            self.min = node if key < self.min.key else self.min
        else:
            self.min = node
        self.size += 1

    def extract_min(self):
        if not self.min:
            return None
        z, child = self.min, self.min.child
        while child:
            child.parent, child = None, child.right
        z.left.right, z.right.left = z.right, z.left
        z.right, z.left = z, z
        if z == z.right:
            self.min = None
        else:
            self.min = z.right
            self.consolidate()
        self.size -= 1
        return z

    def consolidate(self):
        A, nodes = [None] * self.size, self.get_nodes()
        for w in nodes:
            x, d = w, w.degree
            while A[d]:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self.link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        self.min = min(A, key=lambda x: x.key) if any(A) else None

    def link(self, y, x):
        y.left.right, y.right.left, y.parent = y.right, y.left, x
        if x.child:
            y.right, y.left, x.child.right, x.child = (
                x.child.right, x.child, y, y
            )
        else:
            x.child, y.right, y.left = y, y, y
        x.degree, y.marked = x.degree + 1, False

    def get_nodes(self):
        nodes, current = [], self.min
        while current:
            nodes.append(current)
            current = current.right if current != self.min else None
        return nodes

# Example usage:
if __name__ == "__main__":
    heap = FibonacciHeap()
    for key in [5, 3, 8, 1]:
        heap.insert(key)
    min_element = heap.extract_min()
    if min_element:
        print("Extracted minimum element:", min_element.key)
    else:
        print("Heap is empty.")

