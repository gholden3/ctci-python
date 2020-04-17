import unittest

class StackNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = StackNode(data)
        node.next = self.top
        self.top = node

    def is_empty(self) -> bool:
        return (self.top is None)

    def peek(self):
        return self.top.data

    def pop(self) -> StackNode:
        ''' pops an item off of the top of the stack'''
        if not self.top:
            return -1
        item = self.top
        self.top = self.top.next
        return item

class Test(unittest.TestCase):
    def test_is_empty(self):
        my_stack = MyStack()
        self.assertTrue(my_stack.is_empty())
        my_stack.push(3)
        self.assertFalse(my_stack.is_empty())
    def test_peek(self):
        my_stack = MyStack()
        my_stack.push(6)
        self.assertEqual(6, my_stack.peek())

    def test_pop(self):
        my_stack = MyStack()
        my_stack.push(5)
        my_stack.pop()
        self.assertTrue(my_stack.is_empty())

if __name__ == "__main__":
    unittest.main()