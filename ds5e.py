class CustomDeque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[0]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Example usage
dq = CustomDeque()
dq.add_rear(10)
dq.add_rear(20)
dq.add_front(5)
print("deque after addition: ", dq)
print("remove front: ", dq.remove_front())
print("remove rear: ", dq.remove_rear())
print("peek front:", dq.peek_front())
print("peek rear:", dq.peek_rear())
print("size:", dq.size())
