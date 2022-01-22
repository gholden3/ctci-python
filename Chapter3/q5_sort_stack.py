# write a program to sort a stack such that the smallest items are on top.
# you can use any additional temporary stack, but you may not dopy the elements into any other data structure,
# such as an array. The stack supports the following operations: push, pop, peek, and isEmpty
import unittest
from Chapter3.stack import MyStack
from typing import List

# two stacks: left and right. right starts off empty and left starts out unsorted
def sort_stack(left_stack: MyStack):
    right_stack = MyStack()

    # while unsorted elements remain in left stack
    while not left_stack.is_empty():
        # pick up a plate off the unsorted stack and hold it
        temp = left_stack.pop().data

        #  the right stack is guaranteed to be sorted high to low, so if any items on the right stack are higher
        # than the plate you have in your hand, move them to the left stack
        while not right_stack.is_empty() and (right_stack.peek() > temp):
            left_stack.push(right_stack.pop().data)

        # then place the plate in your hand on the right stack, which remains sorted
        right_stack.push(temp)

    #then finally since your right stack is now sorted top to bottom with largest to smallest, move all
    # the plates over to the left and the left will now be sorted top to bottom smallest to largest
    while not right_stack.is_empty():
        left_stack.push(right_stack.pop().data)

    return left_stack




class Tests(unittest.TestCase):
    # tests if stack contents match the given list, from top to bottom
    def test_stack_contents(self, stack, comparison_order: List):
        for val in comparison_order:
            stack_value = stack.pop().data
            self.assertEqual(val, stack_value)
        return True

    def test_sort_stack(self):
        test_stack = MyStack()
        for val in [7, 10, 12, 8, 6, 9, 5, 1, 2]:
            test_stack.push(val)
        sorted_stack = sort_stack(test_stack)
        sorted_order = [1, 2, 5, 6, 7, 8, 9, 10, 12]
        is_sorted = self.test_stack_contents(sorted_stack, sorted_order)
        self.assertTrue(is_sorted)


if __name__ == '__main__':
    unittest.main()

