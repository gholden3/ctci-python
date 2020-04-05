# O(N)
import unittest
from collections import Counter

def pal_perm(phrase):
    '''function checks if a string is a permutation of a palindrome or not'''
    counter = Counter(phrase.replace(' ', '').lower())
    odds = [val%2 for val in counter.values()]
    count_of_odds_in_counter = sum(odds)
    return count_of_odds_in_counter <= 1

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
