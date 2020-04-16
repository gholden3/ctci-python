#implement an algorithm to determine if a string has all unique charachters. 
# what if you cannot use additional data structures?
# O(N)
import unittest


def is_unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


class IsUniqueTest(unittest.TestCase):
    def test_unique_true(self):
        data_true = [('abcd'), ('s4fad'), ('')]
        for test_string in data_true:
            actual = is_unique(test_string)
            self.assertTrue(actual)

    def test_unique_false(self):
        data_false = [('23ds2'), ('hb 627jh=j ()')]
        for test_string in data_false:
            actual = is_unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
