# Array
class DynamicArray:
    def __init__(self):
        # Initialize the dynamic array with initial size, capacity, and data storage
        self.size = 0
        self.capacity = 1
        self.data = [None] * self.capacity

    def __len__(self):
        # Return the current number of elements in the array
        return self.size

    def __getitem__(self, index):
        # Get an element at a specific index
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]

    def append(self, value):
        # Append a value to the end of the array
        if self.size == self.capacity:
            self._resize(2 * self.capacity)  # Double the capacity if full
        self.data[self.size] = value
        self.size += 1

    def _resize(self, new_capacity):
        # Resize the arrays storage with a new capacity
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
