from typing import List
import math
import unittest

def binary_search(a: List, x, low, high):
    if low > high:
        return -1
    mid = math.floor( (low + high) / 2)
    if a[mid] < x:
        return binary_search(a, x, mid+1, high)
    elif a[mid] > x:
        return binary_search(a, x, low, mid-1)
    else:
        return mid


class Tests(unittest.TestCase):

    def test_merge_sort(self):
        a = [2, 4, 5, 6, 7, 8, 9, 11]
        res = binary_search(a, 8, 0, len(a))
        self.assertEqual(res, 5)

if __name__ == '__main__':
    unittest.main()
