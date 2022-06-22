# implement a function to check if a binary tree is a binary search tree
import unittest
from Chapter4.binary_tree import BinaryTreeNode

def check_if_bst(node: BinaryTreeNode, min, max):
    # stop condition
    if node is None:
        return True

    if check_if_bst(node.left, min, node.data) and check_if_bst(node.right, node.data, max):
        if (min and node.data <= min) or (max and node.data > max):
            return False
        else:
            return True
    else:
        return False

    # if ((min != null & & n.data <= min) | | (max != null & & n.data > max)) {
    # return false;
    # }
    # if (!checkBST(n.left, min, n.data) | |
    #     !checkBST(n.right, n.data, max)) {
    #     return false;
    # }
    # return true;

def run_check_if_bst(node):
    return check_if_bst(node, None, None)

class Test(unittest.TestCase):
    def test_bst_true(self):
        #     2
 #           / \
 #          /   \
 #          2   3
 #               \
 #               4

        three_node = BinaryTreeNode("3")
        four_node = BinaryTreeNode("4")
        three_node.right = four_node
        two_node = BinaryTreeNode("2")
        two_node2 = BinaryTreeNode('2')
        two_node.left = two_node2
        two_node.right = three_node

        bst = run_check_if_bst(two_node)
        self.assertTrue(bst)
        #
        #        2
        #       / \
        #      /  \
        #      1   2
        #           \
        #              4

    def test_bst_false(self):
        two_node = BinaryTreeNode("2")
        two_node2 = BinaryTreeNode('2')
        one_node = BinaryTreeNode('1')
        four_node = BinaryTreeNode('4')
        two_node2.right = four_node
        two_node.left = one_node
        two_node.right = two_node2

        bst = run_check_if_bst(two_node)
        self.assertFalse(bst)


      #
        #        5
        #       / \
        #      /  \
        #      3   7
        #       \    \
        #        6     8

    def test_bst_false_all_children(self):
        five_node = BinaryTreeNode("5")
        three_node = BinaryTreeNode('3')
        six_node = BinaryTreeNode('6')
        seven_node = BinaryTreeNode('7')
        eight_node = BinaryTreeNode('8')
        three_node.right = six_node
        five_node.left = three_node
        seven_node.right = eight_node
        five_node.right = seven_node

        bst = run_check_if_bst(five_node)
        self.assertFalse(bst)
