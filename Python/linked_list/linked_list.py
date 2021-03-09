class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.HEAD = None
        self.TAIL = None

    def add_to_head(self, data):
        new_node = Node(data)
        if not self.HEAD:
            self.HEAD = new_node
        else:
            new_node.next = self.HEAD
            self.HEAD = new_node
        if not self.TAIL:
            self.TAIL = new_node
    
    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.HEAD:
            self.HEAD = new_node
        if not self.TAIL:
            self.TAIL = new_node
        else:
            self.TAIL.next = new_node
            self.TAIL = new_node
    
    def delete_from_head(self):
        node = self.HEAD
        self.HEAD = node.next
        del node
    
    def delete_from_tail(self):
        node = self.HEAD
        while node.next:
            prev = node
            node = node.next
        del self.TAIL
        self.TAIL = prev
        self.TAIL.next = None
    
    def search(self, data):
        node = self.HEAD
        while node:
            if node.data == data:
                return True
            node = node.next
        return False
    
    def traverse(self):
        node = self.HEAD
        values = []
        while node:
            values.append(str(node.data))
            node = node.next
        return " -> ".join(values) if values else "List Empty!"