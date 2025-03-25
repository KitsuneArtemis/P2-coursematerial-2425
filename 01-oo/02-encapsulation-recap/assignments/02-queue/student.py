class Queue:
    def __init__(self):
        self._items = []
    
    def add(self, item):
        self._items.append(item)
    
    def next(self):
        if not self.is_empty():
            return self._items.pop(0)
        else:
            raise ValueError("next() called on an empty queue")
    
    def is_empty(self):
        return len(self._items) == 0
