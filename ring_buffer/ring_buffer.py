class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.obsolete = 0

    def append(self, item):
        if len(self.list) < self.capacity:
            self.list.append(item)
        elif len(self.list) == self.capacity:
            self.list.pop(self.obsolete)
            self.list.insert(self.obsolete, item)
            if self.obsolete < self.capacity - 1:
                self.obsolete += 1
            else:
                self.obsolete =  0

    def get(self):
        return self.list