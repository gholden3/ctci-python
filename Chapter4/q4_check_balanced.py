# implement a function to check if a binary tree is balanced. 
# for the purposes of this question, a balanced tree is defined to be a tree such that the heights
# of the two subtrees of any node never differ by more than one


import unittest
from Chapter4.binary_tree import BinaryTreeNode

ERROR = -3


def check_height(node: BinaryTreeNode) -> int:
    if node is None:
        return -1
    left_height = check_height(node.left)
    if left_height is ERROR:
        return ERROR

    right_height = check_height(node.right)
    if right_height is ERROR:
        return ERROR

    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return ERROR
    else:
        return max(left_height, right_height) + 1


def check_balanced(binary_tree_node: BinaryTreeNode) -> bool:
    return check_height(binary_tree_node) != -3


class Test(unittest.TestCase):
    def test_balanced_true_perfect(self):
        #          1
        #       /     \
        #      2        3
        #    /   \     / \
        #   4     5   6    7
        six_node = BinaryTreeNode("6")
        seven_node = BinaryTreeNode("7")
        three_node = BinaryTreeNode("3")
        three_node.left = six_node
        three_node.right = seven_node
        four_node = BinaryTreeNode("4")
        five_node = BinaryTreeNode("5")
        two_node = BinaryTreeNode("2")
        two_node.left = four_node
        two_node.right = five_node
        one_node = BinaryTreeNode("1")
        one_node.left = two_node
        one_node.right = three_node
        balanced = check_balanced(one_node)
        self.assertTrue(balanced)

    def test_balanced_true(self):
        #          1
        #       /     \
        #      2        3
        #    /   \     /
        #   4     5   6
        six_node = BinaryTreeNode("6")
        three_node = BinaryTreeNode("3")
        three_node.left = six_node
        four_node = BinaryTreeNode("4")
        five_node = BinaryTreeNode("5")
        two_node = BinaryTreeNode("2")
        two_node.left = four_node
        two_node.right = five_node
        one_node = BinaryTreeNode("1")
        one_node.left = two_node
        one_node.right = three_node
        balanced = check_balanced(one_node)
        self.assertTrue(balanced)

    def test_balanced_false(self):
        #          1
        #       /     \
        #      2        3
        #    /   \     /
        #   4     5   6
        #         |
        #         7
        #         |
        #         8
        six_node = BinaryTreeNode("6")
        three_node = BinaryTreeNode("3")
        three_node.left = six_node
        four_node = BinaryTreeNode("4")
        eight_node = BinaryTreeNode("8")
        seven_node = BinaryTreeNode("7")
        seven_node.left = eight_node
        five_node = BinaryTreeNode("5")
        five_node.left = seven_node
        two_node = BinaryTreeNode("2")
        two_node.left = four_node
        two_node.right = five_node
        one_node = BinaryTreeNode("1")
        one_node.left = two_node
        one_node.right = three_node
        balanced = check_balanced(one_node)
        self.assertFalse(balanced)


if __name__ == "__main__":
    unittest.main()
