"""https://leetcode.com/problems/valid-perfect-square/
Given a positive integer num, write a function which returns True if num is a perfect
square else False.

Note: Do not use any built-in library function such as sqrt.
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :param num:
        :return: True or False
        """
        low, high = 0, num
        while low <= high:
            i = low + (high - low) / 2
            tmp = i * i
            if tmp == num:
                return True
            elif tmp < num:
                low = i + 1
            elif tmp > num:
                high = i - 1

        return False
