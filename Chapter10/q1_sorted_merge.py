import unittest

def sorted_merge(a, b, last_idx_a):
    index_a = last_idx_a
    index_b = len(b) - 1
    index_merged = index_a + index_b +1 # end of merged array

    # merge a and b, starting from last element in each
    # and adding elements to the end of a
    while(index_b >= 0):
        if (index_a >=0) and (a[index_a] > b[index_b]):
            a[index_merged] = a[index_a]
            index_a -= 1
        else:
            a[index_merged] = b[index_b]
            index_b -= 1
        index_merged -= 1
    return a

class Tests(unittest.TestCase):

    def test_sorted_merge(self):
        list_a = [1, 3, 4, 5, 9, None, None, None, None, None]
        list_b = [2, 6, 7, 8, 10]
        sorted_list = sorted_merge(list_a, list_b, 4)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], sorted_list)

if __name__ == '__main__':
    unittest.main()

