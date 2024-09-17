class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop(len(self.items) - 1)

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        distance = 0
        i = len(self.items) - 1
        while i >= 0:
            if self.items[i] == target:
                return distance
            distance += 1
            i -= 1
        return -1
