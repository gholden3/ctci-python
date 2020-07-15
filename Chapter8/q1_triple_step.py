# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps
# at a time. Implement a method to count how many possible ways the child can run up the stairs
import unittest

def triple_step(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)


def Method2(x):
    memo = [-1] * (x + 1)
    return TripleHopRecursive(x, memo)


def TripleHopRecursive(x, memo):
    if x < 0:
        return 0
    memo[0] = 1
    if x >= 1:
        memo[1] = 1
    if x >= 2:
        memo[2] = memo[1] + memo[0]
    if x > 2:
        for i in range(3, x + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[x]

class Test(unittest.TestCase):
    """Test Cases"""
    # test cases in the form (n,p)
    # where n is the number of steps in the staircase
    # and p is the expected number of paths available to get there
    test_cases = [
        (1,  1),
        (2, 2),
        (3, 4),
        (4, 7)
    ]

    def test_triple_step(self):
        for (n, expected) in self.test_cases:
            actual = triple_step(n)
            self.assertEqual( expected, actual)

if __name__ == "__main__":
    unittest.main()