import unittest
from typing import List
from Chapter4.binary_tree import BinaryTreeNode
import math


# Given a sorted (increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height

def create_minimal_tree(arr, left, right):
    if right < left:
        return None
    mid = math.floor((left + right) / 2)
    n: BinaryTreeNode = BinaryTreeNode(arr[mid])
    n.left = create_minimal_tree(arr, left, mid-1)
    n.right = create_minimal_tree(arr, mid+1, right)
    return n

def minimal_tree(arr: List[int]):
    return create_minimal_tree(arr, 0, len(arr) -1)

class Tests(unittest.TestCase):

    def test_minimal_tree(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 9, 13]
        bst: BinaryTreeNode = minimal_tree(arr)
        bst.print_tree()


if __name__ == '__main__':
    unittest.main()