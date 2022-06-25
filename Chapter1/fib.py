import unittest

def fib(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    return fib(n-1) + fib(n-2)

def memo_fib(n, memo):
    if n <= 0:
        return 0
    if n==1:
        return 1
    if memo[n] > 0:
        return memo[n]
    memo[n] = memo_fib(n-1, memo) + memo_fib(n-2, memo)
    return memo[n]

def run_memo_fib(n):
    m = [0] * (n+1)
    return memo_fib(n, m)


class Test(unittest.TestCase):
    def test_fib(self):
        print(fib(7))
    def test_memo_fib(self):
        print(run_memo_fib(7))