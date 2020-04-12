# given two singly linked lists, determine if the two lists intersect. return the intersecting node. 
# note that intersection is defined based on reference, not value. that is, if the kth node in the first list 
# is the exact same node (by reference) as the jth node of the second linked list, they are intersecting. 

from LinkedList import LinkedList
import unittest

def intersection(list1, list2):
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for i in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


class Test(unittest.TestCase):
  def test_intersection_true(self):
    tail = LinkedList([7, 2, 1])
    list_one = LinkedList([3, 1, 5, 9])
    list_one.append_node_to_tail(tail.head)
    list_two = LinkedList([4, 6])
    list_two.append_node_to_tail(tail.head)
    self.assertEqual(tail.head, intersection(list_one, list_two))

  def test_false(self):
    list_one = LinkedList([3, 1, 5, 9, 7, 2, 1])
    list_two = LinkedList([4, 6, 7, 2, 1])
    self.assertFalse(intersection(list_one, list_two))

if __name__ == "__main__":
    unittest.main()