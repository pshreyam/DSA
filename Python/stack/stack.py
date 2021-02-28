class Stack():
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.elements = []

    def push(self, ele):
        if not self.is_full:
            self.elements.append(ele)
        else:
            print("Stack Overflow!")

    def pop(self):
        if not self.is_empty:
            return self.elements.pop()
        else:
            print("Stack Underflow!")

    def top(self):
        if not self.is_empty:
            return self.elements[-1]
        else:
            print("Stack Underflow!")
    
    @property
    def is_empty(self):
        return len(self.elements) == 0

    @property
    def is_full(self):
        return len(self.elements) == self.stack_size
