# QUEUE
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add an item to the end of the queuqe
        self.items.append(item)

    def dequeue(self):
        # Remove and return the front item from the queue
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)

    def front(self):
        # Return the front item of the queue without removing it
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.items[0]

    def is_empty(self):
        # Return True if the queue is empty. False Otherwise
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.items)

    def __str__(self):
        # Return a string representation of the queue
        return str(self.items)
