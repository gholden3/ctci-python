# given a binary tree, design an algorithm which creates a linked list of all the
# nodes at each depth (eg if you have a tree with depth D, you'll have D linked lists)

import unittest
from Chapter4.binary_tree import BinaryTreeNode
from typing import List
from Chapter2.LinkedList import LinkedList, LinkedListNode


def list_of_depths(root_node: BinaryTreeNode, lists: List[LinkedList], level: int) -> List[LinkedList]:
    # base case. bottom of the tree
    if root_node is None:
        return

    if len(lists) == level:
        # this level is not contained in the list. 
        # since levels are traversed in order, if this is the first item
        # at this level, we can insert the list at the end of the array
        ll = LinkedList()
        lists.append(ll)
    else:
        # this level is in the list
        ll: LinkedList = lists[level]
    ll_node = LinkedListNode(root_node.data)
    ll.append_node_to_tail(ll_node)
    list_of_depths(root_node.left, lists, level + 1)
    list_of_depths(root_node.right, lists, level + 1)
    return lists


def run_list_of_depths(binary_tree: BinaryTreeNode) -> List[LinkedList]:
    return list_of_depths(binary_tree, [], 0)

    


class Test(unittest.TestCase):
    def test_list_of_depths(self):

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
        response = run_list_of_depths(one_node)
        list_one: LinkedList = response[0]
        self.assertEqual('1', list_one.head.value)
        list_two = response[1]
        self.assertEqual('2', list_two.head.value)
        list_three = response[2]
        self.assertEqual('4', list_three.head.value)


if __name__ == "__main__":
    unittest.main()