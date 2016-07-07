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
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        head = None
        if list1.data <= list2.data:
            head = list1
        else:
            head = list2

        cur1 = list1.next
        cur2 = list2.next
        cur = head
        while cur1 and cur2:
            if cur1.data <= cur2.data:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2


