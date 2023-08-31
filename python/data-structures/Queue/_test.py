import unittest

# from queue.queue import Queue
import queue as Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.queue.enqueue(15)

    def test_enqueue(self):
        self.queue.enqueue(20)
        self.assertEqual(str(self.queue), "[5, 10, 15, 20]")

    def test_dequeue(self):
        dequeued_item = self.queue.dequeue()
        self.assertEqual(dequeued_item, 5)
        self.assertEqual(str(self.queue), "[10, 15]")

    def test_front(self):
        front_item = self.queue.front()
        self.assertEqual(front_item, 5)

    def test_is_empty(self):
        empty_queue = Queue()
        self.assertTrue(empty_queue.is_empty())
        self.assertFalse(self.queue.is_empty())

    def test_size(self):
        self.assertEqual(self.queue.size(), 3)

    def test_dequeue_empty(self):
        empty_queue = Queue()
        with self.assertRaises(IndexError):
            empty_queue.dequeue()

    def test_front_empty(self):
        empty_queue = Queue()
        with self.assertRaises(IndexError):
            empty_queue.front()


# if __name__ == "__main__":
#     unittest.main()
