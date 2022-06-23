import unittest

def fib(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    return fib(n-1) + fib(n-2)


class Test(unittest.TestCase):
    def test_fib(self):
        print(fib(7))