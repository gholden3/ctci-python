import unittest
import math

def insertion_sort(l):
    for i in range(1, len(l)):

        key = l[i]

        # Move elements of l[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l


def bucket_sort(arr, n):
    if n <= 0:
        return

    # 1) Create n empty buckets
    buckets = [0] * n

    for i in range( n):
        buckets[i] = []

    # 2) Put array elements in different buckets
    for i in range( n):
        idx = arr[i] * n
        buckets[math.floor(idx)].append(arr[i])

    # 3) Sort individual buckets
    # Sort individual buckets
    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])
    # 4) Concatenate all buckets into arr[]
    index = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[index] = buckets[i][j]
            index += 1

class Test(unittest.TestCase):
    def test_bs(self):
        arr =[0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
        n = len(arr)
        bucket_sort(arr, n)
        print(arr)
        self.assertEqual(arr, [ 0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897 ])
