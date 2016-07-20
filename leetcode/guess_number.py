"""https://leetcode.com/problems/guess-number-higher-or-lower/
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0)

Example:
n = 10, I pick 6. Return 6.
"""

class Solution(object):
    def guess_number(self, n):
        """
        :param n: int
        :return: int
        """
        low, high = 1, n
        while low <= high:
            mid = low + (high - low) / 2
            val = guess(mid)
            if val == 0:
                return mid
            elif val > 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0
