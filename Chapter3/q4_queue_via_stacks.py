# implement a MyQueue class which implements a queue using two stacks
import unittest
from Chapter3.stack import MyStack

class QueueStacks:
    def __init__(self):
        self.oldStack = MyStack()
        self.newStack = MyStack()

    def push(self, data):
        self.oldStack.push(data)
    def peek(self):
        return self.oldStack.peek().data
    def pop(self):
        return self.oldStack.pop().data


class Tests(unittest.TestCase):
    def test_queue_stacks(self):
        stacks = QueueStacks()
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        self.assertEqual(lst, list(reversed(range(35))))


if __name__ == '__main__':
    unittest.main()