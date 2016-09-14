"""https://leetcode.com/problems/combination-sum-iv/
Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive integer target.

Example:
nums = [1, 2, 3], target = 4
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.
Therefore the output is 7.
"""

class Solution(object):
    # Consider nums[i] is missing foreach 0 <= i < size
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [1]
        for i in range(1, target+1):
            sum = 0
            for num in nums:
                if i >= num:
                    sum += dp[i - num]
            dp.append(sum)
        return dp[target]


if __name__ == "__main__":
    print Solution().combinationSum4([1, 2, 3], 4)


