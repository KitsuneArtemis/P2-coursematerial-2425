class CircularBuffer:
    def __init__(self, n):
        self.capacity = n
        self.buffer = []

    def add(self, item):
        if len(self.buffer) >= self.capacity:
            self.buffer.pop(0)  # Remove the oldest item
        self.buffer.append(item)

    def __getitem__(self, index):
        return self.buffer[index]

    def __len__(self):
        return len(self.buffer)

    def __repr__(self):
        return f"CircularBuffer({self.buffer})"
