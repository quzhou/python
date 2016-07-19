"""https://leetcode.com/problems/merge-two-sorted-lists/
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""

class ListNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution(object):
    def merge_list(self, list1, list2):
        """
        :param list1:
        :param list2:
        :return: new list
        """
        curr = dummy = ListNode(0)
        while list1 and list2:
            if list1.data < list2.data:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next

