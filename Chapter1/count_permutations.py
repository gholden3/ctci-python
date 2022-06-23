import unittest

def permutation(str, prefix):
    if len(str) == 0:
        print(prefix)
    else:
        for i in range(0, len(str)):
            rem = str[0:i] + str[i+1:]
            permutation(rem, prefix + str[i])

def run_permutation(str):
    permutation(str, '')


class Test(unittest.TestCase):
    def test_permutations(self):
        run_permutation('gina')
