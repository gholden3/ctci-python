# implement a method to perform basic string compression using the counts of repeated characters.
# see test cases for examples.
# if the "compressed" string would not become smaller than the original string, your method shoudl return the original string.
# you can assume the string has only uppsercase and lowercase letters (a-z)
# the book notes something about stringbuilder in java to avoid the n^2 cost of string concatenation but there is
# no direct correlation in python. instead, list append is considered O(1) so runtime here is O(p + k) where p is the
# size of original string and k is number of charachter sequences.
# the book also notes a case where you might want to check the resulting compressed length before you start
# actually building the string because it might save you some time if you dont expect to have a lot of repeating
# charachters. its simple implementation and actually increases run time if you do have good compression,
# so have omitted it here.
import unittest


def string_compression(string):
    compressed = []
    counter = 0

    for i in range(len(string)):
        if (i != 0) and (string[i] != string[i - 1]):
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, ''.join(compressed), key=len)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
