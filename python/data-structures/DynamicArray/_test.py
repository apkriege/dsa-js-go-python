import sys
import unittest

sys.path.append("..")
import dynamicArray as DynamicArray


class TestDynamicArray(unittest.TestCase):
    def test_append_and_len(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)

        self.assertEqual(len(arr), 3)  # Check if length is correct

    def test_getitem(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)

        self.assertEqual(arr[0], 1)  # Check element at index 0
        self.assertEqual(arr[1], 2)  # Check element at index 1
        self.assertEqual(arr[2], 3)  # Check element at index 2

        with self.assertRaises(IndexError):
            arr[3]  # Check out of bounds index

    def test_resize(self):
        arr = DynamicArray()
        for i in range(10):
            arr.append(i)

        self.assertEqual(len(arr), 10)  # Check if length is correct
        self.assertEqual(arr[7], 3)  # Check element at index 7

    def test_empty_array(self):
        arr = DynamicArray()

        self.assertEqual(len(arr), 0)  # Check length of an empty array
        with self.assertRaises(IndexError):
            arr[0]  # Check accessing an element in an empty array


# if __name__ == "__main__":
#     unittest.main()
