from typing import List
import math
import unittest
# driver function


def merge(array, low, middle, high):
    # copy both halves into a helper array
    helper = [0]*len(array)
    helper[low:high+1] = array[low:high+1]
    helper_left = low
    helper_right = middle+1
    current = low # current keeps track of destination index in real array

    # iterate through the helper array. compare the left and right and copy the smaller
    # value into the real array
    while (helper_left <= middle) and (helper_right <= high):
        if helper[helper_left] <= helper[helper_right]:
            array[current] = helper[helper_left]
            helper_left += 1
        else:
            array[current] = helper[helper_right]
            helper_right += 1
        current += 1
    # if we exited the loop before left side was finished copying over, we need to copy
    # all the remaining elements
    remaining = middle+1 - helper_left
    for i in range(0, remaining):
        array[current+i] = helper[helper_left + i]



def mergesort(array, low, high):
    if(low < high):
        print(f"in mergesort. low: {low}, high: {high}")
        middle = math.floor((low+high)/2)
        print('sorting left')
        mergesort(array, low, middle) # sort the left half
        print('sorting right')
        mergesort(array,  middle + 1, high)
        print(f'calling merge. array: {array} low: {low}, middle: {middle}, high: {high}')
        merge(array, low, middle, high)
        print(f"merged: {array}")

def merge_sort(in_arr: List[int]):
    mergesort(in_arr, 0, len(in_arr)-1)
    return in_arr


class Tests(unittest.TestCase):

    def test_merge_sort(self):
        unsorted = [9, 6, 3, 4, 5, 1, 7, 8]
        sorted_answer = merge_sort(unsorted)
        self.assertEqual(sorted_answer, [1, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()

