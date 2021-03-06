"""https://leetcode.com/problems/integer-break/
Given a positive integer n, break it into the sum of at least two positive integers and
maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int, 2 <= n <= 58
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4

        maxp = [0, 1, 2, 3, 4]
        for i in range(5, n+1):
            maxVal = 0
            for k in range(1, i):
                val = maxp[k] * maxp[i-k]
                if val > maxVal:
                    maxVal = val
            maxp.append(maxVal)

        return maxp[n]


if __name__ == "__main__":
    print Solution().integerBreak(8)






