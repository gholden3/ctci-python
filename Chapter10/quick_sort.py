import unittest
from typing import List
import math

def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

def partition(arr, left, right):
    # last element will be pivot
    pivot_val = arr[right]
    # ptr represents the index to place pivot value where
    # everything to the left is lower than pivot value.
    ptr = left
    for i in range(left, right):
        val_i = arr[i]
        # if val_i is smaller than pivot
        if val_i <= pivot_val:
            # move val_i into the pointer spot and move
            # the value that was in the pointer into i^th index, so that
            # the pointer can be moved right and the lesser value, vali_i, is to the left
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
        # Finally swapping the last element with the pointer indexed number
    arr[ptr], arr[right] = arr[right], arr[ptr]
    return ptr

def quicksort(arr: List[int], left: int, right: int):
    # pick an index and partition st all numbers to left are less
    # and all numbers to the right are greater than element at index
    if len(arr) == 1:
        return arr
    if left < right:
        index: int = partition(arr, left, right)
        quicksort(arr, left, index-1)
        quicksort(arr, left, index-1)

def quick_sort(in_arr: List[int]):
    quicksort(in_arr, 0, len(in_arr) - 1 )
    return in_arr


class Tests(unittest.TestCase):

    def test_quick_sort(self):
        unsorted = [9, 6, 3, 4, 5, 1, 7, 8]
        sorted_answer = quick_sort(unsorted)
        self.assertEqual(sorted_answer, [1, 3, 4, 5, 6, 7, 8, 9])

        unsorted = [9, 6, 3, 4, 12, 13,  5, 10, 7, 11, 8, 15]
        sorted_answer = quick_sort(unsorted)
        self.assertEqual(sorted_answer, [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15])

if __name__ == '__main__':
    unittest.main()

