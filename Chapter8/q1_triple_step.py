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


def triple_step_memo_runner(n):
    path_counts = [-1] * (n+1)
    return triple_step_memo(n, path_counts)


def triple_step_memo(n, path_counts):
    if n < 0:
        return 0
    if n == 0:
        return 1
    # check to see if the value has already been computed
    if path_counts[n] > -1:
        return path_counts[n]
    #otherwise calculate the number of paths to this step
    path_counts[n] = triple_step_memo(n-1, path_counts) + \
                     triple_step_memo(n-2, path_counts) + triple_step_memo(n-3, path_counts)
    return path_counts[n]


class Test(unittest.TestCase):
    """Test Cases"""
    # test cases in the form (n,p)
    # where n is the number of steps in the staircase
    # and p is the expected number of paths available to get there
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 4),
        (4, 7)
    ]

    def test_triple_step(self):
        for (n, expected) in self.test_cases:
            actual = triple_step(n)
            self.assertEqual(expected, actual)

    def test_triple_step_with_memo(self):
        for (n, expected) in self.test_cases:
            actual = triple_step_memo_runner(n)
            self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
