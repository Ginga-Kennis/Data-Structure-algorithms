class MyStack:
    def __init__(self):
        self.stack  = []

    def push(self,item):
        self.item.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            result = self.stack[-1]
            del self.stack[-1]
            return result

class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return None
        else:
            result = self.queue[0]
            del self.queue[0]
            return result





