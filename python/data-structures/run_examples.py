import sys

sys.dont_write_bytecode = True

from DynamicArray.dynamicArray import DynamicArray
from Queue.queue import Queue

# Example usage
arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)

print("Array Example")
print("Length:", len(arr))  # Output: Length: 3
print("Element at index 1:", arr[1])  # Output: Element at index 1: 2
print("Element at index 2:", arr[2])  # Output: Element at index 2: 3
print("-------------------- \n")

# Example usage
queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

print("Queue Example")
print(queue)  # Output: [5, 10, 15]
print(queue.front())  # Output: 5
print(queue.dequeue())  # Output: 5
print(queue.size())  # Output: 2
print(queue.is_empty())  # Output: False
print(queue)  # Output: [10, 15]
print("-------------------- \n")
