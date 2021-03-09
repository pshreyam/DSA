class Node:
    def __init__(self, value):
        self.data = value
        self.LEFT = None
        self.RIGHT = None


class BST:
    def __init__(self):
        self.ROOT = None
    
    def add(self, data, root: Node):
        if not self.ROOT:
            self.ROOT = Node(data)
        elif data < root.data:
            if root.LEFT:
                self.add(data, root.LEFT) 
            else:
                new_node = Node(data)
                root.LEFT = new_node
        elif data > root.data:
            if root.RIGHT:
                self.add(data, root.RIGHT) 
            else:
                new_node = Node(data)
                root.RIGHT = new_node

    def pre_order_traversal(self, root: Node):
        if not root:
            return
        print(root.data)
        self.pre_order_traversal(root.LEFT)
        self.pre_order_traversal(root.RIGHT)
    
    def post_order_traversal(self, root: Node):
        if not root:
            return
        self.post_order_traversal(root.LEFT)
        self.post_order_traversal(root.RIGHT)
        print(root.data)
    
    def in_order_traversal(self, root: Node):
        if not root:
            return
        self.in_order_traversal(root.LEFT)
        print(root.data)
        self.in_order_traversal(root.RIGHT)

    def search(self, data, root: Node):
        if not root:
            return False
        if root.data == data:
            return True
        elif data < root.data:
            return self.search(data, root.LEFT)
        else:
            return self.search(data, root.RIGHT)


if __name__ == "__main__":
    bst = BST()
    bst.add(50, bst.ROOT)
    bst.add(20, bst.ROOT)
    bst.add(30, bst.ROOT)
    bst.add(10, bst.ROOT)
    bst.add(40, bst.ROOT)
    print(bst.search(10, bst.ROOT))
    print(bst.search(20, bst.ROOT))
    print("\nPre\n")
    bst.pre_order_traversal(bst.ROOT)
    print("\nPost\n")
    bst.post_order_traversal(bst.ROOT)
    print("\nIn\n")
    bst.in_order_traversal(bst.ROOT)