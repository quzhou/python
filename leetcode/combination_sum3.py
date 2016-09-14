"""https://leetcode.com/problems/combination-sum-iii/
Find all possible combinations of k numbers that add up to a number n, given that only numbers
from 1 to 9 can be used and each combination should be a unique set of numbers.

Example 1:
k = 3, n = 7
output: [1, 2, 4]

Example 2:
k = 3, n = 9
output:
[
    [1, 2, 6],
    [1, 3, 5],
    [2, 3, 4]
]
Thus number can't be used repeatedly. No [3, 3, 3].
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        output = []
        self.helper(k, n, [1, 2, 3, 4, 5, 6, 7, 8, 9], output)
        return output

    def helper(self, k, n, candidates, result):
        if k == 1:
            if n in candidates:
                result.append([n])
            return

        if len(candidates) == k:
            if sum(candidates) == n:
                result.append(candidates)
            return

        rightlist1 = []
        self.helper(k, n, candidates[1:], rightlist1)
        rightlist2 = []
        self.helper(k-1, n - candidates[0], candidates[1:], rightlist2)

        for elem in rightlist1:
            result.append(elem)
        for elem in rightlist2:
            result.append([candidates[0]] + elem)

if __name__ == "__main__":
    print Solution().combinationSum3(3, 9)


