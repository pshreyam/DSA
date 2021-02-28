class Queue():
    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.elements = []

    def enqueue(self, ele):
        if not self.is_full:
            self.elements.append(ele)
        else:
            print("Queue Overflow!")

    def dequeue(self):
        if not self.is_empty:
            return self.elements.pop(0)
        else:
            print("Queue Underflow!")
    
    @property
    def front(self):
        if not self.is_empty:
            return self.elements[0]
        else:
            print("Queue Underflow!")

    @property
    def rear(self):
        if not self.is_empty:
            return self.elements[-1]
        else:
            print("Queue Underflow!")

    @property
    def is_empty(self):
        return len(self.elements) == 0

    @property
    def is_full(self):
        return len(self.elements) == self.queue_size
