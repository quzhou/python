"""https://leetcode.com/problems/add-two-numbers/
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 and l2:
            tmp = l1.val + l2.val + carry
            cur.next = ListNode(tmp % 10)
            carry = tmp / 10
            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        list = l1 or l2
        while list:
            cur.next = ListNode((list.val + carry) % 10)
            carry = (list.val + carry) / 10
            list = list.next
            cur = cur.next

        if carry > 0:
            cur.next = ListNode(carry)

        return dummy.next


